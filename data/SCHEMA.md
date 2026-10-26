# Catalog schema / Схема каталога

`catalog.json` is the authoritative full export. Category JSON files are generated subsets; `ai/index.json` is a routing index and has its own schema version.

## Version 2 — v0.2

The existing fields remain available. This version adds the `reference` kind for specifications and datasets, detailed resource types, and declared subcategories. Consumers that enumerate kinds should handle `reference` before adopting schema 2. The validator accepts versions 1 and 2; the released v0.1 catalog uses version 1.

| Field | Contract |
| --- | --- |
| `id`, `repo`, `url` | Stable GitHub repository ID and canonical public name/URL; unique across the catalog. |
| `category` | An ID declared in the top-level `categories` array. |
| `subcategory` | Required when the category declares `subcategories`; otherwise omitted. Each subcategory declares its own entry count. |
| `kind` | Broad class: `starter`, `software`, `collection`, `learning`, or `reference`. |
| `resource_type` | Optional precise class: `application`, `library`, `sdk`, `toolkit`, `specification`, `dataset`, or `learning`. Older records may omit it. |
| `description` | Short English editorial summary or attributed legacy upstream text; at most 24 words. |
| `description_origin` | Identifies editorial text versus shortened upstream metadata. |
| `summary_ru`, `summary_en` | Original summaries, present together or both null. New and revised entries provide both. |
| `verification`, `checked_at` | Metadata-only evidence level and snapshot date; not a runtime or security certification. |
| `license_spdx` | GitHub-detected SPDX label or `CHECK-LICENSE`. |
| `pricing`, `deployment` | `not-reviewed` in the current contract. |
| `language`, `stack_status` | Primary GitHub language, not a complete stack. |
| `source` | Canonical primary-source repository link and discovery/editorial origin. |

Category shards preserve record IDs and fields from the full export. The AI index records exact byte sizes and SHA-256 hashes of those shards. Resolve `raw_url` against the URL from which the index was read; resolve `data_path` and `markdown_path` from the repository root at the same branch or commit.

Entry order is editorial navigation, not a quality score. Categories with subcategories group their Markdown entries under named headings. A repository may be linked from guides without being counted twice.
