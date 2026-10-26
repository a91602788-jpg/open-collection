# Quality standards / Стандарты качества

**Scope:** Public Open Collection repository, editorial submissions, and reviews of linked resources.  
**Область:** оформление каталога, отбор ссылок, качество описаний и обзор дизайн-ресурсов.

These are review criteria, **not** a ban on using AI or a universal prescription for colors, fonts and visual style. A human or AI-assisted contribution is acceptable if its claims are accurate, its value is specific, and a contributor takes responsibility for checking it.

Правила оценивают **результат и доказательства**, а не то, использовался ли ИИ. Каталог не разработчик перечисленных продуктов и не гарантирует их качество.

## 1. Mandatory catalog review / Обязательная проверка

A proposed index entry must satisfy **all** of these conditions:

1. **Real source / Первоисточник.** Canonical, publicly accessible upstream URL. For the current catalog schema: GitHub owner/repository plus stable GitHub repository ID. No speculative, shortened, referral, redirected-to-advertising or fabricated links.
2. **Distinct purpose / Конкретная польза.** Describe what the project does, for whom, and its type (application, starter, component, SDK, collection, standard, etc.). Do not confuse an SDK with a complete application, a demo with a finished product, or a booking calendar with hotel property management.
3. **Evidence boundaries / Границы проверки.** `metadata-checked` means public repository metadata was read, **not** runtime-tested, production-ready, secure, legally reviewed, compliant, or free to use commercially. Pricing, capabilities and technical performance need primary-source evidence and dates.
4. **Ownership and licensing / Права.** Link to the original author, check known license signals, explicitly label unknown terms. No copying README chapters, marketing graphics, screenshots, fonts or source trees into this index without applicable permission. This repository's CC0 dedication does not relicense upstream materials.
5. **No duplication / Без дублей.** One authoritative primary entry per stable repository ID; other guides can cross-link it. New categories must follow the data schema and regenerate derived navigation.
6. **Trust and safety / Безопасность.** No phishing, malware, leaked credentials, unauthorized/pirated content, disguised tracking, affiliate spam or deliberately deceptive listings.

## 2. No AI slop in descriptions / Без шаблонного текста

Reject or rewrite:

- Empty praise: “revolutionary”, “game-changing”, “ultimate”, “seamless experience”, “best ever”, “AI-powered solution for everything” without a specific verified function.
- Invented numbers, launch dates, testimonials, user counts, screenshots, quotes, audit claims, certifications, rankings or comparisons.
- A chain of stock slogans and repetitive section headings that adds no useful facts.
- Descriptions copied wholesale from an upstream README, or AI-generated summaries not checked against the primary source.
- Ambiguous statements that confuse community projects, commercial vendors, source mirrors, educational demos or source-available products with permissively licensed software.

**Use instead:** a short factual summary naming the task solved, the form of the resource and a relevant limitation or dependency when known. Write naturally in RU/EN where the schema provides original summaries. If it cannot be substantiated, leave the attribute `not-reviewed` or use the designated unknown license marker instead of guessing.

## 3. Design quality / Дизайн без шаблонности

When reviewing **design-related examples**, require purposeful decisions rather than a category stereotype:

| Area | What a credible review considers |
| --- | --- |
| Purpose & audience | Real user tasks, product identity, information architecture and intended visual direction |
| Composition | Clear hierarchy, readable scanning order, appropriate density and varied layouts where content requires them |
| Typography | Legibility, deliberate hierarchy, spacing, line length and fonts suitable for the audience |
| Color & imagery | Distinguishable states, meaningful contrast, traceable licenses and images connected to real content |
| Interaction | Clickable controls with real behaviors; coherent forms, validation, feedback, empty/loading/error/success states |
| Accessibility | Keyboard support, visible focus, labels, text alternatives, reduced motion and applicable WCAG criteria |
| Responsiveness | Real small/large viewport behavior without overflow, hidden functionality or unreadable controls |
| Motion & performance | Animation supports comprehension and respects preferences; not a decorative burden or accessibility obstacle |
| Content authenticity | No fake metrics, fabricated customers, imaginary integrations, misleading mock data or screenshots presented as production |
| Engineering | Appropriate semantics, component reuse where justified, maintainability and tested behavior when the claim is made |

Repeated gradient heroes, glass panels, identical rounded-card grids, stock blobs, dark glows, center-everything layouts and generic dashboard shells are **warning signs only when chosen without an explicit product reason**. Do **not** ban specific fonts, gradients, corners, CSS libraries or AI use categorically. A visually plain tool can be excellent; an attractive demo can be unusable.

A listed project is **not** a design endorsement. Deeper “design-reviewed” or “tested” claims require a separate defined evidence process; do not invent verification states in the current JSON schema.

## 4. GitHub presentation / Оформление самого репозитория

- Keep README as a useful, bilingual entry point with short sections and direct links to topical files; do not turn it into a huge wall of 10,000 links.
- Prefer readable Markdown, descriptive link text, consistent headings, working relative links and compact navigation.
- Avoid decorative ASCII logos, meaningless shields, misleading star badges, emoji-filled headings, gratuitous animations, massive banners and stock illustrations.
- Use factual counts **only when derived from the checked catalog**. Avoid “#1”, “the world's largest”, “official partner” or false endorsement claims.
- Do not add a separate website, backend, database or hosting requirement just to achieve a decorative layout.
- Respect attribution, privacy, readable mobile layouts and localization.

## 5. Review outcomes / Итог проверки

| Result | Apply when |
| --- | --- |
| **BLOCK / FAIL** | Malicious/deceptive or unauthorized material, fabricated source, secret leakage, affiliate manipulation, or a substantive uncorrected false claim |
| **REVISE / CONDITIONAL** | Useful entry, but inaccurate wording, missing evidence, unclear license, duplicate location, inaccessible navigation or unsupported claims remain |
| **ACCEPT (metadata only)** | Catalog format, canonical source and editorial requirements pass; no claim about runtime safety, UI quality or commercial clearance |

These are **editorial decisions**, not CI verdicts. Automated checks may catch formatting and duplicate URLs but cannot reliably decide whether a design has purpose or whether prose is truthful. Human review is required.

## 6. Useful references / Источники

- [Design quality and anti-slop reference repos](guides/design-quality-and-anti-slop.md) — researched links for interface craft, content and code review.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — normative accessibility criteria for applicable web products.
- [GitHub content design principles](https://docs.github.com/en/contributing/writing-for-github-docs/content-design-principles) — user-centered, clear and evidence-driven documentation.
- [Editorial policy](EDITORIAL_POLICY.md) and [Contribution guide](CONTRIBUTING.md) — existing catalog schema, rights and submission workflow.

**Status:** proposed review standards; publication to main and any enforcement changes require maintainer approval. None of the linked third-party programs was installed or audited for this document.
