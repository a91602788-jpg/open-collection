# Отраслевая поисковая партия / Sector discovery — 2026-10-28

[Review data](2026-10-28-sector-discovery.json) · [Topic index](../topics.json) · [Discovery queue](../README.md)

Добавлены **26 новых кандидатов** по шести заполненным исследовательским темам. Очередь: **1 896 → 1 922**, карта исследования: **70 → 76 тем**. Все новые записи имеют статус `pending-editorial-review`; новых записей основного каталога и опубликованных категорий в этой партии нет.

База — commit `b3cb96b6fc0f01a49555a9f2a7d113172fa59715` [PR #6](https://github.com/a91602788-jpg/open-collection/pull/6), который основан на открытом [PR #5](https://github.com/a91602788-jpg/open-collection/pull/5). Ветка содержит 1 307 записей основного каталога и 63 категории; эти числа не означают, что PR уже слиты в main.

## Как искали / Method

Два субагента GPT-6 Luna исследовали космос/морские технологии и музыку/фотографию; GPT-6.1 Sol — физическую безопасность и учёт животных. Основной Codex повторно прочитал метаданные и README всех 26 выбранных репозиториев, сверил их с 3 203 ранее известными ID и проверил отсутствие совпадений между агентами. Внешние модели OpenRouter не использовались.

Recorded 32 bounded search retrievals with 484 returned observations, including repeated IDs across queries. This is not a claim about all GitHub matches or comprehensive discovery. The earlier 70-topic search snapshot was not repeated. Each topic file retains the actual queries, observed IDs and candidate-specific `discovery_sources`.

Descriptions distinguish applications, libraries, plugin hosts and reference implementations. GitHub license detections are kept separate from upstream declarations. One unsupported extra discovery tag for RawTherapee was removed; its confirmed RawTherapee-query source remains.

## Найденные ресурсы / Resources

### Космос и аэрокосмические технологии / Space & aerospace — 5

[Candidates and search history](../candidates/71-space-and-aerospace.json)

**[satellogic/orbit-predictor](https://github.com/satellogic/orbit-predictor)** — library, ID `110282435`.

Python-библиотека для расчёта положения спутников и пролётов над заданными точками по TLE; использует реализацию SGP4.

Python library for satellite positions and site passes from TLE data, wrapping the python-sgp4 implementation.

[README](https://github.com/satellogic/orbit-predictor/blob/master/README.rst) · [License source](https://github.com/satellogic/orbit-predictor/blob/master/LICENSE) · [Metadata](https://api.github.com/repos/satellogic/orbit-predictor). GitHub license signal: `MIT`.

Ограничения / limitations: Orbit propagation delegates to python-sgp4; pass predictions depend on input TLE data.

**[JuliaSpace/SatelliteToolboxPropagators.jl](https://github.com/JuliaSpace/SatelliteToolboxPropagators.jl)** — library, ID `625713980`.

Пакет Julia с аналитическими J2/J4, двухтельной и SGP4/SDP4 моделями распространения орбиты для экосистемы SatelliteToolbox.jl.

Julia package providing J2, J4, two-body, and SGP4/SDP4 orbit propagators for the SatelliteToolbox.jl ecosystem.

[README](https://github.com/JuliaSpace/SatelliteToolboxPropagators.jl/blob/main/README.md) · [License source](https://github.com/JuliaSpace/SatelliteToolboxPropagators.jl/blob/main/LICENSE.txt) · [Metadata](https://api.github.com/repos/JuliaSpace/SatelliteToolboxPropagators.jl). GitHub license signal: `MIT`.

Ограничения / limitations: Part of a larger Julia package ecosystem; no operational accuracy review performed.

**[open-space-collective/open-space-toolkit-astrodynamics](https://github.com/open-space-collective/open-space-toolkit-astrodynamics)** — library, ID `136835751`.

C++ и Python-инструментарий для орбитальной и полётной динамики, ориентации аппарата, анализа доступа и миссий.

C++ and Python toolkit for orbit and flight dynamics, spacecraft attitude, access analysis, and mission studies.

[README](https://github.com/open-space-collective/open-space-toolkit-astrodynamics/blob/main/README.md) · [License source](https://github.com/open-space-collective/open-space-toolkit-astrodynamics/blob/main/LICENSE) · [Metadata](https://api.github.com/repos/open-space-collective/open-space-toolkit-astrodynamics). GitHub license signal: `Apache-2.0`.

Ограничения / limitations: Describes an analysis toolkit; repository claims do not establish mission or safety qualification.

**[nyx-space/nyx](https://github.com/nyx-space/nyx)** — library, ID `115235540`.

Библиотека на Rust для проектирования миссий, определения орбиты и расчёта траекторий; README указывает AGPL для ядра и отдельные условия для premium-функций.

Rust library for mission design, orbit determination, and trajectory analysis; the core is AGPL-licensed, with separate terms for premium features.

[README](https://github.com/nyx-space/nyx/blob/master/README.md) · [License source](https://github.com/nyx-space/nyx/blob/master/LICENSE) · [Metadata](https://api.github.com/repos/nyx-space/nyx). GitHub license signal: `AGPL-3.0`.

Ограничения / limitations: README describes separate licensing for premium features; no mission-readiness or performance claims are independently verified.

**[jacobwilliams/Fortran-Astrodynamics-Toolkit](https://github.com/jacobwilliams/Fortran-Astrodynamics-Toolkit)** — library, ID `21782788`.

Библиотека на Fortran для задач орбитальной механики: решатели Ламберта, распространение орбит, эфемериды, модели сил и преобразования элементов.

Fortran library for orbital mechanics, including Lambert solvers, orbit propagation, ephemerides, force models, and element conversions.

[README](https://github.com/jacobwilliams/Fortran-Astrodynamics-Toolkit/blob/master/README.md) · [License source](https://github.com/jacobwilliams/Fortran-Astrodynamics-Toolkit/blob/master/LICENSE) · [Metadata](https://api.github.com/repos/jacobwilliams/Fortran-Astrodynamics-Toolkit). GitHub license signal: `CHECK-LICENSE`; upstream declaration: `NOASSERTION`.

Ограничения / limitations: README labels the toolkit a work in progress; LICENSE uses custom terms without a detected SPDX identifier.

### Морские технологии и навигация / Maritime & navigation — 3

[Candidates and search history](../candidates/72-maritime-and-navigation.json)

**[yellowfeather/AisParser](https://github.com/yellowfeather/AisParser)** — library, ID `159361959`.

C#-библиотека декодирует сообщения AIS и извлекает сведения о судах из потоков AIVDM/AIVDO.

C# library for decoding AIS AIVDM/AIVDO messages into vessel information.

[README](https://github.com/yellowfeather/AisParser/blob/master/README.md) · [License source](https://github.com/yellowfeather/AisParser/blob/master/LICENSE) · [Metadata](https://api.github.com/repos/yellowfeather/AisParser). GitHub license signal: `MIT`.

Ограничения / limitations: AIS message decoding only; does not provide a live vessel feed or navigation service.

**[canboat/canboatjs](https://github.com/canboat/canboatjs)** — library, ID `118728494`.

TypeScript-библиотека и CLI для декодирования и формирования NMEA 2000, включая поддержку PGN и интерфейсы к шлюзам.

TypeScript library and CLI for decoding and encoding NMEA 2000 data, including PGN handling and gateway interfaces.

[README](https://github.com/canboat/canboatjs/blob/master/README.md) · [License source](https://github.com/canboat/canboatjs/blob/master/LICENSE.md) · [Metadata](https://api.github.com/repos/canboat/canboatjs). GitHub license signal: `Apache-2.0`.

Ограничения / limitations: Requires a compatible gateway or CAN interface for direct network use; not a chartplotter.

**[zaari/nmea-parser](https://github.com/zaari/nmea-parser)** — library, ID `302067149`.

Библиотека Rust разбирает сообщения NMEA 0183 для AIS классов A/B и основных предложений GNSS.

Rust library parsing NMEA 0183 sentences for AIS Class A/B and commonly used GNSS messages.

[README](https://github.com/zaari/nmea-parser/blob/master/README.md) · [License source](https://github.com/zaari/nmea-parser/blob/master/LICENSE) · [Metadata](https://api.github.com/repos/zaari/nmea-parser). GitHub license signal: `Apache-2.0`.

Ограничения / limitations: Parser library only; the README documents selected AIS and GNSS sentence coverage, not the full NMEA standard.

### Музыка и производство звука / Music & audio production — 5

[Candidates and search history](../candidates/73-music-and-audio-production.json)

**[gridsound/daw](https://github.com/gridsound/daw)** — application, ID `55375779`.

Браузерная DAW на Web Audio для создания композиций; авторы обозначают проект как находящийся в разработке и частично открытый.

A browser DAW built on Web Audio for composing music; its authors describe it as work in progress and only partly open source.

[README](https://github.com/gridsound/daw/blob/main/README.md) · [License source](https://github.com/gridsound/daw/blob/main/LICENSE) · [Metadata](https://api.github.com/repos/gridsound/daw). GitHub license signal: `AGPL-3.0`.

Ограничения / limitations: README says work in progress and half open-source; saving compositions through the hosted service requires an account. Not runtime-tested.

**[falkTX/Carla](https://github.com/falkTX/Carla)** — application, ID `7517166`.

Хост аудиоплагинов для подключения и маршрутизации инструментов и эффектов; README перечисляет LADSPA, DSSI, LV2, VST и AU.

An audio plugin host for connecting and routing instruments and effects; its README lists LADSPA, DSSI, LV2, VST and AU formats.

[README](https://github.com/falkTX/Carla/blob/main/README.md) · [License source](https://github.com/falkTX/Carla/blob/main/README.md#what-is-carla) · [Metadata](https://api.github.com/repos/falkTX/Carla). GitHub license signal: `CHECK-LICENSE`; upstream declaration: `GPL-2.0-or-later`.

Ограничения / limitations: Repository API did not report a detected license; README states GPL version 2 or later. Plugin and driver support were not tested.

**[surge-synthesizer/surge](https://github.com/surge-synthesizer/surge)** — application (audio_plugin), ID `149678202`.

Открытый синтезатор Surge XT в виде плагина; команда публикует исходный код и ссылки на загрузки для музыкантов.

Surge XT is an open-source synthesizer plugin; its team publishes source code and musician downloads.

[README](https://github.com/surge-synthesizer/surge/blob/main/README.md) · [License source](https://github.com/surge-synthesizer/surge/blob/main/LICENSE) · [Metadata](https://api.github.com/repos/surge-synthesizer/surge). GitHub license signal: `GPL-3.0`.

Ограничения / limitations: Plugin source, not a DAW. Compatibility and included sound assets were not independently audited.

**[DBraun/DawDreamer](https://github.com/DBraun/DawDreamer)** — library, ID `284760653`.

Python-библиотека на базе JUCE для построения аудиосцен, запуска VST-инструментов и эффектов и автоматизации параметров.

A JUCE-based Python library for building audio graphs, running VST instruments and effects, and automating parameters.

[README](https://github.com/DBraun/DawDreamer/blob/main/README.md) · [License source](https://github.com/DBraun/DawDreamer/blob/main/LICENSE) · [Metadata](https://api.github.com/repos/DBraun/DawDreamer). GitHub license signal: `GPL-3.0`.

Ограничения / limitations: Developer library rather than a standalone DAW; plugin loading and native build requirements were not tested.

**[LMMS/lmms](https://github.com/LMMS/lmms)** — application, ID `15778896`.

Кроссплатформенная программа для музыкального производства; репозиторий связывает исходники, релизы и руководство пользователя.

Cross-platform music production software; the repository links its source, releases and user manual.

[README](https://github.com/LMMS/lmms/blob/master/README.md) · [License source](https://github.com/LMMS/lmms/blob/master/COPYING) · [Metadata](https://api.github.com/repos/LMMS/lmms). GitHub license signal: `GPL-2.0`.

Ограничения / limitations: Repository documentation reviewed, not the application; recording, plugin and platform behavior was not tested.

### Фотография и обработка изображений / Photography & imaging — 5

[Candidates and search history](../candidates/74-photography-and-imaging.json)

**[darktable-org/darktable](https://github.com/darktable-org/darktable)** — application, ID `3791835`.

Фотографический workflow и RAW-проявщик с каталогом цифровых негативов, просмотром на lighttable и неразрушающим редактированием.

A photography workflow and RAW developer with a digital-negative database, lighttable browsing and non-destructive editing.

[README](https://github.com/darktable-org/darktable/blob/master/README.md) · [License source](https://github.com/darktable-org/darktable/blob/master/LICENSE) · [Metadata](https://api.github.com/repos/darktable-org/darktable). GitHub license signal: `GPL-3.0`.

Ограничения / limitations: Camera-specific RAW support was not checked; entry should not imply compatibility with a particular camera.

**[RawTherapee/RawTherapee](https://github.com/RawTherapee/RawTherapee)** — application, ID `40539005`.

Кроссплатформенное приложение для обработки RAW-фотографий; репозиторий содержит исходники программы и документацию.

A cross-platform application for processing RAW photographs; the repository contains the program source and documentation.

[README](https://github.com/RawTherapee/RawTherapee/blob/dev/README.md) · [License source](https://github.com/RawTherapee/RawTherapee/blob/dev/LICENSE) · [Metadata](https://api.github.com/repos/RawTherapee/RawTherapee). GitHub license signal: `GPL-3.0`.

Ограничения / limitations: Camera-specific decoding support and processing behavior were not verified.

**[ncruces/RethinkRAW](https://github.com/ncruces/RethinkRAW)** — application, ID `169814657`.

Приложение для проявки RAW-фотографий; README описывает релизы и установку через Scoop или Homebrew.

An application for developing RAW photographs; its README documents releases and installation through Scoop or Homebrew.

[README](https://github.com/ncruces/RethinkRAW/blob/master/README.md) · [License source](https://github.com/ncruces/RethinkRAW/blob/master/LICENSE) · [Metadata](https://api.github.com/repos/ncruces/RethinkRAW). GitHub license signal: `MIT-0`.

Ограничения / limitations: Camera compatibility and processing quality were not tested; repository documentation only. README identifies Adobe DNG Converter as a dependency; its terms and camera-specific support were not reviewed.

**[pch/rawmakase](https://github.com/pch/rawmakase)** — application, ID `1389278567`.

Неразрушающий RAW-проявщик с каталогом и импортом части настроек и метаданных Lightroom Classic.

A non-destructive RAW developer with a catalog and import for some Lightroom Classic settings and metadata.

[README](https://github.com/pch/rawmakase/blob/main/README.md) · [License source](https://github.com/pch/rawmakase/blob/main/LICENSE) · [Metadata](https://api.github.com/repos/pch/rawmakase). GitHub license signal: `MIT`.

Ограничения / limitations: README says WebP, AVIF and JPEG XL export is not yet available and Lightroom compatibility has not been measured; not independently tested. README identifies early software with changing rendering and limited backward compatibility before 1.0.

**[tropy/tropy](https://github.com/tropy/tropy)** — application, ID `45496875`.

Приложение для исследователей: помогает описывать и упорядочивать фотографии архивных источников, чтобы находить их по контексту.

A research photo management application for describing and organizing source photographs so researchers can retrieve them by context.

[README](https://github.com/tropy/tropy/blob/main/README.md) · [License source](https://github.com/tropy/tropy/blob/main/LICENSE) · [Metadata](https://api.github.com/repos/tropy/tropy). GitHub license signal: `CHECK-LICENSE`; upstream declaration: `AGPL-3.0`.

Ограничения / limitations: Designed for research photographs and source description, not a general-purpose RAW developer; upstream notes a separate trademark.

### Физическая безопасность и контроль доступа / Physical security & building access — 5

[Candidates and search history](../candidates/75-physical-security-and-building-access.json)

**[scottlamb/moonfire-nvr](https://github.com/scottlamb/moonfire-nvr)** — application, ID `48900514`.

Приложение NVR записывает H.264-потоки IP-камер по RTSP и позволяет выбирать и экспортировать временные фрагменты видео.

NVR application records H.264 RTSP camera streams and exports selected time ranges as MP4 video.

[README](https://github.com/scottlamb/moonfire-nvr/blob/master/README.md) · [License source](https://github.com/scottlamb/moonfire-nvr/blob/master/LICENSE.txt) · [Metadata](https://api.github.com/repos/scottlamb/moonfire-nvr). GitHub license signal: `CHECK-LICENSE`; upstream declaration: `GPL-3.0-or-later WITH GPL-3.0-linking-exception`.

Ограничения / limitations: Pre-1.0; README describes basic web UI, no motion detection, and TLS through a separate proxy.

**[opensensor/lightNVR](https://github.com/opensensor/lightNVR)** — application, ID `944391405`.

NVR для Linux записывает потоки IP-камер, предоставляет просмотр через браузер и управляет сроками хранения записей.

Linux NVR records IP camera streams, provides browser playback, and manages recording retention.

[README](https://github.com/opensensor/lightNVR/blob/main/README.md) · [License source](https://github.com/opensensor/lightNVR/blob/main/LICENSE) · [Metadata](https://api.github.com/repos/opensensor/lightNVR). GitHub license signal: `GPL-3.0`.

Ограничения / limitations: Optional detection uses separate services; resource and hardware compatibility claims were not tested.

**[roflcoopter/viseron](https://github.com/roflcoopter/viseron)** — application, ID `291498455`.

Локальное приложение NVR объединяет запись камер с компонентами обнаружения движения и объектов и веб-интерфейсом настройки.

Local NVR application combines camera recording with motion and object detection components and browser configuration.

[README](https://github.com/roflcoopter/viseron/blob/dev/README.md) · [License source](https://github.com/roflcoopter/viseron/blob/dev/LICENSE) · [Metadata](https://api.github.com/repos/roflcoopter/viseron). GitHub license signal: `MIT`.

Ограничения / limitations: Docker and component configuration required; recognition accuracy and hardware compatibility not reviewed.

**[cameraui/camera.ui](https://github.com/cameraui/camera.ui)** — application, ID `421865133`.

Платформа для камер предоставляет прямой просмотр, плагины и интеграции умного дома; часть функций записи и поиска требует подписки.

Camera platform provides live viewing, plugins, and smart-home integrations; some recording and search features require a subscription.

[README](https://github.com/cameraui/camera.ui/blob/master/README.md) · [License source](https://github.com/cameraui/camera.ui/blob/master/LICENSE.md) · [Metadata](https://api.github.com/repos/cameraui/camera.ui). GitHub license signal: `MIT`.

Ограничения / limitations: README marks continuous recording, semantic search, and push notifications as subscription features; pricing not reviewed.

**[nrfconnect/ncs-door-lock-and-access-control](https://github.com/nrfconnect/ncs-door-lock-and-access-control)** — toolkit (reference implementation), ID `918341005`.

Эталонная реализация для nRF Connect SDK помогает разрабатывать электронные замки и считыватели доступа с Aliro и Matter.

nRF Connect SDK reference implementation supports development of Aliro and Matter door locks and access readers.

[README](https://github.com/nrfconnect/ncs-door-lock-and-access-control/blob/main/README.md) · [License source](https://github.com/nrfconnect/ncs-door-lock-and-access-control/blob/main/LICENSE) · [Metadata](https://api.github.com/repos/nrfconnect/ncs-door-lock-and-access-control). GitHub license signal: `CHECK-LICENSE`; upstream declaration: `LicenseRef-Nordic-5-Clause`.

Ограничения / limitations: Source-available hardware-restricted license permits use only with Nordic Semiconductor integrated circuits; not a turnkey building access system.

### Уход за животными и приюты / Animal care & shelters — 3

[Candidates and search history](../candidates/76-animal-care-and-shelters.json)

**[oldauntie/ababu](https://github.com/oldauntie/ababu)** — application, ID `262356963`.

Приложение ветеринарного учёта на PHP с хранением данных в MariaDB.

PHP veterinary practice record application backed by MariaDB.

[README](https://github.com/oldauntie/ababu/blob/master/README.md) · [License source](https://github.com/oldauntie/ababu/blob/master/LICENSE) · [Metadata](https://api.github.com/repos/oldauntie/ababu). GitHub license signal: `AGPL-3.0`.

Ограничения / limitations: README describes an evolving project and future installers; operational completeness and clinical workflows not tested.

**[evangauer/openvpm](https://github.com/evangauer/openvpm)** — application, ID `1185503465`.

Веб-приложение ветеринарной практики ведёт пациентов, приёмы, записи и счета; предоставляет API для поддерживаемых интеграций.

Veterinary practice application manages patients, appointments, records, and invoices, with an API for supported integrations.

[README](https://github.com/evangauer/openvpm/blob/main/README.md) · [License source](https://github.com/evangauer/openvpm/blob/main/LICENSE) · [Metadata](https://api.github.com/repos/evangauer/openvpm). GitHub license signal: `AGPL-3.0`.

Ограничения / limitations: Upstream distinguishes implemented workflows from roadmap; clinic pilot readiness, clinical accuracy, payments, and security not assessed.

**[UkraineAnimalHelp/Shelters-Management-App](https://github.com/UkraineAnimalHelp/Shelters-Management-App)** — application, ID `779973623`.

Flutter-приложение для организации работы приютов для животных; использует Firebase.

Flutter application for animal shelter operations using Firebase services.

[README](https://github.com/UkraineAnimalHelp/Shelters-Management-App/blob/master/README.md) · [License source](https://github.com/UkraineAnimalHelp/Shelters-Management-App/blob/master/LICENSE) · [Metadata](https://api.github.com/repos/UkraineAnimalHelp/Shelters-Management-App). GitHub license signal: `GPL-3.0`.

Ограничения / limitations: Flutter/Firebase dependencies; last repository push 2024-12-13; deployment and feature completeness not tested.

## Отбор и ограничения / Review boundaries

Архивные зеркала digiKam и Hugin, репозитории-потомки вместо первоисточников и неоднозначный GitHub/Codeberg-источник SentryShot не добавлены. Остальные исключения и отложенные варианты перечислены с причинами и источниками в JSON; отбор ограничен этой партией и не является общим рейтингом проектов.

The Nordic access-control reference uses a hardware-restricted license, not a general permissive software license. GridSound describes a partly open project, Nyx separates premium-feature terms, and camera.ui marks some features as subscription-based. These distinctions remain explicit; no current price comparison or legal clearance is claimed. RethinkRAW documents an Adobe DNG Converter dependency. Tropy separates its source license from trademark terms.

Проверены публичные метаданные, README и лицензионные сигналы. Сторонние проекты не клонировались, не устанавливались и не запускались. Точность орбитальных расчётов, морской навигации, распознавания камер, медицинских записей, совместимость RAW-камер и аудиоплагинов не тестировалась. Цены, развёртывание, безопасность и эксплуатационная готовность остаются непроверенными.

Шесть новых файлов — исследовательские направления, а не пустые папки опубликованного каталога. Перед продвижением кандидатов требуется отдельная редакционная партия с обновлением каталога, Markdown и производной AI-навигации; слияние остаётся за владельцем.
