import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from urllib.parse import urljoin

from render_ai_navigation import encode_json, generate, generated_errors


class ProgressiveReadingContracts(unittest.TestCase):
    def setUp(self):
        self.catalog = {
            'schema_version': 1, 'checked_at': '2026-10-27',
            'repository': 'https://github.com/a91602788-jpg/open-collection',
            'verification': 'Metadata only.',
            'categories': [
                {'id': '08-crm-and-sales', 'title_ru': 'CRM и продажи', 'title_en': 'CRM & sales', 'count': 1},
                {'id': '09-erp-and-enterprise', 'title_ru': 'ERP', 'title_en': 'ERP', 'count': 1},
            ],
            'entries': [
                {'id': 1, 'repo': 'example/crm', 'category': '08-crm-and-sales'},
                {'id': 2, 'repo': 'example/erp', 'category': '09-erp-and-enterprise'},
            ],
        }

    def test_lookup_index_contains_no_full_project_records(self):
        result = generate(encode_json(self.catalog))
        index = json.loads(result['ai/index.json'])
        self.assertEqual(index['total_entries'], 2)
        self.assertNotIn('example/crm', result['ai/index.json'].decode())
        self.assertNotIn('example/erp', result['llms.txt'].decode())

    def test_shard_contains_only_its_category_and_hash_matches_file(self):
        result = generate(encode_json(self.catalog))
        index = json.loads(result['ai/index.json'])
        for category in index['categories']:
            content = result[category['data_path']]
            shard = json.loads(content)
            self.assertEqual([e['category'] for e in shard['entries']], [category['id']])
            self.assertEqual(category['bytes'], len(content))
            self.assertEqual(category['sha256'], hashlib.sha256(content).hexdigest())

    def test_unrelated_category_update_keeps_cached_shard_valid(self):
        before = generate(encode_json(self.catalog))
        self.catalog['entries'][1]['repo'] = 'example/erp-renamed'
        after = generate(encode_json(self.catalog))
        path = 'data/categories/08-crm-and-sales.json'
        self.assertEqual(before[path], after[path])
        self.assertNotEqual(before['ai/index.json'], after['ai/index.json'])

    def test_category_links_stay_on_the_readers_branch(self):
        result = generate(encode_json(self.catalog))
        category = json.loads(result['ai/index.json'])['categories'][0]
        base = 'https://raw.githubusercontent.com/a91602788-jpg/open-collection/catalog/v0.2-expanded-domains/'
        resolved = urljoin(base+'ai/index.json', category['raw_url'])
        self.assertEqual(resolved, base+category['data_path'])

    def test_missing_stale_and_removed_category_files_are_detected(self):
        result = generate(encode_json(self.catalog))
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertTrue(generated_errors(root, result))
            for path, content in result.items():
                file = root/path
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_bytes(content)
            self.assertEqual(generated_errors(root, result), [])
            (root/'ai/index.json').write_text('{}')
            (root/'data/categories/removed-category.json').write_text('{}')
            errors = generated_errors(root, result)
            self.assertTrue(any('stale' in e for e in errors))
            self.assertTrue(any('unexpected' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
