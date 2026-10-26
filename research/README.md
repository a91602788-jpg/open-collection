# Поиск по темам / Topic discovery

[Catalog](../README.md) · [Quality standards](../QUALITY_STANDARDS.md) · [Topic index](topics.json)

**70 тем проверено поиском · 2,035 уникальных кандидатов · 1,158 записей в каталоге этой ветки.**

This is a discovery queue, not an extension of the curated count. Every candidate awaits editorial review, canonical-source checks and an original RU/EN description before catalog inclusion. Search metadata is not runtime testing or an endorsement. Counts reflect the current branch/commit.

Это очередь исследования, а не готовая подборка. Кандидаты не увеличивают основной счётчик. У ресурса одна запись по GitHub ID; совпадения по другим темам хранятся в `matched_topic_ids`. Отредактированные записи и исследовательские метаданные разделены.

## Как читать / How to read

1. Open the [compact topic index](topics.json), find a topic by its RU/EN title and fetch only its `data_path`.
2. `catalog` means the topic has a populated category in this branch; `proposed` means a research direction without a published category folder.
3. `candidate_count` counts IDs assigned to that topic once. A zero means no new unique candidates in this particular first batch, not that the topic has no projects.
4. Files include byte sizes and SHA-256 in the index. Keep the same branch/commit when resolving paths.

## Охват / Coverage

- 37 populated catalog categories and 33 proposed directions.
- One recorded query per topic, first 50 results sorted by stars: 3,500 observations before deduplication.
- Already-counted IDs, forks, archives and obvious leak/piracy names are excluded from the queue. Topic fit, ownership, trustworthiness and useful descriptions still need editorial review.
- Search terms and source URLs are retained per topic. This is an initial dated snapshot, not exhaustive discovery or a popularity-based recommendation.

## Следующие действия / Editorial next steps

Prioritize thin categories such as property, hospitality and sector-specific software, then compare candidates against their upstream documentation. Describe the actual task and resource class; keep missing license, deployment and pricing evidence explicit. Submit coherent catalog batches by topic with regenerated data, Markdown and AI navigation. Maintainer approval is required for merge.

The [quality decision record](quality-decisions.json) documents the new quality-category additions and excluded/previously-counted resources. Their edited catalog descriptions are in [section 37](../37-design-quality-and-engineering-standards/README.md).

## Проверки / Checks

`python3 scripts/check_research.py` checks queue uniqueness, separation from catalog IDs, topic coverage, file hashes and review status. It does not decide whether a candidate deserves inclusion. GitHub Actions runs it with the catalog and navigation checks.
