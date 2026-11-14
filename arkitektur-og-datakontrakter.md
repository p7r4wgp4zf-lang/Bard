# Arkitektur og datakontrakter — v0.2

## Arkitekturprinsipper

1. **Local-first:** Ingen server, konto, sky, telemetri eller nettverk kreves for test, lagring og profilutveksling.
2. **Samme kodebase:** React/TypeScript med Tauri 2. Kompiler Windows- og macOS-artefakter på respektive plattformer/byggmiljøer.
3. **Prosessprivilegier:** Vanlig kjøring med standardbrukertoken. Aldri UAC-oppheving, root, driverinstallasjon eller systemtjenester ved oppstart eller daglig bruk.
4. **Dataseparasjon:** SQLite er intern lokal lagring; `.voiceprofile` er det **offentlige, stabile utvekslingsformatet**. Ingen eksponering av DB-filen som delingsformat.
5. **Historiske observasjoner er uforanderlige:** Reviderte algoritmer legger til nye analyser eller nye sesjoner; de skriver ikke om gamle måleresultater.
6. **Kompatibilitet:** Nye versjoner leser gamle profiler via eksplisitte migreringssteg. Ukjente fremtidige obligatoriske felter avvises uten datatap; valgfrie ukjente felter bevares ved round-trip når formatet tillater det.
7. **Samtykke og minimal lagring:** Kompakte signaltrekk og testmetadata kan lagres. Råopptak er avslått som standard og krever særskilt, informert samtykke om de noen gang innføres.
8. **Analyse er ikke diagnose:** Ikke utgi akustiske analyser som målinger av larynxspenning, lufttrykk, fysiologisk pustestøtte, faktisk tungeposisjon eller stemmebåndenes bilder.
9. **Kildekode og kontroll:** Vurder og lås tredjepartsavhengigheter. Ikke inkorporer tilfeldige GitHub-repoer automatisk selv om de er offentlig tilgjengelige.

## Moduler

| Modul | Ansvar | Standard |
|---|---|---|
| UI/Presentasjon | Veiledning, tonevisning, diagram, tilgjengelighet, personvernvalg | React/TypeScript |
| Audio Capture | Mikrofontillatelse, OS-enhetsvalg, buffering i minne | Tauri/WebView2 / plattform-API, testet |
| Signal Analysis | F0 (Hz), cents, stabilitet, signal quality, tidsserier | Egen versjonert grenseflate |
| Voice Assessment | Sammenstiller algoritmedata og brukerens komfortvurderinger | Versjonerte regler |
| Profile Service | Historikk, import, eksport, migrering, hash og schema | JSON-kontrakter |
| Local Store | SQLite-transaksjoner og lokale appinnstillinger | SQLite |
| Educational Visualizer | Framtidig pedagogisk anatomimodell | Separat modul, ikke P0 |
| Music & Guitar | Framtidige MP3-filer, ChordPro, tab, lydtransponering | Separat modul, ikke P0 |

## Modellér observasjoner og tolkninger separat

- **Kilden:** `VoiceSession` (id, tid, versjon, oppgavetype, scenario, kalibrering, input-device, samtykkestatus).
- **Observasjonen:** `AudioObservation` (måltonen, referansefrekvens, akustiske tidsserier/aggregater, usikkerhet, signal/klipping/støynivå og algoritmeversjon).
- **Egenvurderingen:** `SelfReport` (komfort, opplevd innsats, smerte/ubehag som brukerklassifisering, registermodus hvis brukeren oppgir den; ikke medisinske diagnoser).
- **Tolkningen:** `DerivedAssessment` (komfortabelt intervall, presisjon, sustain, forbehold, analysemetode/versjon, datakilder).
- **Profilen:** `VoiceProfile` (UUID, visningsnavn, metadata, testhistorikk, innstillinger, preferanser og opsjonelle framtidige navneromsutvidelser).

Prinsippet «lagre mer enn vi viser» gjelder **beregnede/utledede features**, ikke hemmelig rålydopptak. Ønskede framtidige analysemuligheter kartlegges som et bevisst sett med versjonerte, bounded felt: typisk tidsserier for F0, RMS/proxy for styrke, voiced/confidence samt respons på oppgaver. Slike data gir ikke mulighet til å beregne enhver framtidig akustisk egenskap: da må det være lov å tilby en ny test eller eksplisitt lokalt lydopptak i en seinere versjon.

## Filformat og kompatibilitet

Se `kontrakter/voiceprofile-format.md`. `voiceprofile` inneholder ikke operativsystemavhengige enhets-ID-er/stier eller lydfiler, og behandles som **ubetrodd data** ved import. Manifest har versjonering og checksums, filstørrelsesgrenser og filnavn-allowlist.

## Lyd og analysemotor

- Start med robust monofon tonehøydeanalyse (F0). Evaluer YIN eller tilsvarende, krev tester med støy, vibrato, flere harmoniske og oktavfeil.
- Registrer sample rate, kanalbruk, frame/hop, eventuell preprosessering, algoritmenavn + versjon, måleusikkerhet. Ingen magiske antakelser om fysisk kalibrert dB SPL uten faktisk kalibrering.
- Bruk hodetelefoner eller pauser mellom avspilt referansetone og opptak for å redusere lekkasje.
- Nye analyser implementeres som separate algoritmemoduler med egne resultatversjoner; kan sammenlignes, men ikke slåes sammen som om de var målt identisk.

## Kjøring og bygging

- Windows: Tauri NSIS `installMode: currentUser` som standard. Appbinær skal verifiseres under standardbruker; ikke forespør UAC under bruk. WebView2 er OS-avhengighet; hvis fraværende eller utdatert kan en separat, dokumentert installasjonsprosess være nødvendig. Offline-bundling kan vurderes.
- macOS: app i brukerens programområde og lokal datamappe; mikrofon-tillatelse gjennom operativsystemet, ingen root-rettighet for normal kjøring. Signering/notarisering ved ekstern distribusjon.
- Nye installasjonsavhengigheter må beskrives med leverandør, lisens, formål, hash, nødvendige rettigheter og om alternativ finnes.

## Påfølgende implementasjonsbeslutninger

- F0-algoritme og kvalitetsterskler etter måleprototypen.
- Eksakt komprimeringsmetode for tidsserier og retensjonsgrenser etter test av dataomfang og profilfilstørrelse.
- Hvilke egenskaper som skal være obligatoriske i schema v1 versus nullable/opsjonelle.
- Valg av underspesifikasjon for visning av fonasjon/resonans. Ingen tredjepartskode legges inn før lisens- og sikkerhetsgjennomgang.
