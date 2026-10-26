# Security

This repository publishes a directory, not the listed applications. Report a vulnerability in a listed project through that project’s own security policy; do not publish exploit details or private data in catalog issues.

For exposed credentials or a sensitive issue in this repository, use [GitHub private vulnerability reporting](https://github.com/a91602788-jpg/open-collection/security/advisories/new) if available. If it is unavailable, open a minimal issue requesting a private reporting channel without including sensitive details.

Workflows use read-only permissions, pinned action revisions and no application secrets. Catalog URLs are restricted to canonical public `github.com/owner/repo` addresses. External project code is never executed by catalog checks. Maintenance scripts authenticate only to `api.github.com` and do not follow authenticated requests to other hosts.
