# Spesifikasjon 001: Veiledet stemmetest og portabel profil

**Status:** Utkast v0.2  
**Avhengigheter:** APP-001–002, VOX-001–010, PRF-001–004, SEC-001–005  
**Prioritet:** Første vertikale funksjonsleveranse

## 1. Mål og verdi
En bruker skal kunne starte en lokal app, gi mikrofontillatelse, følge en sikker og forståelig test for komfortabelt sangregister, se resultat og lagre/eksportere en profil som kan importeres på annen plattform. Ingen internettforbindelse eller innlogging er nødvendig.

## 2. Ikke-mål
- Appen er ikke et medisinsk stemmediagnoseverktøy.
- Den skal ikke fastsette stemmetype (tenor, alt osv.) automatisk.
- Den skal ikke konkludere om sangteknikk eller utholdenhet ut fra tonehøyde alene.
- Den skal ikke lagre eller dele rå mikrofonopptak.
- Automatisk sangtilpasning fra MP3 inngår ikke.

## 3. Begreper
- **Grunnfrekvens (F0):** Estimert frekvens for sunget tone.
- **Cent:** 1/100 av en halvtone; positivt avvik betyr høyere enn referansen.
- **Komfortabelt register:** Området av toner sangeren både mestrer målemessig og selv vurderer som komfortabelt i testsituasjonen.
- **Utvidet register:** Observerte toner utenfor komfortområdet; brukes ikke som automatisk anbefalingsgrunnlag.
- **Konfidens:** Indikator på hvor pålitelig den tekniske målingen er, ikke medisinsk sikkerhet.

## 4. Brukerflyt
1. Start app offline → velg «Opprett profil» eller eksisterende profil.
2. Velg «Test stemmen min» → informasjon om test, frivillighet og stopp.
3. Velg mikrofon → gi OS-tillatelse → test inngangsnivå og bakgrunnsstøy.
4. Appen spiller en behagelig referansetone → brukeren synger den → måling vises.
5. Trinnvis utforsking av nedre og øvre register; komfortvurdering etter prøver.
6. Ved dårlig måling: forsøk på nytt, bytt mikrofon eller hopp over.
7. Appen oppsummerer laveste/høyeste komfortable tone, usikkerhet og testdato.
8. Brukeren lagrer eller forkaster → kan senere eksportere én profilfil.

## 5. Funksjonelle regler
- FR-01: Profilnavn er valgfritt; intern UUID identifiserer profil og sesjoner.
- FR-02: OS-mikrofontillatelse innhentes først ved testoppstart, ikke ved applikasjonsstart.
- FR-03: Måling skal filtrere bort ikke-tonale/svake signaler, og vise «usikker» ved utilstrekkelig kvalitet.
- FR-04: Målealgoritme og versjon lagres per testsesjon.
- FR-05: Et teststeg godkjennes bare når både signalmåling og eksplisitt komfortvurdering oppfyller krav.
- FR-06: «Ubehagelig / stopp» avslutter aktuell retning; brukeren kan avbryte hele testen.
- FR-07: Appen forsøker å verifisere en grensetone på nytt før resultatet blir endelig.
- FR-08: Et nytt resultat legges til historikken, og erstatter aldri eldre resultat uten eksplisitt handling.
- FR-09: Profil skal vises som noter med oktav og som spenn i halvtoner.
- FR-10: Import skal aldri automatisk erstatte en eksisterende profil med samme UUID.
- FR-11: Appen sender ingen testlyd eller profildata til internett.

## 6. Målemodell – startparametere som må valideres
Dette er **prototypehypoteser**, ikke ferdig aksepterte medisinske eller musikalske grenser:
- Tonehøydeanalysen skjer fortløpende lokalt, i for eksempel 20–50 ms analysehopp.
- Etter at brukeren synger en referansetone, beregnes stabilitet over en sammenhengende periode, for eksempel 1,0–1,5 sekund.
- Kandidat for «truffet tone» kan starte med toleranse ±50 cent, men må testes mot faktiske mikrofoner, vibrato og brukeropplevelse.
- Ikke mål bare høyeste/laveste registrerte enkeltframe: robust registrering over tid og gjentatt bekreftelse kreves.
- Avspillingslyd kan lekke inn i mikrofonen. Anbefal hodetelefoner og legg inn et stille målevindu etter referansen.
- Registeralgoritmen skal ikke anta kjønn, stemmefag eller alderskategori.

