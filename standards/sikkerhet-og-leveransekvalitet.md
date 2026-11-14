# Sikkerhetskrav og Definition of Done — v0.2

**Sikkerhet er P0 fra første kodecommit.** Ingen «security later»-fase.

## Rettighetsmodell

| Operasjon | Standardrettigheter | Annet |
|---|---|---|
| Normal kjøring, stemmetest, profil, import/eksport | Standardbruker | UAC/sudo/root **forbudt** i normal drift |
| Mikrofontilgang | Standardbruker + OS-mikrofontillatelse | Innhent kun ved uttrykkelig teststart; steng ved stopp |
| Windows per-user NSIS-installasjon | Normalt standardbruker | Tauri `installMode: currentUser`, til lokal brukerprofil |
| Windows per-machine-installasjon | Admin kan kreves | Kun frivillig og tydelig forklart, ikke standard |
| Manglende WebView2/systemruntime | Avhenger av konkret distribusjon/OS | Varsles særskilt, helst kontrollert offline/proveniens |
| Mac vanlig kjøring/egen brukerinstallasjon | Standardbruker | Systemwide installasjon/signering kan ha egne krav |
| Utviklerverktøy på utviklingsmaskinen | Kan kreve admin ved installasjon | **Skal ikke** smitte over på sluttbrukerens kjørerettigheter |

**Release-blokkerende test:** Start, test, import, eksporter og avinstaller applikasjonen under en dedikert Windows-standardbruker og ikke-administrativ Mac-bruker. Dokumenter alle forhøyede installasjonsoperasjoner med formål, utgiver og alternativ.

## Trusselmodell og tiltak (P0)

1. **Supply-chain:** Kompromitterte npm-, Cargo- og transitive pakker; reviews på direkte avhengigheter og kritiske transitiver; lockfiles; faste versjoner; ikke `curl | sh`/ukontrollert installasjon. Pinned CI actions, SBOM og sikkerhetsskanning.
2. **Falske installasjonsfiler:** SHA-256, kildecommit, release-notat, senere kodesignering/notarisering. Unngå automatiske oppdateringer i MVP.
3. **Ubetrodd profilimport:** Allowlist ZIP, grenser for komprimert/utpakket størrelse, traversal, symlink/duplikat, JSON-schema, ingen kodekjøring, transaksjonell lagring. SHA-256 i manifestet er ingen autentisering.
4. **OS-tilganger:** Ingen kernel-drivere, systemtjenester, startoppgaver, oppstart i admin-kontekst eller bred fil-/nettverkstilgang. Tauri capabilities og CSP settes til minste behov.
5. **Personvern:** Ingen rålydopptak lagres som standard; ingen telemetri. Personlige profiler og opptak holdes unna GitHub.
6. **Parser og ressursbruk:** Test korrupte MP3/ChordPro-filer i senere faser, uendelige datastrømmer, store testfiler og skadefull filmetadata.
7. **Utviklerkonto:** GitHub-repo `Private`, MFA/passkey, begrensede GitHub Actions-tillatelser. Ingen hemmeligheter i repo eller logger.
8. **Anatomi/modeller:** Åpne GitHub-modeller er inspirasjon, ikke automatisk godkjent kode. Vurder lisens, vedlikehold, opprinnelse, presisjon og om modellen kan mislede.

## Tiltak som ikke garanterer sikkerhet

Et stort populært bibliotek er ikke nødvendigvis trygt. Lockfil begrenser uventede versjonsendringer, men beskytter ikke mot en kompromittert versjon vi selv har godkjent. En privat GitHub-repo beskytter ikke mot kompromittert lokal PC/konto. SBOM er en oversikt, ikke en forsikring. Tauri capabilities/CSP reduserer angrepsflate, men gjør ikke import og lydkode risikofri.

## Windows 10 og releasepolicy

Windows 10 har passert ordinær support for vanlige Home/Pro-utgaver. Utviklingsmaskinen kan brukes for kravarbeid. Før signering eller ekstern distribusjon bør et støttet, oppdatert Windows-byggmiljø benyttes og sluttbrukerstøtten avklares. Test appen på Windows 10 som avtalt, men ikke lov sikkerhetsoppdateringer Microsoft ikke gir.

## Definition of Done – P0

- [ ] Sporbar historie, spesifikasjon, tester og Git-revisjon.
- [ ] Alle P0-tester i `tester/akseptansetestmatrise.md` er bestått.
- [ ] Standardbrukerkjøring på Windows/macOS uten UAC/root; installasjonsunntak er begrunnet.
- [ ] Ingen skjult nettverkstrafikk, konto, telemetri eller automatisk lagring av råopptak.
- [ ] Enhets- og mikrofontillatelser er eksplisitte og slippes ved avbrudd.
- [ ] Feil i import/eksport skal aldri ødelegge originalprofil, historikk eller database.
- [ ] Kompatibilitetstester for gamle og fremtidige profiler inkl. ukjent major/minor.
- [ ] Originale målinger og versjoner bevares; «ikke målt» vises som dette.
- [ ] Dependency review, lisensoversikt, lockfiler, sårbarhetssøk, SBOM, checksums og review av CI er dokumentert.
- [ ] Installerbare artefakter er sporbare; ingen uautoriserte drivere eller kode nedlastet ved kjøring.

## Referanser

- Tauri: https://v2.tauri.app/distribute/windows-installer/
- GitHub supply-chain: https://docs.github.com/en/code-security/concepts/supply-chain-security/supply-chain-security
- OWASP: https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html
