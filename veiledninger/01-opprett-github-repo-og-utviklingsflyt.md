# Kom i gang med GitHub og VS Code — steg for steg på Windows 10

**Mål:** En privat, tom-kode prosjektmappe med alle kravdokumentene i GitHub. Du trenger ikke kunne Git-kommandoer for denne oppgaven.

## Før vi begynner: tre begreper

- **Repository (repo):** Mappen med alle prosjektfiler og historikken over endringer. Den finnes både lokalt på PC-en og hos GitHub når den er publisert.
- **Commit:** Et navngitt lagringspunkt i historikken, f.eks. «Opprett SDD-baseline v0.2».
- **Push/Pull:** Push sender dine commits til GitHub; Pull henter inn andres/andre maskiners commits fra GitHub.
- **Branch:** En arbeidsgren. `main` er den godkjente versjonen. Vi kan senere lage `feature/voice-profile-import` for separat arbeid.

## Steg 0 — grunnleggende sikkerhet

1. Slå på **tofaktorautentisering/passkey** på GitHub-kontoen (Settings → Password and authentication).
2. Hold prosjektet **privat**, i alle fall i starten.
3. **Ikke** legg adgangsnøkler, råopptak, personlige `.voiceprofile`-filer eller kommersielle MP3-filer i repoet.
4. Bruk helst en lokal mappe, f.eks. `C:\Utvikling`, som **ikke** synkroniseres automatisk med OneDrive. GitHub Desktop tar seg av GitHub-synkronisering.
5. Installer kun fra offisielle adresser: https://desktop.github.com/ og https://code.visualstudio.com/.

## Steg 1 — installer og åpne GitHub Desktop

1. Last ned **GitHub Desktop** fra https://desktop.github.com/.
2. Installer, start og logg inn med GitHub-kontoen du allerede har opprettet.
3. Åpne GitHub Desktop → **File → New repository...**.
4. Bruk verdiene:
   - **Name:** `gitar-stemme`
   - **Description:** `Lokal applikasjon for gitar, stemmetest og sangtrening`
   - **Local path:** `C:\Utvikling` (eller en tilsvarende mappe du velger)
   - **Git ignore:** `None` eller et enkelt passende utgangspunkt (vi leverer egen `.gitignore`)
   - **License:** `None` nå. Lisens velges før eventuell offentlig publisering.
5. Trykk **Create repository**. Programmet lager mappen `C:\Utvikling\gitar-stemme`. **Ikke opprett enda et repo i denne mappen.**

**Hvis du allerede har laget et repo på github.com:** Bruk heller GitHub Desktop → **File → Clone repository...** → velg repoet → velg lokal plassering. Ikke lag et nytt repo med samme navn.

## Steg 2 — gjør repoet privat på GitHub

1. I GitHub Desktop: Klikk **Publish repository**.
2. Kryss av **Keep this code private**.
3. Bekreft med **Publish Repository**.
4. Fra menyen: **Repository → View on GitHub**. Sjekk at repoet er merket **Private**.
5. Det er helt normalt at repoet foreløpig bare har et README-dokument.

## Steg 3 — legg inn SDD-dokumentene

1. Last ned `gitarstemme_SDD_startpakke_v0_2.zip` fra ChatGPT.
2. Høyreklikk ZIP → **Pakk ut alle...**. Åpne mappen med utpakkede filer.
3. I GitHub Desktop: **Repository → Show in Explorer**. Da åpnes den **eksisterende** `gitar-stemme`-mappen.
4. Kopier **innholdet** i ZIP-mappen inn i `gitar-stemme` (ikke kopier mappen som ett ekstra nivå).
5. Dersom Windows spør om `README.md` kan erstattes, velg å erstatte med filen fra startpakken.
6. Kontroller at `gitar-stemme\README.md` og `gitar-stemme\produktbacklog.md` ligger på øverste nivå. `.gitignore` kan være skjult i Utforsker avhengig av innstillinger.

**Ikke kopier `.git`-mappen** eller bruk kommandolinjen `git init` inni repoet. GitHub Desktop har allerede etablert historikken.

