# Akseptanse- og kompatibilitetstestmatrise v0.2

| ID | Test | Forventet resultat | Prioritet |
|---|---|---|---|
| T-01 | Start offline med standard Windows-bruker | App starter uten adminprompt, konto eller nettverkskrav | P0 |
| T-02 | Start offline med standard macOS-bruker | App starter uten root/sudo eller konto | P0 |
| T-03 | Mikrofontillatelse avslås | Tydelig feil, ingen falske resultat, mikrofon stengt | P0 |
| T-04 | Syntetisk A4=440 Hz pluss støy | F0 gjenkjennes eller merkes usikker innenfor testet toleranse | P0 |
| T-05 | Vibrato og oktavfeil i signalet | Usikre frames godkjennes ikke, måleresultat sporer algoritme | P0 |
| T-06 | Bruker markerer ubehag | Tonen inkluderes ikke i komfortabelt område | P0 |
| T-07 | Stopp midt i test | Innhenting og referanselyd stopper; tidligere historikk beholdes | P0 |
| T-08 | Gjennomfør og lagre test | F0 og målemetode knyttes til egen session og observasjoner | P0 |
| T-09 | Eksport Win→Mac; import | Samme UUID, antall sesjoner, målte verdier og user reports | P0 |
| T-10 | Eksport Mac→Win; import | Samme som T-09 | P0 |
| T-11 | Import eldre stabil versjon (testfixture) | Migrering uten tap, ukjent forblir ukjent | P0 |
| T-12 | Import fremtidig minor med ekstra frivillig felt | Felt bevares ved round-trip, eller filen åpnes bare i read-only | P0 |
| T-13 | Import fremtidig ukjent major/required feature | Avvis sikker skriving, forklar behov for nyere app | P0 |
| T-14 | ZIP-bombe, traversal, symlink, duplikatnavn | Avvis uten kodekjøring, ingen DB-/filendring | P0 |
| T-15 | Import UUID-konflikt | Ingen stille overskriving; brukeren velger håndtering | P0 |
| T-16 | Oppgradering av analysealgoritme | Historiske målinger beholdes uendret med original versjon | P0 |
| T-17 | Feil når import nesten er fullført | Transaksjon rollback, originalfil og profil uskadd | P0 |
| T-18 | Kontroller UAC-/sudo-spørringer ved normal kjøring | Ingen; ethvert avvik blokkerer release | P0 |
| T-19 | Avinstallering og datarettigheter | App avinstalleres kontrollert; profilhåndtering dokumentert | P0 |
| T-20 | Installer fremfor standardbruker | Per-user Windows-installer uten UAC når OS-forutsetninger er oppfylt | P0 |
| T-21 | Test fonasjon og sustain | Lengde/stabilitet måles separat, ikke forvekslet med fysisk pustestøtte | P1 |
| T-22 | Pedagogisk 3D-modell | Skiller alltid målt, estimert og simulert | P2 |

**Release-gate:** Alle P0-scenarier skal bestå på definerte testplattformer. Unntak krever dokumentert beslutning, risikoaksept og signert testresultat.
