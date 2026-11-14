# Gitar & Stemme — SDD-grunnlag v0.3 – pipeline

**Dato:** 14. november 2026  
**Status:** Kravbaseline + automatisk SDD-validering (GitHub Actions). Ingen Tauri-applikasjon er implementert.  
**Første implementeringsmål:** Lokal stemmetest og portabel stemmeprofil på Windows og macOS.  
**Metode:** Spesifikasjonsdrevet utvikling (SDD). Først spesifikasjon, deretter plan, oppgaver, implementasjon og tester.

## Hva er nytt siden v0.1?

1. **Profiler og kompatibilitet:** Versjonert, plattformuavhengig filformat; migrering fra eldre versjoner, sikring av fremtidige datafelt, bevaring av historiske observasjoner og eksplisitt håndtering av ukjent fremtidig format.
2. **Lydanalyse:** Utvidelse fra toneomfang til stabilitet, intonasjon, sustain, frasering og senere vokaler/resonans, med tydelig skille mellom målbare data, brukerens egne vurderinger og usikre modeller.
3. **Anatomi:** Framtidig pedagogisk 2D/3D-modell for hals, stemmebånd og tunge; **ikke** utgi akustiske estimater for å være faktisk observert anatomi.
4. **Sikkerhet og rettigheter:** Sikkerhet er et P0-krav. Normal kjøring uten administratorrettigheter; per-user Windows-installatør som standard; eksplisitt brukersamtykke for mikrofon og eventuelle råopptak.
5. **GitHub:** Ny steg-for-steg-veileder for førstegangsbruker med GitHub Desktop og VS Code, uten kommandolinjekrav for første commit.
6. **SDD-styring:** Egen grunnlov/konstitusjon, beslutningslogg og testmatrise.

## Hva skal du gjøre akkurat nå?

På Mac: Åpne **`veiledninger/03-macos-github-pipeline.md`**. Eldre Windows-veiledning finnes i `veiledninger/01-opprett-github-repo-og-utviklingsflyt.md`. Den viser hvordan du oppretter et **privat GitHub-repo** og legger inn filene med GitHub Desktop.

**Viktig:** Ikke legg private råopptak, faktiske stemmeprofiler, adgangsnøkler eller hele MP3-samlingen i GitHub. Repoet er for kode, spesifikasjoner, eksempelfiler med syntetiske verdier og automatiske tester.

## Dokumentkart

| Fil | Hva den inneholder |
|---|---|
| `produktbacklog.md` | Tidligere brukerhistorier + nye historier for profilkompatibilitet, stemmetrening og sikkerhet. |
| `specs/001-stemmetest-profil/spec.md` | Oppdatert detaljkrav til første funksjon og nye akseptansescenarier. |
| `arkitektur-og-datakontrakter.md` | Modularkitektur, prinsipper for datafangst og versjonering. |
| `kontrakter/voiceprofile-format.md` | Filformat, bakoverkompatibilitet, migrering og truede importveier. |
| `kontrakter/voiceprofile-eksempel.json` | Syntetisk eksempel, **ikke** et faktisk brukeropptak. |
| `standards/sikkerhet-og-leveransekvalitet.md` | P0-krav, avhengighetskontroll, rettigheter og Definition of Done. |
| `standards/prosjektkonstitusjon.md` | Regler for AI-agent / SDD-implementering. |
| `veiledninger/01-opprett-github-repo-og-utviklingsflyt.md` | Konkret veiledning for Windows 10, GitHub Desktop og VS Code. |
| `veiledninger/02-utviklingsmiljo-senere.md` | Verktøy som først trengs når vi faktisk skal kompilere. |
| `beslutningslogg.md` | Besluttet, foreslått og uavklart. |
| `tester/akseptansetestmatrise.md` | Konkrete akseptanse- og kompatibilitetstester. |
| `.gitignore` | Sperrer ordinære lokale data og byggfiler mot utilsiktet innlegging i Git. |

## Teknisk retning

- Frontend: React + TypeScript.
- Desktop: Tauri 2 / Rust.
- Lokal data: SQLite i brukerens profilområde.
- Distribusjon: Windows-installer (`.exe`, standard installasjon for gjeldende bruker) og macOS `.app`/`.dmg` fra samme kildekode.
- Portabel brukerdata: `.voiceprofile` (ZIP med begrenset sett JSON-dokumenter); ingen plattformspesifikke stier.
- Ulike moduler kan byttes ut uten å endre historiske dataformat eller profilidentitet.

## SDD-arbeidsrekkefølge

**Godkjenn brukerhistorier → godkjenn spesifikasjon → definér verifikasjonstester → teknisk plan → små kodeoppgaver → review → test → sammenslå i `main`.**

Første implementeringsoppgave bør være profilens serialisering, versjonsleser og migreringstester. Deretter minimal UI, mikrofontilgang, og toneanalyse. Dette gjør datakontrakten stabil før vi lagrer virkelige målinger.

## Kilder og referanser

- GitHub Desktop: https://docs.github.com/en/desktop/overview/creating-your-first-repository-using-github-desktop
- VS Code Git: https://code.visualstudio.com/docs/sourcecontrol/quickstart
- GitHub Spec Kit: https://github.github.com/spec-kit/
- Tauri v2 Windows Installer: https://v2.tauri.app/distribute/windows-installer/
- Vocal Tract Lab (inspirasjon, ikke valgt avhengighet): https://github.com/chiranjeevi-sagi/vocal-tract-lab
- ASHA vurdering av objektive stemmemål: https://pubs.asha.org/doi/10.1044/2018_AJSLP-17-0009

## CI-pipeline i v0.3

- `.github/workflows/01-sdd-validate.yml` kjører ved push, PR og manuelt og validerer dokumentbaselinen med kun Python standardbibliotek.
- `scripts/valider_sdd.py` kontrollerer syntetisk profilformat og enkelte risikable filtyper i Git-indeksen. **Dette tester ikke funksjonell profilkompatibilitet.**
- `maler/02-desktop-build.yml.template` er en **inaktiv** mal for Windows-/Mac-bygg. Aktiver først etter at Tauri-appen er opprettet i `app/`, låsefiler er committet og lokal bygging fungerer.
- `veiledninger/03-macos-github-pipeline.md` gir komplett trinn-for-trinn-oppsett.