## Steg 4 — første commit og push

1. Gå tilbake til GitHub Desktop. Velg fanen **Changes**.
2. Du skal se flere nye/endrede Markdown- og JSON-filer.
3. Nederst til venstre: Skriv i **Summary**: `Legg inn SDD-baseline v0.2`.
4. Klikk **Commit to main**.
5. Klikk **Push origin**.
6. Gå til github.com/repoet, oppdater siden og kontroller at dokumentene vises.

**Forskjellen:** Commit lagrer historikken lokalt; Push sender den til GitHub.

## Steg 5 — åpne prosjektet i VS Code

1. I GitHub Desktop: **Repository → Open in Visual Studio Code** (eller velg VS Code som standard editor under Options/Preferences).
2. Alternativt: VS Code → **File → Open Folder...** → `C:\Utvikling\gitar-stemme`.
3. Godkjenn **Trust** kun hvis du kjenner igjen akkurat denne mappen og innholdet.
4. Åpne `README.md`. Bruk gjerne **Open Preview** for å lese Markdown-formatert dokument.
5. Se at filutforskeren viser `produktbacklog.md`, `kontrakter/`, `specs/` og `veiledninger/`.

Det er **ikke nødvendig** å installere Rust, Node.js, Tauri eller en AI-kodeassistent bare for å etablere spesifikasjonsrepoet. Vi gjør dette kontrollert når første implementeringsoppgave er godkjent.

## Steg 6 — utviklingsarbeid framover

Når vi utvikler en funksjon:

1. Godkjenn eller oppdater tilhørende `.md`-spesifikasjon.
2. Opprett en egen arbeidsgren i GitHub Desktop, for eksempel `feature/001-profilformat`.
3. Gjør små, tydelige endringer i VS Code.
4. Test endringen (senere automatiserte tester og byggetester).
5. **Commit** med beskrivende melding. **Push origin** til GitHub.
6. Opprett eventuelt en **Pull Request** på GitHub, gjennomgå endringene og slå dem sammen til `main`.
7. **Fetch origin/Pull origin** på den andre maskinen når du skal jobbe der.

Vi trenger ikke begynne med alle funksjonene i GitHub Issues/Projects. En enkel arbeidsgren per funksjon og en `produktbacklog.md` er nok i første runde.

## Når GitHub Desktop eller VS Code viser noe uventet

- Ser du `No local changes` før ZIP-filene er kopiert? Sjekk at du limte dem inn i **repo-mappen**, ikke i en undermappe ved siden av.
- Har du opprettet et repo både på GitHub og lokalt? Bruk **Clone repository** på det eksisterende, ikke et ekstra repo.
- Kan du ikke åpne `.md`? Det er vanlige tekstfiler, og VS Code kan lese dem uten tillegg.
- Spør VS Code om å kjøre ukjente scripts? Avslå fram til vi vet hva de gjør.
- Ser du en konflikt ved push? Ikke slett noe. Undersøk om GitHub-repoet allerede hadde endringer; hent først, og løst konflikten kontrollert.

## Hvordan vi bruker ChatGPT videre

- **Vanlig chat:** Krav, faglige beslutninger, forslag, kodegjennomgang og feilsøking.
- **GitHub-repo:** Autoritativ kopi av godkjente `.md`, kildekode og tester.
- **VS Code:** Lokalt utviklingsmiljø.
- **GitHub Desktop:** Kontrollerer hvilke endringer som sendes til GitHub.
- **Valgfri GitHub-tilkobling i ChatGPT:** Kan etter godkjenning gi mer direkte samarbeid med repoet, dersom tilkoblingen tilbyr nødvendige skrivehandlinger. **VS Code-installasjonen alene gir ikke ChatGPT tilgang til repoet.**

Det er helt greit å bytte mellom Windows og Mac. Begynn med Windows 10-maskinen du har foran deg. Når vi skal lage Mac-installer, trenger vi tilgang til et macOS-byggmiljø, lokalt eller gjennom en kontrollert CI-jobb.
