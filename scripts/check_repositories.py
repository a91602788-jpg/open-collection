"""Read-only live checks against GitHub; never runs listed projects."""
import json
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


class NoRedirect(urllib.request.HTTPRedirectHandler):
    # Do not forward an authenticated request to a redirected host.
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch(batch, token):
    fields = []
    for i, entry in enumerate(batch):
        if not re.fullmatch(r'[A-Za-z0-9-]+/[A-Za-z0-9_.-]+', entry['repo']):
            raise ValueError('Invalid repository name')
        owner, name = entry['repo'].split('/')
        fields.append(f'r{i}:repository(owner:{json.dumps(owner)},name:{json.dumps(name)})'
                      '{databaseId nameWithOwner isArchived isFork isPrivate isDisabled}')
    payload = json.dumps({'query': '{' + ' '.join(fields) + '}'}).encode()
    request = urllib.request.Request('https://api.github.com/graphql', data=payload,
                                    headers={'Authorization': 'Bearer '+token,
                                             'Content-Type': 'application/json',
                                             'User-Agent': 'open-collection-link-check'})
    opener = urllib.request.build_opener(NoRedirect())
    for attempt in range(3):
        try:
            with opener.open(request, timeout=30) as response:
                result = json.load(response)
            fatal = [e for e in result.get('errors', []) if e.get('type') != 'NOT_FOUND']
            if fatal:
                raise RuntimeError('GitHub GraphQL returned an error; no success was assumed')
            if not isinstance(result.get('data'), dict):
                raise RuntimeError('GitHub returned no repository data')
            return result['data']
        except urllib.error.HTTPError as error:
            if error.code not in {429, 500, 502, 503, 504} or attempt == 2:
                raise RuntimeError(f'GitHub HTTP {error.code}; live check incomplete') from None
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise RuntimeError('GitHub unavailable; live check incomplete') from None
        time.sleep(2 ** attempt)
    raise RuntimeError('GitHub live check incomplete')


def main():
    token = os.environ.get('GH_TOKEN')
    if not token:
        print('GH_TOKEN is required for read-only GitHub API access.', file=sys.stderr)
        return 1
    entries = json.loads((ROOT/'data/catalog.json').read_text())['entries']
    problems = []
    for start in range(0, len(entries), 25):
        batch = entries[start:start+25]
        data = fetch(batch, token)
        for i, entry in enumerate(batch):
            current = data.get(f'r{i}')
            if not current:
                problems.append(entry['repo']+': not publicly resolvable')
            elif current['databaseId'] != entry['id']:
                problems.append(entry['repo']+': stable repository ID changed')
            elif current['nameWithOwner'] != entry['repo']:
                problems.append(entry['repo']+': canonical name is '+current['nameWithOwner'])
            elif any(current[k] for k in ('isArchived', 'isFork', 'isPrivate', 'isDisabled')):
                problems.append(entry['repo']+': archive/fork/access state changed')
        print(f'Checked {min(start+25,len(entries))}/{len(entries)} public repositories', flush=True)
    summary = f"Checked {len(entries)} GitHub repositories. Changes requiring review: {len(problems)}.\n"
    if problems:
        summary += '\n'+'\n'.join('- '+p for p in problems)+'\n'
    print(summary)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as file:
            file.write(summary)
    return 1 if problems else 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)
