# Maintainer guide

## Working model

The main branch is the published collection. Proposed changes should arrive as pull requests. Run `python3 scripts/validate_catalog.py` locally before opening a PR. The validation workflow has read-only repository permissions and cannot publish changes.

## Adding a topic

A topic requires (1) a Markdown file under `catalog/`, (2) a matching entry in both README files, and (3) an update to `EXPECTED_CATEGORIES` in `scripts/validate_catalog.py`. Avoid adding empty categories. Do not change established paths casually; existing links may depend on them.

## Review checklist

- Link leads to the intended upstream project; avoid trackers or unofficial mirrors.
- Brief description is accurate and written in our own words.
- No other entry uses the same URL; related categories can link to the primary listing via relative links.
- No unsupported license, price, safety or maintenance claims.
- No copied software, images, fonts, logos or large third-party text.
- No changes to workflows, security policy or license without explicit owner review.

## Validation boundaries

`validate_catalog.py` checks formatting, category coverage and duplicate URLs. It does not contact external networks and cannot validate GitHub project ownership, license or functionality. CI success does not imply a security audit. Check documentation and license at upstream before recommending a resource for production.
