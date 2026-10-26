# Contributing / Как участвовать

Предлагайте один проект через [Issue](https://github.com/a91602788-jpg/open-collection/issues/new/choose) или небольшой Pull Request. Русский и английский подходят. Предложение не означает автоматическое включение.

Suggest one repository in an issue or a focused pull request. Russian and English are welcome. Explain the task it helps solve, which category fits and whether you are affiliated with the project.

## Submission

- Canonical public GitHub URL; check existing records for duplicates and redirects.
- A short factual description, without unsupported performance or security claims.
- Original summaries in Russian and English for new or revised entries; say what it does and who can use it. Distinguish software from SDKs, specifications and datasets. Follow the description-editing section of EDITORIAL_POLICY.md.
- Current license file or an explicit missing/custom-license note.
- Primary-source evidence for any pricing, deployment or compatibility claim.
- No secrets, private data, affiliate links or copied README sections.

Maintainers edit [data/catalog.json](data/catalog.json) and the matching category README together. One repository gets one primary category and one count. Cross-reference it in guides when useful. Preserve stable IDs and use `metadata-checked` only after fetching public repository metadata. Do not mark anything runtime-tested without reproducible evidence and a separate schema/policy update.

## AI navigation / Навигация для AI

After editing the source catalog, regenerate its small navigation files with `python3 scripts/render_ai_navigation.py` in the authorized remote editing environment. Commit `llms.txt`, `SITEMAP.md`, `ai/index.json` and `data/categories/*.json` with the source change. These files are generated; edit the source or generator instead of updating their copies by hand. GitHub Actions checks their exact contents, category coverage and cache hashes with `python3 scripts/render_ai_navigation.py --check`. The [schema guide](data/SCHEMA.md) explains optional subcategories, detailed resource types and the schema 2 reference kind. Preserve the chosen branch/commit when resolving relative navigation links.

Для поиска проектов AI может читать [компактный индекс](ai/index.json) и один нужный раздел вместо полного экспорта. [Карта репозитория](SITEMAP.md) объясняет маршруты чтения. Поддержка такого режима зависит от используемого агента.

## Checks

The GitHub workflow runs `python3 scripts/check_catalog.py` and `python3 -m unittest discover -s scripts -p 'test_*.py'`. They check the catalog structure, duplicate IDs/names, URL format, license placeholders, category counts, Markdown coverage and local links. Run the manually dispatched “Repository links” workflow for read-only live checks. No dependencies need to be installed.

Small descriptive corrections are welcome. Larger restructures should explain the user-facing problem before changing the schema. Maintainers review all additions; no automatic merge is configured.

## Quality and discovery

Use [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md) for concrete, evidence-based review. Linters and repository popularity do not establish design quality, factual correctness or production readiness. The [quality guide](guides/design-quality-and-anti-slop.md) links to reference methods rather than imposing a single aesthetic.

The [topic index](research/topics.json) holds a separate, uncounted discovery queue. Raw candidate descriptions are attributed search metadata and need original RU/EN editing before inclusion. Candidates use one primary topic and cross-topic labels; stable IDs may not duplicate catalog IDs. When promoting one, remove it from the queue and update counts, byte sizes and SHA-256. `python3 scripts/check_research.py` checks separation, counts and hashes. New search snapshots need dated query URLs and explicit review status. Do not create empty catalog sections just to match the proposed topic map.