## 7. Akseptansescenarier (Gherkin)

### S1 – Start uten internettilgang
**Gitt** at applikasjonen er installert og nettverk er deaktivert, **når** brukeren starter appen og oppretter en profil, **så** kan brukeren starte en stemmetest uten nettilgang eller innlogging.

### S2 – Mikrofontillatelse nektes
**Gitt** at mikrofontillatelse ikke er gitt, **når** brukeren forsøker å teste, **så** får brukeren forklaring og kan prøve igjen uten at appen krasjer eller lagrer falske resultater.

### S3 – Ugyldig tone / støy
**Gitt** at bakgrunnsstøyen hindrer sikker tonebestemmelse, **når** et teststeg måles, **så** merkes steget «usikker» og godkjennes ikke.

### S4 – Komfort er avgjørende
**Gitt** at en tone måles med god presisjon, **når** brukeren markerer «Ubehagelig / stopp», **så** registreres den ikke som del av komfortregisteret.

### S5 – Normal fullføring
**Gitt** at brukeren har gjennomført gyldige nedre og øvre testtrinn, **når** testen fullføres, **så** vises komfortabelt register med note og oktav, testdato og indikasjon på målekvalitet.

### S6 – Avbrutt test
**Gitt** at en testsesjon pågår, **når** brukeren velger «Stopp», **så** stanses mikrofon og referanselyd, og et eventuelt ufullstendig resultat overskriver ikke forrige profilresultat.

### S7 – Eksport/import Windows → Mac
**Gitt** at en profil er eksportert fra Windows til én `.voiceprofile`-fil, **når** den importeres på macOS med samme profilskjemaversjon, **så** er profilidentitet, register, historikk og innstillinger uendret.

### S8 – Eksport/import Mac → Windows
**Gitt** at en profil er eksportert fra macOS, **når** den importeres på Windows, **så** gjelder samme resultat som S7.

### S9 – Eksisterende profil
**Gitt** at importert UUID finnes lokalt, **når** import startes, **så** spør appen om kopi eller avbrudd og overskriver ikke taushetsfullt.

### S10 – Manipulert profilfil
**Gitt** en feilformatert, overstor eller manipulert fil, **når** den importeres, **så** avvises den kontrollert uten kodekjøring, uønskede filoperasjoner eller tap av eksisterende profiler.

## 8. Kvalitetsmål / verifikasjon
- K-01: Ingen nettverksforbindelse kreves for stemmetest eller profilflytting.
- K-02: Windows 10/11 og macOS verifiseres med manuelt installasjons- og mikrofonløp; nøyaktig macOS-støtte fastsettes ved avhengighetsgodkjenning.
- K-03: Akseptansetestene S1–S10 er grønne før første MVP merkes «ferdig».
- K-04: En kontrollert tonesignalkilde benyttes til automatiske tester av tonegjenkjenning (inkl. stillhet, støy og oktavfeil).
- K-05: Rålyd registreres ikke til fil og er ikke en del av profilens eksport.
- K-06: Ressursbruk, latenstid og signalgrenser måles på en faktisk Windows 10-maskin og en Mac før endelige terskelverdier låses.

## 9. Åpne avklaringer for implementeringsplanen
- Eksakt audiobibliotek/metode for F0-måling og signalrens.
- Prøvemålinger for toneområde, signalstyrke og terskler på praktiske mikrofoner.
- Minimumsstøttet macOS-versjon og maskinarkitektur (Apple Silicon/Intel).
- Om import skal tilby sammenslåing i v0.2 eller bare kopi/avbryt (anbefalt kopi/avbryt).
- Om eksporformatet skal ha komprimering (anbefalt ja) og maksimal størrelse (foreslått 2 MB for profildata uten lyd).


## 10. Endringer i v0.2: Testen skal beskrive mer enn bare register

**Første vertikale MVP (P0)** omfatter tre uavhengige dimensjoner:

