# Contributing / Как участвовать

Предлагайте один проект через [Issue](https://github.com/a91602788-jpg/open-collection/issues/new/choose) или небольшой Pull Request. Русский и английский подходят. Предложение не означает автоматическое включение.

Suggest one repository in an issue or a focused pull request. Russian and English are welcome. Explain the task it helps solve, which category fits and whether you are affiliated with the project.

## Submission

- Canonical public GitHub URL; check existing records for duplicates and redirects.
- A short factual description, without unsupported performance or security claims.
- Current license file or an explicit missing/custom-license note.
- Primary-source evidence for any pricing, deployment or compatibility claim.
- No secrets, private data, affiliate links or copied README sections.

Maintainers edit [data/catalog.json](data/catalog.json) and the matching category README together. One repository gets one primary category and one count. Cross-reference it in guides when useful. Preserve stable IDs and use `metadata-checked` only after fetching public repository metadata. Do not mark anything runtime-tested without reproducible evidence and a separate schema/policy update.

## Checks

The GitHub workflow runs `python3 scripts/check_catalog.py` and `python3 -m unittest discover -s scripts -p 'test_*.py'`. They check the catalog structure, duplicate IDs/names, URL format, license placeholders, category counts, Markdown coverage and local links. Run the manually dispatched “Repository links” workflow for read-only live checks. No dependencies need to be installed.

Small descriptive corrections are welcome. Larger restructures should explain the user-facing problem before changing the schema. Maintainers review all additions; no automatic merge is configured.
