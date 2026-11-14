# Oppsett: Mac → GitHub → kontroller → macOS/Windows-bygg

**Versjon:** 0.3, 14.11.2026.  **Fase:** Oppsett, ingen applikasjonskode er inkludert.

## A. GitHub og editor (ingen terminal nødvendig)

1. Installer GitHub Desktop fra https://desktop.github.com/ og VS Code fra https://code.visualstudio.com/.
2. Logg inn i GitHub Desktop og kontroller at 2FA/passkey er aktivert på GitHub.
3. Hvis `gitar-stemme` allerede finnes på GitHub: `File → Clone Repository`, velg en lokal mappe som `~/Developer/gitar-stemme`.
4. Hvis det ikke finnes: `File → New Repository`; navn `gitar-stemme`, deretter `Publish repository` og **Keep this code private**.
5. I GitHub Desktop: `Repository → Show in Finder`. Pakk ut ZIP-pakken og kopier **innholdet** *inn* i repoets rotmappe (inkludert `.github` og `.gitignore`). Finder skjuler punktumfiler som standard: trykk `Cmd+Shift+.` for å vise dem før du kopierer. Ikke kopier en ny overordnet mappe inn i repoet. Ikke overskriv `.git` (den finnes ikke i pakken).
6. GitHub Desktop → Changes: kontroller at ingen private lydfiler, stemmeprofiler, passord eller nøkler listes. Legg inn commit `Opprett SDD og CI-baseline v0.3`, trykk `Commit to main` og `Push origin`.
7. Gå til repoet i nettleseren → `Actions` → `01 SDD baseline`. Vent til arbeidsflyten er grønn. Hvis GitHub spør om å aktivere Actions, godkjenn kun arbeidsflytene du har kontrollert.

## B. Lokale kompilatorverktøy på Mac

Åpne Terminal og kjør, én om gangen:

```bash
git --version
xcode-select -p
node --version
npm --version
rustc --version
cargo --version
```

- Ved manglende Xcode Command Line Tools: `xcode-select --install`.
- Installer Node.js LTS fra https://nodejs.org/en/download.
- Installer Rust gjennom verifisert Rustup-metode på https://rustup.rs/; gjennomgå kommando/script før kjøring. Utviklingsverktøy trenger ikke å kjøres som root etter installering.
- Start Terminal på nytt og kontroller versjonene.

## C. Opprett Tauri 2 / React-prosjekt i eksisterende repo

Kun når GitHub-kontrollen er grønn og verktøy er installert:

1. I GitHub Desktop: `Repository → Open in Visual Studio Code`.
2. I VS Code: Terminal → New Terminal (du skal stå i `gitar-stemme`). Bekreft med `pwd`. Repoet bør ligge på en lokal disk, ikke i en synkronisert iCloud-/OneDrive-mappe.
3. Se gjennom den offisielle Tauri-generatoren på https://github.com/tauri-apps/create-tauri-app og kjør en **versjonsfestet** generator, eksempelvis `npm create tauri-app@4.7.5 app` (versjon kontrollert 14.11.2026). Ikke bruk `@latest` ukritisk ved sikkerhetsbevisst utvikling.
4. Velg: navn `app`, en unik reverse-DNS-ID (f.eks. `app.gitarstemme.desktop`), `TypeScript / JavaScript`, `npm`, `React`, `TypeScript`. Ikke kopier tilfeldig kode fra andre kilder.
5. Kjør:

```bash
cd app
npm install
npm run tauri dev
```

Tauri skal nå åpne en lokal test-app. Dette lager `app/package-lock.json` og vanligvis `app/src-tauri/Cargo.lock`: begge skal inn i Git.
Stopp testappen med `Ctrl+C` i Terminal. Kjør `npm run tauri build` fra `app` for lokal Mac-bygging.
Tilbake i GitHub Desktop: kontroller endringene, commit og push.

## D. Aktiver to-plattform kompilering i GitHub

Etter at lokal Mac-bygging fungerer:

1. Kopier `maler/02-desktop-build.yml.template` til `.github/workflows/02-desktop-build.yml`.
2. Gjennomgå nye tredjepartsavhengigheter og GitHub Actions. Workflows bruker låste commit-SHA og `contents: read`.
3. Commit og push.
4. GitHub → Actions → `02 Desktop build (manual)` → `Run workflow`.
5. Etter vellykket kjøring: åpne workflow-run og finn `Artifacts` nederst. Last ned Mac-/Windows-artefakter.

Disse artefaktene er **testbygg**, ikke ferdig signerte eller notariserte distribusjonsutgaver. CI-minutter og macOS/Windows-løpere kan belastes GitHub-kontoens kvote. Se Actions-budsjettet i GitHub før hyppige builds.

## E. Arbeidsrutine etterpå

- Skriv krav / endring i SDD-spec → lag egen branch fra main → implementer én historie → kjør lokale tester.
- Commit og push → opprett PR → sjekk at `01 SDD baseline` er grønn → review → merge.
- På private GitHub Free-repo kan håndhevet branch protection være utilgjengelig; gjennomfør samme kontroll manuelt til eventuell planstøtte er avklart.
- Slå på Dependabot-varsel for kritiske sårbarheter. Når /app finnes, utvid `.github/dependabot.yml` med npm under `/app` og Cargo under `/app/src-tauri`.

## Sikkerhet

Ingen private MP3, råopptak, `.voiceprofile`-filer eller hemmeligheter i repoet. Bruk GitHub-passkey/MFA. GitHub Actions-arbeidsflyten i fase A trenger ikke hemmeligheter og skriver aldri til repoet. Ingen vanlig app-kjøring skal kreve administratorrettigheter. Mac OS-mikrofontilgang etterspørres først når den er relevant for stemmetesten.

## Offisiell dokumentasjon

- https://v2.tauri.app/start/prerequisites/
- https://v2.tauri.app/start/create-project/
- https://v2.tauri.app/distribute/pipelines/github/
- https://docs.github.com/en/desktop/overview/creating-your-first-repository-using-github-desktop
- https://docs.github.com/en/actions/reference/security/secure-use
