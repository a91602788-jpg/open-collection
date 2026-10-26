# Editorial policy / Правила отбора

## Scope

Apply the [quality standards](QUALITY_STANDARDS.md) to new entries and revisions. The [discovery queue](research/README.md) holds uncounted candidates; search-result metadata is not editorial acceptance. Proposed research topics do not become catalog categories until populated and reviewed.


Useful public GitHub repositories for building, operating, learning and creating: starters, libraries, applications, tools and resource collections. CRM and ERP have separate lanes; HR and inventory tools may be grouped under enterprise software without being labeled complete ERPs.

## Evidence levels

- `metadata-checked`: a public canonical repository was resolved through GitHub API; description, primary language, license detection, fork/archive flags and push timestamp were captured.
- Runtime tests, security reviews and legal assessments are **not** implied. The launch catalog contains no `tested` or `production-ready` claims.

The first release combines selected known entry points with topic/name-based GitHub discovery. Category fit is screened using names, descriptions and topics; it is not a comparative product review. GitHub topics are author-supplied and can be imperfect. Stars guide discovery, not trust or quality ranking. Discovery queries are recorded in [data/discovery.json](data/discovery.json).

## Inclusion and deduplication

Use the canonical GitHub repository and stable numeric ID. No duplicate IDs or case-insensitive names, forks or repositories archived at the snapshot date. Do not include piracy, leaked proprietary materials, empty showcases, affiliate dumps or unrelated keyword matches. A project may appear in several task-guide links but has only one primary catalog entry and is counted once.

Descriptions are either original short RU/EN summaries or clearly attributed upstream GitHub metadata, truncated to 24 words. Upstream descriptions remain the authors’ claims, not independent verification. Repository source code, screenshots and entire READMEs are not mirrored.

## Description editing / Редактура описаний

New entries and description revisions receive original Russian and English summaries. Describe the resource's function and use case in complete sentences. Remove superlatives, emoji advertising, vague promises and truncated fragments. Identify whether the resource is an application, library, SDK, specification, dataset, learning material or tool. A booking tool is not automatically a hotel PMS; a medical data specification is not a clinical application; a GitHub issue tracker is not automatically the project's current source repository.

Use primary-source evidence for each substantive statement. Metadata-only checks remain metadata-only after rewriting a description. Do not repeat unsupported compliance, accuracy, performance, pricing or production-readiness claims. Note material boundaries such as source mirrors, development branches and version-dependent terms.

The v0.2 update adds 120 original bilingual summaries. Older entries without original summaries retain their clearly attributed upstream text until revised; this release does not claim that every earlier description has been edited.

## Data boundaries

`CHECK-LICENSE` means GitHub did not supply a recognized SPDX identifier. Other labels are GitHub detections, not proof that every module, asset or dependency uses those terms. License links open the original repository so readers can inspect current files. Nonstandard/source-available projects are allowed without claiming the whole collection is open source.

Pricing and deployment are `not-reviewed` unless evidence is added in a future reviewed record. Primary language is not a full technology stack. All entries use snapshot dates rather than unsupported “actively maintained” badges.

## Updates

Pull requests require human review. Catalog checks validate data and local links. A weekly read-only GitHub API check reports removals, redirects and archival changes in Actions; it does not silently rewrite records or merge changes. GitHub can disable scheduled workflows in inactive public repositories; run the workflow manually if necessary. No autonomous growth or guaranteed update frequency is promised.

Report errors through Issues with primary-source links. Remove or amend misleading entries. Sponsored placement is not part of this release; any future sponsorship must be disclosed and must not replace editorial criteria.
