# Utviklingsmiljø — først når vi skal kjøre kode

Opprett repository og SDD-baseline først. Dette er **ikke** nødvendige installasjoner for å legge Markdown-filene i GitHub.

## Kompilering på Windows

- **Visual Studio Code:** Allerede installert av bruker.
- **GitHub Desktop:** Lokal versjonskontroll og synkronisering med repo.
- **Node.js LTS og npm:** Lastes kun fra nodejs.org når frontend-utvikling begynner. Lås npm-avhengigheter i lockfil.
- **Rust / rustup:** Lastes fra rust-lang.org via prosjektets oppdaterte Tauri-krav. Velg eksplisitt, kontrollert installasjon.
- **Microsoft C++ Build Tools / Windows SDK:** Kan være nødvendige for Tauri på Windows. Installasjon kan kreve administratorrettigheter; dette gjelder **utviklingsmaskinen**, ikke sluttbruker-appen. Kontroller Tauri-dokumentasjonen før installasjon.
- **WebView2:** Ta i bruk systemets eksisterende kjøretid der den er tilstrekkelig. Dokumenter særskilt installer når den mangler.

## Kompilering på macOS

- Xcode Command Line Tools, Rust og Node.js etter kontrollert installasjonsplan.
- Bygg `.app`/`.dmg` på støttet macOS-maskin eller godkjent macOS CI-løper.
- Signering og notarization når distribusjon krever det.

## Tredjepartskode og supply-chain

1. Godkjenn direkte avhengigheter i en egen `dependency-approval`-prosess.
2. Kjør låste installasjoner (`npm ci`, `cargo --locked`) når repoet inneholder lockfiler.
3. Gjennomgå transitive avhengigheter, lisens, sikkerhetsvarsler og maintainer-/releasehistorikk.
4. Pin tredjeparts GitHub Actions til full commit-hash, og begrens CI-token til minste tillatelser.
5. Produser SBOM, sjekksummer, signering der relevant, og dokumentasjon av byggmiljø ved release.

## Praktisk sikkerhetsavgrensning for Windows 10

Windows 10 er uten ordinær support (med unntak for særskilte utvidede sikkerhetsoppdateringsprogrammer). Begrens konto-/repo-tilgang og vurder en støttet maskin for signering/release. Vi trenger ikke oppgradere PC-en bare for å opprette kravrepo, men det er fornuftig å bygge produksjonsrelease i et støttet, oppdatert miljø.

## Viktig

Ingen installasjon av egne mikrofon- eller lyddrivere er planlagt. Bruk eksisterende operativsystemdrivere og API-er.
