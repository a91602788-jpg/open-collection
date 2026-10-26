# Карта репозитория / Repository sitemap

[Каталог / Catalog](README.md) · [AI entry point](llms.txt) · [Machine index](ai/index.json)

## Короткий маршрут / Minimal reading route

1. Откройте `llms.txt` или `ai/index.json`. / Read the AI entry point or compact index.
2. Выберите раздел по задаче. / Pick the category that matches the task.
3. Прочитайте только его JSON **или** Markdown. / Read only its JSON **or** Markdown.
4. Для подробностей откройте первоисточники выбранных проектов. / Follow selected projects' original URLs for detail.

Для вопроса про CRM достаточно индекса и `08-crm-and-sales`: раздел ERP нужен, только если задача включает корпоративные процессы. Для сравнения SaaS-основ начните с `01-saas-and-starters`; добавляйте UI или backend по необходимости. Полный обзор всех направлений требует полного каталога — карта не заменяет его содержимое.

For a CRM question, load the index and the CRM shard. Add ERP only if enterprise processes matter. For SaaS starters, start with the starters shard and add UI/backend as needed. An exhaustive cross-category task may require the full catalog.

## Файлы и назначение / Files and purpose

| File | When to read |
| --- | --- |
| [llms.txt](llms.txt) | Small AI entry point and raw-content links. |
| [ai/index.json](ai/index.json) | Route a task; check counts, sizes and SHA-256 before reading a category. |
| [guides/start-here.md](guides/start-here.md) | Find selected starting points by practical task. |
| [guides/choosing-a-project.md](guides/choosing-a-project.md) | Evaluate scope, licenses, costs and maintenance. |
| [AGENTS.md](AGENTS.md) | Instructions for changing the collection. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Submit a change and regenerate navigation. |
| [EDITORIAL_POLICY.md](EDITORIAL_POLICY.md) | Understand evidence levels and inclusion policy. |
| [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md) | Apply editorial quality gates without treating linters as product certification. |
| [guides/design-quality-and-anti-slop.md](guides/design-quality-and-anti-slop.md) | Follow references across design, writing and engineering. |
| [research/topics.json](research/topics.json) | Explore a topic's uncounted discovery candidates; read only for research tasks. |
| [research/README.md](research/README.md) | Understand search coverage, exclusions and pending review. |
| [SOURCES.md](SOURCES.md) | Understand source attribution. |
| [VALIDATION.md](VALIDATION.md) | Launch-check evidence; current results are in Actions. |
| [data/catalog.json](data/catalog.json) | Full export and authoritative editing source; exhaustive tasks. |
| [data/discovery.json](data/discovery.json) | Audit discovery queries; not needed for ordinary project lookup. |

## Разделы / Categories

Both views represent the same records; select one format rather than fetching both.

