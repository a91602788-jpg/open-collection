"""Check the uncounted discovery queue independently from the curated catalog."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]


def queue_errors(index, shards, catalog_ids):
    errors=[]
    topics=index.get('topics',[])
    topic_ids={t['id'] for t in topics}
    if len(topic_ids)!=len(topics):errors.append('duplicate research topic')
    seen=set()
    for topic in topics:
        if topic.get('status') not in {'catalog','proposed'}:
            errors.append('invalid topic status: '+topic['id'])
        if topic['id'] not in shards:
            errors.append('missing candidate shard: '+topic['id']);continue
        rows=shards[topic['id']].get('candidates',[])
        if topic.get('candidate_count')!=len(rows):errors.append('candidate count mismatch: '+topic['id'])
        for row in rows:
            repo=row.get('repo','')
            if type(row.get('id')) is not int or row['id']<=0:errors.append('invalid candidate ID')
            if row.get('id') in seen:errors.append('duplicate candidate ID: '+str(row.get('id')))
            seen.add(row.get('id'))
            if row.get('id') in catalog_ids:errors.append('already counted in catalog: '+repo)
            if not re.fullmatch(r'[A-Za-z0-9-]+/[A-Za-z0-9_.-]+',repo) or row.get('url')!='https://github.com/'+repo:
                errors.append('invalid candidate URL: '+repo)
            if row.get('review_status')!='pending-editorial-review':errors.append('candidate cannot claim editorial acceptance: '+repo)
            if not row.get('license_spdx'):errors.append('missing candidate license signal: '+repo)
            if row.get('archived') is not False or row.get('fork') is not False:
                errors.append('excluded archive/fork in candidate queue: '+repo)
            if not row.get('matched_topic_ids') or not set(row['matched_topic_ids'])<=topic_ids:
                errors.append('invalid matched topics: '+repo)
            if row.get('primary_topic_id')!=topic['id'] or topic['id'] not in row.get('matched_topic_ids',[]):
                errors.append('candidate primary topic disagrees with its shard: '+repo)
    if index.get('unique_candidates')!=len(seen):errors.append('unique candidate total mismatch')
    return errors


def main():
    index=json.loads((ROOT/'research/topics.json').read_text())
    catalog=json.loads((ROOT/'data/catalog.json').read_text())
    shards={}
    errors=[]
    for topic in index['topics']:
        path=(ROOT/topic['data_path']).resolve()
        if not path.is_relative_to((ROOT/'research/candidates').resolve()) or not path.is_file():
            errors.append('missing/unsafe candidate path: '+topic['id']);continue
        content=path.read_bytes()
        if len(content)!=topic['bytes'] or hashlib.sha256(content).hexdigest()!=topic['sha256']:
            errors.append('stale candidate size/hash: '+topic['id'])
        shards[topic['id']]=json.loads(content)
    errors+=queue_errors(index,shards,{e['id'] for e in catalog['entries']})
    actual_categories={c['id'] for c in catalog['categories']}
    declared={t['id'] for t in index['topics'] if t['status']=='catalog'}
    if actual_categories!=declared:errors.append('research map disagrees with published category IDs')
    if index.get('catalog_entries')!=len(catalog['entries']) or index.get('catalog_categories')!=len(catalog['categories']):
        errors.append('research summary disagrees with catalog counts')
    expected_paths={t['data_path'] for t in index['topics']}
    actual_paths={p.relative_to(ROOT).as_posix() for p in (ROOT/'research/candidates').glob('*.json')}
    if expected_paths!=actual_paths:errors.append('orphan or missing candidate file')
    if len(index['topics'])!=index.get('searched_topics'):errors.append('search coverage count mismatch')
    if any(t.get('search_status')!='complete' for t in index['topics']):
        errors.append('unresolved search failure/incomplete response')
    if errors:
        print('\n'.join(errors),file=sys.stderr);return 1
    print(f"PASS: {len(index['topics'])} searched topics; {index['unique_candidates']} unique uncounted candidates; no overlap with catalog IDs.")
    return 0


if __name__=='__main__':raise SystemExit(main())
