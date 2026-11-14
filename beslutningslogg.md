# Beslutningslogg v0.2

| ID | Status | Beslutning / avklaring | Begrunnelse |
|---|---|---|---|
| ADR-001 | Foreslått | Tauri 2 + React + TypeScript | Samme desktop-kodebase for Win/Mac; begrensede native rettigheter |
| ADR-002 | Besluttet | Local-first; ingen konto/server/telemetri i stemmetest | Brukereierstyring og robust offline-bruk |
| ADR-003 | Besluttet | Standardbruker ved kjøring; ingen admin-oppheving | Minste privilegium |
| ADR-004 | Besluttet | Kryssplattform `.voiceprofile` med migrering og uforanderlig historikk | Portabilitet og langsiktig dataverdi |
| ADR-005 | Foreslått | ZIP + JSON manifest og profilpayload | Validerbart og åpent filformat |
| ADR-006 | Besluttet | Ingen rålydopptak i MVP | Personvern, enkel portabilitet |
| ADR-007 | Besluttet | Mikrofonmål, egenvurderinger og estimater holdes separat | Unngå villedende data og opplæring |
| ADR-008 | Foreslått | GitHub Desktop + VS Code og privat repo | Lav terskel for nybegynner |
| ADR-009 | Besluttet | Sikkerhet og dependency-kontroll er P0 | Gjelder fra første kodecommit |
| ADR-010 | Uavklart | Analysebibliotek for F0, versjon og akseptable målgrenser | Må testes mot reelle stemmer og mikrofoner |
| ADR-011 | Uavklart | Øvre grense for profiler med tidsserier og eksakt JSON-schema | Må avklares før implementasjon |
| ADR-012 | Foreslått | Anatomimodell kun pedagogisk i P2, vurder Vocal Tract Lab som referanse | Kan ikke utlede sann anatomi fra mikrofon |
| ADR-013 | Uavklart | Om betalte CI-løpere for macOS er ønskelig | Kostnad og kode-/release-sikkerhet |
| ADR-014 | Foreslått | GitHub Spec Kit innføres senere, ikke nødvendig for første repo-opprettelse | Skille onboarding fra verktøykonfigurasjon |

**Merk:** «Besluttet» betyr at dette er akseptert som designretning i dialogen. Foreslått/uavklart må tas stilling til ved implementeringsplan.