| № | Раздел / Category | Records | Readable | JSON shard |
| --- | --- | ---: | --- | --- |
| 01 | SaaS и готовые основы / SaaS & starters | 60 | [Markdown](01-saas-and-starters/README.md) | [JSON](data/categories/01-saas-and-starters.json) |
| 02 | Дизайн, иконки и шрифты / Design & creative | 40 | [Markdown](02-design-and-creative/README.md) | [JSON](data/categories/02-design-and-creative.json) |
| 03 | Веб-разработка и готовые сайты / Web development | 50 | [Markdown](03-web-development/README.md) | [JSON](data/categories/03-web-development.json) |
| 04 | Компоненты веб-интерфейсов / Web components | 70 | [Markdown](04-web-components/README.md) | [JSON](data/categories/04-web-components.json) |
| 05 | Мобильные приложения / Mobile applications | 45 | [Markdown](05-mobile-applications/README.md) | [JSON](data/categories/05-mobile-applications.json) |
| 06 | AI, агенты, MCP и RAG / AI & machine learning | 80 | [Markdown](06-artificial-intelligence/README.md) | [JSON](data/categories/06-artificial-intelligence.json) |
| 07 | Базы данных и хранилища / Databases & storage | 50 | [Markdown](07-databases-and-storage/README.md) | [JSON](data/categories/07-databases-and-storage.json) |
| 08 | CRM и продажи / CRM & sales | 25 | [Markdown](08-crm-and-sales/README.md) | [JSON](data/categories/08-crm-and-sales.json) |
| 09 | ERP и корпоративные системы / ERP & enterprise | 20 | [Markdown](09-erp-and-enterprise/README.md) | [JSON](data/categories/09-erp-and-enterprise.json) |
| 10 | Финансы и платежи / Finance & payments | 25 | [Markdown](10-finance-and-payments/README.md) | [JSON](data/categories/10-finance-and-payments.json) |
| 11 | Интернет-магазины и торговля / E-commerce | 35 | [Markdown](11-ecommerce/README.md) | [JSON](data/categories/11-ecommerce.json) |
| 12 | Self-hosted и собственные сервисы / Self-hosted services | 50 | [Markdown](12-self-hosted/README.md) | [JSON](data/categories/12-self-hosted.json) |
| 13 | DevOps, облака и мониторинг / DevOps & cloud | 60 | [Markdown](13-devops-and-cloud/README.md) | [JSON](data/categories/13-devops-and-cloud.json) |
| 14 | Безопасность, IAM и приватность / Cybersecurity & identity | 45 | [Markdown](14-cybersecurity/README.md) | [JSON](data/categories/14-cybersecurity.json) |
| 15 | API, SDK и интеграции / APIs, SDKs & integrations | 30 | [Markdown](15-apis-and-sdks/README.md) | [JSON](data/categories/15-apis-and-sdks.json) |
| 16 | Автоматизация и no-code / Automation & no-code | 30 | [Markdown](16-automation-and-nocode/README.md) | [JSON](data/categories/16-automation-and-nocode.json) |
| 17 | Данные, BI и аналитика / Data & analytics | 35 | [Markdown](17-data-and-analytics/README.md) | [JSON](data/categories/17-data-and-analytics.json) |
| 18 | Контент, CMS и маркетинг / Content & marketing | 30 | [Markdown](18-content-and-marketing/README.md) | [JSON](data/categories/18-content-and-marketing.json) |
| 19 | Совместная работа и знания / Collaboration & knowledge | 30 | [Markdown](19-collaboration/README.md) | [JSON](data/categories/19-collaboration.json) |
| 20 | Настольные приложения и утилиты / Desktop & utilities | 35 | [Markdown](20-desktop-and-utilities/README.md) | [JSON](data/categories/20-desktop-and-utilities.json) |
| 21 | Устройства, IoT и умный дом / Hardware & IoT | 25 | [Markdown](21-hardware-and-iot/README.md) | [JSON](data/categories/21-hardware-and-iot.json) |
| 22 | Игры, звук и видео / Gaming & media | 30 | [Markdown](22-gaming-and-media/README.md) | [JSON](data/categories/22-gaming-and-media.json) |
| 23 | Обучение, практика и исследования / Learning & research | 50 | [Markdown](23-learning-and-research/README.md) | [JSON](data/categories/23-learning-and-research.json) |
| 24 | Каталоги и тематические коллекции / Awesome & collections | 50 | [Markdown](24-awesome-collections/README.md) | [JSON](data/categories/24-awesome-collections.json) |
| 25 | Связь и realtime / Communications & realtime | 12 | [Markdown](25-communications-and-realtime/README.md) | [JSON](data/categories/25-communications-and-realtime.json) |
| 26 | Карты и геопространственные данные / Maps & geospatial | 12 | [Markdown](26-maps-and-geospatial/README.md) | [JSON](data/categories/26-maps-and-geospatial.json) |
| 27 | Логистика и транспорт / Logistics & transportation | 10 | [Markdown](27-logistics-and-transportation/README.md) | [JSON](data/categories/27-logistics-and-transportation.json) |
| 28 | Недвижимость и управление объектами / Real estate & property | 4 | [Markdown](28-real-estate-and-property/README.md) | [JSON](data/categories/28-real-estate-and-property.json) |
| 29 | Туризм, бронирование и рестораны / Travel & hospitality | 6 | [Markdown](29-travel-and-hospitality/README.md) | [JSON](data/categories/29-travel-and-hospitality.json) |
| 30 | Документы и legal tech / Documents & legal tech | 12 | [Markdown](30-documents-and-legal-tech/README.md) | [JSON](data/categories/30-documents-and-legal-tech.json) |
| 31 | Медицина и медицинские данные / Healthcare & medical | 10 | [Markdown](31-healthcare-and-medical/README.md) | [JSON](data/categories/31-healthcare-and-medical.json) |
| 32 | Образовательные платформы и LMS / Education & LMS | 10 | [Markdown](32-education-and-lms/README.md) | [JSON](data/categories/32-education-and-lms.json) |
| 33 | Доступность и локализация / Accessibility & localization | 12 | [Markdown](33-accessibility-and-localization/README.md) | [JSON](data/categories/33-accessibility-and-localization.json) |
| 34 | Наука и инженерия / Science & engineering | 12 | [Markdown](34-science-and-engineering/README.md) | [JSON](data/categories/34-science-and-engineering.json) |
| 35 | Открытые данные и civic tech / Open data & civic tech | 10 | [Markdown](35-open-data-and-civic-tech/README.md) | [JSON](data/categories/35-open-data-and-civic-tech.json) |
| 36 | Поиск и базы знаний / Search & knowledge | 10 | [Markdown](36-search-and-knowledge/README.md) | [JSON](data/categories/36-search-and-knowledge.json) |
| 37 | Качество дизайна, anti-slop и инженерные стандарты / Design Quality, Anti-AI-Slop & Engineering Standards | 38 | [Markdown](37-design-quality-and-engineering-standards/README.md) | [JSON](data/categories/37-design-quality-and-engineering-standards.json) |

## Повторное чтение / Repeat visits

The index provides SHA-256 hashes of exact category file bytes. If your client supports caching, reuse unchanged shards. If a fetched file does not match the index hash, refresh the index and retry; concurrent updates can occur. For a consistent historical snapshot, request files at a single Git commit. Cache availability depends on the agent/client; this repository does not create persistent memory for it.

## Сопровождение / Maintenance

`data/catalog.json` is the source of truth. `llms.txt`, this map, `ai/index.json` and `data/categories/*.json` are generated by [scripts/render_ai_navigation.py](scripts/render_ai_navigation.py). GitHub Actions checks exact agreement and rejects stale generated files. See [CONTRIBUTING.md](CONTRIBUTING.md).

This is a repository navigation map, not a website crawler configuration. GitHub controls its own robots and HTTP headers. Publishing these files helps agents that discover and follow them; it cannot compel every AI crawler to use them. The entry-point format follows the [llms.txt proposal](https://llmstxt.org/).
