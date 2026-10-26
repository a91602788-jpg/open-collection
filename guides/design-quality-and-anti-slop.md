# Design quality, anti-slop and craft / Дизайн и стандарты качества

[Home / Главная](../README.md) · [Quality standards / Стандарты](../QUALITY_STANDARDS.md) · [Editorial policy](../EDITORIAL_POLICY.md)

**Cross-category reference guide.** Selected sources are now indexed once in [section 37](../37-design-quality-and-engineering-standards/README.md). Existing accessibility tools remain in [section 33](../33-accessibility-and-localization/README.md). This guide adds no separate counted entries.

**Навигационная подборка, без повторного учёта.** Раздел качества охватывает приложения, типографику, UX, тексты, архитектуру и инженерные практики. Включение означает проверку сведений о репозитории и редактуру описания, а не запуск инструмента или подтверждение качества продукта.

## 1. Anti-slop and intentional design / Против шаблонного AI-дизайна

| Repository | Why inspect it / Для чего |
| --- | --- |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Design critique methods and practical patterns for improving AI-assisted interfaces. |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Art direction, references and browser review instead of generic layout defaults. |
| [muris11/anti-ai-slop](https://github.com/muris11/anti-ai-slop) | An evolving taxonomy covering layout, content, visual signals and code-level issues. |
| [waddle36/anti-ai-slop](https://github.com/waddle36/anti-ai-slop) | Combined reference for repetitive visual and written AI-output patterns. |
| [sboghossian/design-skill](https://github.com/sboghossian/design-skill) | Workflow for direction, critique, responsive checks and browser validation. |
| [infernaldudd/anti-ai-slop-ui](https://github.com/infernaldudd/anti-ai-slop-ui) | Agent-oriented guidelines for hierarchy, interaction states and honest product UI. |
| [ZeroZ-lab/cc-design](https://github.com/ZeroZ-lab/cc-design) | Design and content-guideline examples, including anti-patterns. |

**Read critically:** these are mostly third-party opinionated toolkits, not formal standards. No AI detector proves authorship or aesthetic quality. Some source licenses were not automatically recognized; check the upstream LICENSE/NOTICE before reuse.

## 2. Design systems, references and creative assets / Дизайн-системы и референсы

| Repository | Why inspect it / Для чего |
| --- | --- |
| [alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems) | Design-system directories with UI patterns and documentation references. |
| [dalisoft/awesome-ui-libraries](https://github.com/dalisoft/awesome-ui-libraries) | Curated libraries, templates and inspiration collections. |
| [reinaldosimoes/design-resources](https://github.com/reinaldosimoes/design-resources) | Human-reviewed design resources; inspect each downstream asset's terms separately. |
| [brandonhimpfen/awesome-web-design](https://github.com/brandonhimpfen/awesome-web-design) | Typography, layout, UX, color and web-design learning references. |
| [primer/react](https://github.com/primer/react) | React implementation of GitHub's Primer component system. |
| [design-tokens/community-group](https://github.com/design-tokens/community-group) | Open specification work and reference material for design tokens. |
| [storybookjs/storybook](https://github.com/storybookjs/storybook) | Component examples, documentation and testing in isolation. |

A screenshot or high star count is **not** evidence of usability or rights to reuse graphics and fonts.

## 3. Accessibility, UX and functional quality / Доступность и UX

| Repository | Why inspect it / Для чего |
| --- | --- |
| [w3c/aria-practices](https://github.com/w3c/aria-practices) | Official APG authoring patterns and keyboard-interaction examples. |
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | Programmatic web accessibility auditing engine. |
| [pa11y/pa11y](https://github.com/pa11y/pa11y) | Command-line accessibility testing tools. |
| [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | Web performance and best-practice audits. |
| [thedaviddias/Front-End-Checklist](https://github.com/thedaviddias/Front-End-Checklist) | Broad front-end implementation and launch checklist. |

Tests and linters support human accessibility testing; an automated pass is not proof of complete WCAG conformance. See [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/).

## 4. Writing, README and documentation / Тексты и документация

| Repository | Why inspect it / Для чего |
| --- | --- |
| [github/docs](https://github.com/github/docs) | Example of structured public product documentation and contribution workflow. |
| [blader/humanizer](https://github.com/blader/humanizer) | Editorial guidance on replacing formulaic AI-written prose with concrete writing. |
| [DavidAnson/markdownlint](https://github.com/DavidAnson/markdownlint) | Reproducible Markdown linting for consistency and readability. |
| [google/styleguide](https://github.com/google/styleguide) | Language-specific code style guidance to review when appropriate. |
| [airbnb/javascript](https://github.com/airbnb/javascript) | JavaScript style-guide reference, not a universal requirement. |

Editing AI-assisted text is not license to fabricate authorship, endorsements or facts. A good description names concrete capabilities and limitations instead of promising everything.

## 5. Engineering, safety and maintainability / Инженерное качество

| Repository | Why inspect it / Для чего |
| --- | --- |
| [stylelint/stylelint](https://github.com/stylelint/stylelint) | CSS linting and conventional code-style consistency. |
| [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) | Security implementation guidance across common application concerns. |
| [ossf/scorecard](https://github.com/ossf/scorecard) | Source-health signals for open-source supply chain reviews. |

Do not run any listed third-party code in the catalog's CI or grant it repository secrets. For deeper evaluation, isolate execution and report exact versions, scope, evidence, dependencies and known gaps.

## 6. Native interfaces and font engineering / Приложения и шрифты

- [Android Compose samples](https://github.com/android/compose-samples) — official application UI examples; examples are learning material, not a usability audit.
- [Apple Food Truck](https://github.com/apple/sample-food-truck) — SwiftUI application sample, useful for comparing platform-specific flows.
- [FontBakery](https://github.com/fonttools/fontbakery) — font-file quality checks; automated technical results do not decide whether typography suits a product.
- [fontTools](https://github.com/fonttools/fonttools) — font analysis and transformation tools.
- [WCAG2ICT](https://github.com/w3c/wcag2ict) — guidance for applying WCAG principles to non-web documents and software.

## 7. Architecture and decisions / Архитектура и решения

- [Microsoft API guidelines](https://github.com/microsoft/api-guidelines) and [Zalando REST API guidelines](https://github.com/zalando/restful-api-guidelines) — service-contract references; select conventions appropriate to the system.
- [DDD starter modelling process](https://github.com/ddd-crew/ddd-starter-modelling-process) — structured domain-modeling guidance.
- [Architecture decision records](https://github.com/architecture-decision-record/architecture-decision-record) and [MADR](https://github.com/adr/madr) — decision context, alternatives and consequences.
- [Vale](https://github.com/vale-cli/vale) — prose linting for chosen editorial rules; factual accuracy still needs review.

## 8. Applying this collection / Как использовать

1. Start from the actual product or user problem; choose a **reference**, not a template to copy.
2. Write a one-paragraph design direction: audience, use case, content hierarchy, visual tone and interaction density.
3. Sketch meaningful alternatives; critique why a layout, font, animation or decoration exists.
4. For interactive products, inspect keyboard access, focus, mobile viewports and success/error/empty/loading states.
5. Verify any quality claim with reproducible evidence; keep metadata-only discovery separate from design or runtime tests.

**No universal “never use gradients/cards/Inter/AI” rule.** The issue is defaulting to a visual recipe without a product reason.

Cross-category starting points: [Design](../02-design-and-creative/README.md) · [Components](../04-web-components/README.md) · [AppSec](../14-cybersecurity/README.md) · [Learning](../23-learning-and-research/README.md) · [Collections](../24-awesome-collections/README.md).

**Provenance:** repository metadata and selected upstream READMEs were reviewed on 2026-10-27. Canonical IDs, license signals and original RU/EN descriptions are recorded in section 37; cross-category links are counted once. Their status can change. This document does not claim functional or security verification.