1. Komfortabelt toneområde: nedre og øvre toner bekreftet med måling og egenvurdering.
2. Intonasjon og stabilitet: avvik fra referansetone, tidsvariasjon/robust F0 og målekvalitet.
3. Kontrollert tonevarighet: hvor lenge en komfortabel tone kan synges stabilt i en kort, avgrenset oppgave.

**Senere P1:** Frasering og pauser, vokaler/resonans og egenvurdert registerovergang. **P2:** Pedagogisk 2D/3D-modell av hals/tunge/stemmebånd. **P3:** Gamifisert øving utover tonehøyde.

### Oppdaterte funksjonsregler

- FR-12: Hver gyldig observasjon knyttes til oppgavetype, testmetode, instrument-/algoritmeversjon, sample rate, kvalitetsmetadata og explisitte enheter.
- FR-13: Målt akustikk, egenvurdert komfort/innsats og modellert anatomi behandles som tre forskjellige datakategorier.
- FR-14: Signaltrekk (for eksempel kompakte F0-tidsserier, RMS-proxy og voiced-andel) lagres innenfor dokumentert størrelsesgrense. **Ingen rå lyd** lagres i MVP.
- FR-15: Profilens format leses gjennom kontrakten i `kontrakter/voiceprofile-format.md`; nye appversjoner må migrere historiske stabile profilformater.
- FR-16: Uforståelig fremtidig major-format eller ukjent required-feature avvises uten datatap.
- FR-17: Normal kjøring og alle stemmetest-/profilhandlinger krever ikke lokale administratorrettigheter.
- FR-18: Brukeren skal aldri presses til maksimal varighet eller ubehagelige toner for å «bestå». Modulen skal ikke diagnostisere sykdom, stemmeknuter, muskelspenning, pustestøtte eller stemmebåndenes tilstand.

### Nye akseptansescenarier (Gherkin)

**S11 – Versjonsovergang**: Gitt en gyldig profil fra en tidligere stabil versjon, når ny app importerer den, så skal kjent historikk bevares, ukjent være ukjent og originalfilen forbli uendret.

**S12 – Nyere profilfil**: Gitt en ukjent framtidig major-formatversjon, når appen åpner den, så skal den avvise skriving/import og forklare hvordan data kan åpnes uten tap.

**S13 – Ikke destruktiv framtidig minor**: Gitt et ukjent valgfritt felt i en nyere kompatibel fil, når appen håndterer den, så skal feltet bevares gjennom round-trip eller filen forbli read-only, aldri miste feltet lydløst.

**S14 – Ingen admin i drift**: Gitt en standardbrukerkonto, når appen startes, mikrofontester, lagrer, eksporterer og importerer, så forekommer ikke UAC-prompt, sudo eller root.

**S15 – Tonevarighet og stabilitet**: Gitt en kort, komfortabel sangtone, når brukeren fullfører testen, så lagres varighet, gyldig voiced-andel, stabilitet og målekvalitet som forskjellige størrelser, uten påstander om fysiologisk pustestøtte.

**S16 – Avledning ikke lik observasjon**: Gitt en test fra en eldre metodeversjon, når en ny analyseversjon innføres, så bevares de opprinnelige resultatene og nye tolkninger får egne metodeidentifikatorer.

**S17 – Anatomi er opplæring**: Gitt en framtidig anatomiillustrasjon, når brukeren ser modellen, så merkes tunge, stemmebånd og luftveier eksplisitt som illustrert/estimert fremfor observert, med forklaring om at mikrofonen ikke måler dem direkte.

**S18 – Mikrofondata forblir lokale**: Gitt en hel stemmetest, når nettverket er på, så finnes ingen skjulte opplastinger eller telemetri. Bare brukerinitiert eksport lager en lokal fil.

### Verifisering før faktisk kode

- Oppdater testmatrisen; gjennomfør syntetiske testsignaler, Win/Mac-filutveksling, inn-/utpakking av ubetrodde profiler, og standardbrukertest.
- Spesifikasjonen endres ikke automatisk av AI-agenten i implementeringen. Uavklarte terskelverdier skal forbli eksplisitte inntil prototypetester gir grunnlag for dem.
