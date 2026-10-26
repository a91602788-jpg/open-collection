import copy
import unittest
from check_catalog import catalog_errors, entry_errors


class CatalogContracts(unittest.TestCase):
    def setUp(self):
        self.entry = {
            'id': 1, 'repo': 'example/project', 'url': 'https://github.com/example/project',
            'category': '01-tools', 'kind': 'software', 'archived': False, 'fork': False,
            'verification': 'metadata-checked', 'license_spdx': 'CHECK-LICENSE',
            'license_url': 'https://github.com/example/project', 'description': 'A useful tool.',
            'pricing': 'not-reviewed', 'deployment': 'not-reviewed',
            'stack_status': 'primary-language-only', 'summary_ru': None, 'summary_en': None,
            'checked_at': '2026-10-27', 'pushed_at': '2026-10-26T00:00:00Z',
            'source': {'url': 'https://github.com/example/project'},
        }
        self.data = {'schema_version': 1, 'checked_at': '2026-10-27',
                     'categories': [{'id': '01-tools', 'count': 1}], 'entries': [self.entry]}

    def test_missing_license_is_explicit_and_acceptable(self):
        self.assertEqual(catalog_errors(self.data), [])
        self.entry['license_spdx'] = ''
        self.assertTrue(entry_errors(self.entry, {'01-tools'}))

    def test_duplicate_ids_survive_name_change(self):
        other = copy.deepcopy(self.entry)
        other.update(repo='example/renamed', url='https://github.com/example/renamed')
        self.data['entries'].append(other)
        self.assertTrue(any('duplicate repository ID' in e for e in catalog_errors(self.data)))

    def test_names_are_case_insensitive(self):
        other = copy.deepcopy(self.entry)
        other.update(id=2, repo='Example/Project')
        self.data['entries'].append(other)
        self.assertTrue(any('duplicate repository name' in e for e in catalog_errors(self.data)))

    def test_external_and_credential_urls_are_rejected(self):
        for url in ('https://github.com.evil.test/example/project',
                    'https://user:secret@github.com/example/project',
                    'http://github.com/example/project'):
            self.entry['url'] = url
            self.assertTrue(entry_errors(self.entry, {'01-tools'}))

    def test_archives_and_unsupported_assurance_fail(self):
        self.entry.update(archived=True, verification='production-ready')
        self.assertGreaterEqual(len(entry_errors(self.entry, {'01-tools'})), 2)

    def test_category_count_and_date_must_match(self):
        self.data['categories'][0]['count'] = 2
        self.entry['checked_at'] = '2026-10-26'
        self.assertGreaterEqual(len(catalog_errors(self.data)), 2)


if __name__ == '__main__':
    unittest.main()
