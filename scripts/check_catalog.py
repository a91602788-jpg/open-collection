"""Validate public catalog data and its Markdown representation (standard library)."""
import datetime
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = re.compile(r'[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+\Z')


def entry_errors(entry, category_ids):
    errors = []
    repo = entry.get('repo', '')
    if not isinstance(repo, str) or not REPOSITORY.fullmatch(repo):
        errors.append('invalid repository name')
    if entry.get('url') != 'https://github.com/' + repo:
        errors.append('URL must equal the canonical GitHub repository URL')
    if type(entry.get('id')) is not int or entry['id'] <= 0:
        errors.append('a positive stable repository ID is required')
    if entry.get('category') not in category_ids:
        errors.append('unknown category')
    if entry.get('kind') not in {'starter', 'software', 'collection', 'learning', 'reference'}:
        errors.append('unknown resource kind')
    if 'resource_type' in entry and entry['resource_type'] not in {'application', 'library', 'sdk', 'toolkit', 'specification', 'dataset', 'learning'}:
        errors.append('unknown detailed resource type')
    if entry.get('archived') is not False or entry.get('fork') is not False:
        errors.append('archived repositories and forks are excluded')
    if entry.get('verification') != 'metadata-checked':
        errors.append('unsupported verification claim')
    if not isinstance(entry.get('license_spdx'), str) or not entry['license_spdx'].strip():
        errors.append('license or CHECK-LICENSE placeholder is required')
    if entry.get('license_spdx') == 'NOASSERTION':
        errors.append('use CHECK-LICENSE for unrecognized terms')
    if entry.get('license_url') != entry.get('url'):
        errors.append('license evidence must point to the upstream repository')
    description = entry.get('description')
    if not isinstance(description, str) or not description.strip() or len(description.split()) > 24:
        errors.append('upstream description must contain 1–24 words')
    for field in ('pricing', 'deployment'):
        if entry.get(field) != 'not-reviewed':
            errors.append(field + ' needs a schema/evidence update before making claims')
    if entry.get('stack_status') != 'primary-language-only':
        errors.append('do not imply primary language is a complete stack')
    if (entry.get('summary_ru') is None) != (entry.get('summary_en') is None):
        errors.append('original summaries must provide both languages')
    if entry.get('description_origin', '').startswith('Original editorial') and not all(isinstance(entry.get(k), str) and entry[k].strip() for k in ('summary_ru', 'summary_en')):
        errors.append('editorial descriptions require complete RU/EN summaries')
    try:
        datetime.date.fromisoformat(entry['checked_at'])
        datetime.datetime.fromisoformat(entry['pushed_at'].replace('Z', '+00:00'))
    except (KeyError, TypeError, ValueError, AttributeError):
        errors.append('invalid evidence date')
    source = entry.get('source')
    if not isinstance(source, dict) or source.get('url') != entry.get('url'):
        errors.append('canonical primary source is required')
    return errors


def catalog_errors(data):
    errors = []
    if data.get('schema_version') not in {1, 2}:
        errors.append('unsupported schema version')
    categories = data.get('categories', [])
    ids = [c['id'] for c in categories]
    if len(ids) != len(set(ids)):
        errors.append('duplicate category ID')
    for slug in ids:
        if not re.fullmatch(r'\d{2}-[a-z0-9-]+', slug):
            errors.append('invalid category folder: ' + slug)
    seen_names, seen_ids = set(), set()
    entries = data.get('entries', [])
    for entry in entries:
        name = entry.get('repo', '')
        errors.extend(name + ': ' + e for e in entry_errors(entry, set(ids)))
        if data.get('schema_version') == 1 and (entry.get('kind') == 'reference' or 'resource_type' in entry or 'subcategory' in entry):
            errors.append('schema 2 is required for detailed classification: ' + name)
        if name.lower() in seen_names:
            errors.append('duplicate repository name: ' + name)
        if entry.get('id') in seen_ids:
            errors.append('duplicate repository ID: ' + str(entry.get('id')))
        seen_names.add(name.lower())
        seen_ids.add(entry.get('id'))
        if entry.get('checked_at') != data.get('checked_at'):
            errors.append('entry date differs from snapshot date: ' + name)
        category = next((c for c in categories if c['id'] == entry.get('category')), {})
        subcategories = category.get('subcategories', [])
        if subcategories and entry.get('subcategory') not in {s['id'] for s in subcategories}:
            errors.append('missing or unknown subcategory: ' + name)
        if not subcategories and 'subcategory' in entry:
            errors.append('subcategory has no category definition: ' + name)
    for category in categories:
        actual = sum(e.get('category') == category['id'] for e in entries)
        if actual != category.get('count') or actual == 0:
            errors.append('category count mismatch: ' + category['id'])
        subcategories = category.get('subcategories', [])
        if len({s['id'] for s in subcategories}) != len(subcategories):
            errors.append('duplicate subcategory ID: ' + category['id'])
        for subcategory in subcategories:
            actual = sum(e.get('category') == category['id'] and e.get('subcategory') == subcategory['id'] for e in entries)
            if actual != subcategory.get('count') or actual == 0:
                errors.append('subcategory count mismatch: ' + category['id'] + '/' + subcategory['id'])
    if not entries:
        errors.append('catalog must not be empty')
    return errors


def markdown_errors(root, data):
    errors = []
    for category in data['categories']:
        path = root / category['id'] / 'README.md'
        if not path.is_file():
            errors.append('missing category README: ' + category['id'])
            continue
        found = re.findall(r'^#{2,3} \[([^\]]+)\]\((https://github.com/[^)]+)\)$', path.read_text(), re.M)
        expected = [(e['repo'], e['url']) for e in data['entries'] if e['category'] == category['id']]
        if found != expected:
            errors.append('Markdown/data entry mismatch: ' + category['id'])
    root = root.resolve()
    for path in root.rglob('*.md'):
        if '.git' in path.relative_to(root).parts:
            continue
        for link in re.findall(r'\]\(([^)\s]+)\)', path.read_text()):
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f'broken/unsafe local link in {path.relative_to(root)}: {link}')
    return errors


def main():
    data = json.loads((ROOT/'data/catalog.json').read_text())
    errors = catalog_errors(data) + markdown_errors(ROOT, data)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(data['entries'])} unique repositories; {len(data['categories'])} categories; data, Markdown and local links agree.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
