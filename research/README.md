# Поиск по темам / Topic discovery

[Catalog](../README.md) · [Quality standards](../QUALITY_STANDARDS.md) · [Topic index](topics.json)

**76 тем проверено поиском · 1,922 уникальных кандидатов · 1,307 записей в каталоге этой ветки.**

This is a discovery queue, not an extension of the curated count. Every candidate awaits editorial review, canonical-source checks and an original RU/EN description before catalog inclusion. Search metadata is not runtime testing or an endorsement. Counts reflect the current branch/commit.

Это очередь исследования, а не готовая подборка. Кандидаты не увеличивают основной счётчик. У ресурса одна запись по GitHub ID; совпадения по другим темам хранятся в `matched_topic_ids`. Отредактированные записи и исследовательские метаданные разделены.

## Как читать / How to read

1. Open the [compact topic index](topics.json), find a topic by its RU/EN title and fetch only its `data_path`.
2. `catalog` means the topic has a populated category in this branch; `proposed` means a research direction without a published category folder.
3. `candidate_count` counts IDs assigned to that topic once. A zero means no new unique candidates in this particular first batch, not that the topic has no projects.
4. Files include byte sizes and SHA-256 in the index. Keep the same branch/commit when resolving paths.

## Охват / Coverage

- 63 populated catalog categories and 13 proposed research directions.
- Initial snapshot: one query per topic, first 50 results sorted by stars, 3,500 observations before deduplication. The 2026-10-28 follow-up adds 17 targeted repository lookups; it does not rerun all 70 topic searches.
- Six further directions were researched on 2026-10-28 through 32 bounded retrievals (484 returned rows before cross-query deduplication), yielding 26 unseen candidates. Their queries and observed IDs are recorded in the new topic files; this does not rerun the earlier 70-topic snapshot.
- Already-counted IDs, forks, archives and obvious leak/piracy names are excluded from the queue. Topic fit, ownership, trustworthiness and useful descriptions still need editorial review.
- Search terms and source URLs are retained per topic. This is an initial dated snapshot, not exhaustive discovery or a popularity-based recommendation.

## Первая редакционная партия / First editorial batch

[Review record](review-batches/2026-10-27-batch-01.json): 149 edited records proposed for inclusion; 7 removed from the active queue; 42 assigned to more appropriate topics. One agriculture resource remains for a later sector batch. These are proposed editorial decisions, subject to maintainer review. Remaining candidates have not all been reviewed.

The first shortlist refreshed metadata and README evidence for 153 sources. Three apparently available repositories were not promoted because their own READMEs announce deprecation or stopped maintenance. Four other items were excluded by editorial scope. Broad OR queries also confused state management with property management and high-resolution neural networks with HR; the batch records those corrections.

`discovery_sources` preserves the original query, topic and source URL for every remaining candidate. `primary_topic_id` and `matched_topic_ids` may include editorial reassignment; they no longer imply that a candidate was originally found under its current file's query. Moving a candidate never creates a second ID or erases its discovery history.

## Поисковая партия 2026-10-28 / Follow-up discovery

[Readable report](review-batches/2026-10-28-follow-up.md) · [Review data](review-batches/2026-10-28-follow-up.json): 17 new pending candidates and six existing-candidate reviews. The active queue grows from 1,879 to 1,896; no catalog entries or categories are added by this follow-up. Two primary-topic corrections and one stale cross-topic label cleanup retain the original discovery sources. All 23 reviewed resources still await catalog acceptance. Pricing, deployment, runtime behavior and security remain unreviewed.

## Отраслевая партия 2026-10-28 / Sector discovery

[Readable report](review-batches/2026-10-28-sector-discovery.md) · [Review data](review-batches/2026-10-28-sector-discovery.json): 26 new pending candidates populate six proposed topics: space, maritime navigation, audio production, photography, physical security and animal-care software. The active queue grows from 1,896 to 1,922 and the research map from 70 to 76 topics. Catalog entries and published categories remain unchanged. This is metadata/README review, not runtime testing or approval for operational use.

## Следующие действия / Editorial next steps

Prioritize thin categories such as property, hospitality and sector-specific software, then compare candidates against their upstream documentation. Describe the actual task and resource class; keep missing license, deployment and pricing evidence explicit. Submit coherent catalog batches by topic with regenerated data, Markdown and AI navigation. Maintainer approval is required for merge.

The [quality decision record](quality-decisions.json) documents the new quality-category additions and excluded/previously-counted resources. Their edited catalog descriptions are in [section 37](../37-design-quality-and-engineering-standards/README.md).

## Проверки / Checks

`python3 scripts/check_research.py` checks queue uniqueness, separation from catalog IDs, topic coverage, file hashes and review status. It does not decide whether a candidate deserves inclusion. GitHub Actions runs it with the catalog and navigation checks.
