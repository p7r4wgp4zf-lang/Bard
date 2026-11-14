# Produktbacklog — brukerhistorier v0.2

**Prioritet:** P0 = første vertikale leveranse OG tverrgående sikkerhet/profilkontrakt; P1 = neste funksjonsfase; P2 = senere; P3 = idébank.  
**Format:** «Som [rolle] vil jeg [handling] slik at [verdi]». Hver historie har kontrollerbare akseptansekriterier.  
**Roller:** Lokal bruker (en person som benytter klientapplikasjonen); sanger (lokal bruker som gjennomfører stemmetest); vedlikeholder (bygger og oppdaterer appen).

## EPIK A – Oppstart og lokal bruk

### APP-001 — Kjør applikasjonen uten konto [P0]
**Som lokal bruker vil jeg starte appen uten registrering eller innlogging, slik at jeg kan bruke den privat og offline.**
- AK1: Applikasjonen starter uten nettilgang etter at nødvendige lokale kjøretidskomponenter er installert.
- AK2: Ingen skyinnlogging eller nettverkskall er nødvendig for stemmetest eller lagring.
- AK3: Brukeren kan åpne en lokal profil eller opprette en ny.

### APP-002 — Installer på Windows og macOS [P0]
**Som lokal bruker vil jeg installere samme applikasjon på Windows og macOS, slik at jeg kan bruke den på begge maskintypene.**
- AK1: Byggløpet produserer Windows-installer (.exe eller .msi) og macOS-app (.app/.dmg) fra samme kodebase.
- AK2: Et dokumentert manuelt installasjonstestløp utføres på Windows 10, Windows 11 og støttede macOS-versjoner.
- AK3: Installasjonen krever ingen konto eller proprietær tredjepartsapplikasjon ut over OS-kjøretidskomponenter.
- AK4: Eventuelle nødvendige eksterne kjøretidskomponenter kan distribueres kontrollert/offline når dette er valgt i byggoppsettet.

## EPIK B – Stemmetest (første utviklingsmål)

### VOX-001 — Opprett en personlig profil [P0]
**Som sanger vil jeg opprette en lokal profil med et valgfritt navn, slik at testresultatene kan knyttes til meg.**
- AK1: Navn er frivillig; appen kan foreslå «Min profil».
- AK2: Profilen får intern UUID og opprettelsestidspunkt.
- AK3: Ingen e-post, konto, kjønn eller fødselsdato etterspørres.

### VOX-002 — Velg og test mikrofon [P0]
**Som sanger vil jeg velge mikrofon og se at den registrerer lyd, slik at testen ikke gjennomføres med feil lydkilde.**
- AK1: Appen lister tilgjengelige mikrofoner ved innvilget tillatelse, og kan bruke systemets standardmikrofon.
- AK2: En nivåindikator responderer på lyd, og brukeren kan avbryte.
- AK3: Avslag på mikrofontillatelse og frakoblet mikrofon gir forståelige feilmeldinger og ny prøve-mulighet.
- AK4: Mikrofonen aktiveres bare etter en uttrykkelig brukerhandling og deaktiveres når testen avsluttes.

### VOX-003 — Før testen får brukeren instruksjoner [P0]
**Som sanger vil jeg få enkel veiledning før og under testen, slik at jeg forstår hva jeg skal gjøre uten å presse stemmen.**
- AK1: Testen forklarer at målet er komfortabelt register, ikke medisinsk vurdering eller maksimalprestasjon.
- AK2: Det finnes alltid «Stopp», «Hopp over» og en oppfordring om å avbryte ved ubehag.
- AK3: Appen anbefaler hodetelefoner eller lav avspillingsstyrke for å begrense tilbakekobling til mikrofonen.

### VOX-004 — Finn komfortabel nedre grense [P0]
**Som sanger vil jeg synge veiledede toner nedover, slik at appen kan anslå min laveste komfortable sangtone.**
- AK1: Hver testtone har hørbart referanseeksempel og synlig tonenavn/oktav.
- AK2: Appen krever måling med godkjent kvalitet samt brukerens egen komfortvurdering før en tone godtas.
- AK3: Når kvalitet eller komfort faller, forsøkes en kontrollmåling før grensen bestemmes.
- AK4: Manglende måling vises som «usikker/ikke målt», aldri som en antatt lav grense.

### VOX-005 — Finn komfortabel øvre grense [P0]
**Som sanger vil jeg synge veiledede toner oppover, slik at appen kan anslå min høyeste komfortable sangtone.**
- AK1: Samme måle- og komfortkrav gjelder som i VOX-004.
- AK2: Testen kan stoppes uten tap av allerede godkjente målinger.
- AK3: Resultatet skiller mellom komfortabel og eventuelt utforsket utvidet rekkevidde; ubehagelige toner regnes ikke som komfortable.

### VOX-006 — Se tonehøyde og målekvalitet [P0]
**Som sanger vil jeg se om jeg treffer tonen og om mikrofonmålingen er pålitelig, slik at jeg får forståelig tilbakemelding.**
- AK1: Appen viser estimert note og avvik i cent når målingen er gyldig.
- AK2: Støy, polyfonisk lyd, manglende grunnfrekvens eller for svakt signal blir indikert som lav kvalitet.
- AK3: Ugyldig måling gir aldri automatisk bestått resultat.

### VOX-007 — Angi hvor behagelig hver tone er [P0]
**Som sanger vil jeg selv gradere komfort på utvalgte toner, slik at registeret ikke bestemmes utelukkende ut fra hva mikrofonen oppfatter.**
- AK1: Brukeren kan velge «Komfortabel», «Krevende» eller «Ubehagelig / stopp».
- AK2: En korrekt truffet tone som oppleves som ubehagelig, godkjennes ikke som komfortabel.
- AK3: Brukeren kan rette siste komfortvurdering før testen avsluttes.

### VOX-008 — Se og lagre resultat [P0]
**Som sanger vil jeg se målt register på et enkelt piano-/notediagram, slik at jeg forstår resultatet og kan bruke det senere.**
- AK1: Nedre og øvre komfortgrense vises som note med oktav og total spennvidde i halvtoner.
- AK2: Resultatet merkes «foreløpig» dersom det bygger på for få målinger eller inneholder usikkerhet.
- AK3: Testdato, metodeversjon og pålitelighetsindikator lagres sammen med resultatet.
- AK4: Brukeren kan lagre resultatet eller forkaste testsesjonen.

### VOX-009 — Gjenta test og bevar historikk [P0]
**Som sanger vil jeg gjenta testen og sammenligne tidligere resultater, slik at jeg kan følge endringer over tid.**
- AK1: Ny test oppretter en ny sesjon uten å skrive over tidligere sesjoner.
- AK2: Resultatsiden viser siste godkjente måling og tidligere målinger med dato.
- AK3: Brukeren kan slette en enkelt testsesjon.

### VOX-010 — Avbryt og håndter avbrudd [P0]
**Som sanger vil jeg avbryte eller gjenoppta der det er forsvarlig, slik at feil ikke gjør appen ubrukelig.**
- AK1: «Stopp» stanser referanselyd og mikrofoninnhenting umiddelbart.
- AK2: Ved mikrofonfrakobling eller tilgangstap markeres sesjonen ufullstendig.
- AK3: Ufullstendig måling skal aldri overskrive en gyldig profil automatisk.

## EPIK C – Portabel og personstyrt profil

### PRF-001 — Eksporter profilfil [P0]
**Som lokal bruker vil jeg lagre stemmeprofilen som én fil jeg selv velger plassering for, slik at jeg kan ta den med mellom PC og Mac.**
- AK1: Eksport via «Lagre profil som…» gir én `.voiceprofile`-fil.
- AK2: Filen inneholder formatversjon, profilidentitet, testhistorikk og innstillinger som er nødvendige for å bruke profilen.
- AK3: Rå mikrofonopptak tas ikke med; første versjon lagrer ikke råopptak.
- AK4: Brukeren kan velge målmappe og kopiere filen med vanlig filbehandling.

### PRF-002 — Importer profilfil på annen plattform [P0]
**Som lokal bruker vil jeg importere en profilfil fra et annet operativsystem, slik at jeg slipper å gjennomføre stemmetesten på nytt.**
- AK1: Fil eksportert på Windows kan importeres på Mac og omvendt uten dataendring.
- AK2: Import fungerer offline.
- AK3: Validering gir forståelig melding ved feil format eller filversjon.

### PRF-003 — Håndter duplikater og ugyldige filer [P0]
**Som lokal bruker vil jeg få kontroll ved import, slik at jeg ikke utilsiktet mister resultater eller åpner farlige filer.**
- AK1: Eksisterende UUID fører til valg mellom avbryt, opprett kopi og kontrollert sammenslåing hvis støttet.
- AK2: Original profil og fil bevares hvis import avbrytes eller feiler.
- AK3: Import avviser eksekverbart innhold, ugyldige felter, path traversal og filer over fastsatt størrelsesgrense.
- AK4: Programmet utfører aldri instrukser fra profilfilen.

### PRF-004 — Slett lokale data [P0]
**Som lokal bruker vil jeg kunne slette profil og historikk, slik at jeg kontrollerer hvilke data som ligger igjen på maskinen.**
- AK1: Bruker må bekrefte sletting med tydelig konsekvensbeskrivelse.
- AK2: Applikasjonen fjerner egne lokale databaseoppføringer og lagrede sesjonsdata for profilen.
- AK3: Eksporterte kopier utenfor applikasjonens lagringsområde berøres ikke, og det forklares til brukeren.

### PRF-005 — Flere familiemedlemmer [P1]
**Som lokal bruker vil jeg kunne ha flere separate profiler uten pålogging, slik at flere personer kan bruke samme installasjon.**
- AK1: Hver profil har egen testhistorikk og egne innstillinger.
- AK2: Bytte mellom profiler kan gjøres uten nettverk eller passord.

## EPIK D – Musikk og gitar (neste utviklingsfaser)

### MUS-001 — Importer egne MP3-filer [P1]
**Som gitarist vil jeg legge til egne MP3-filer i biblioteket, slik at jeg kan spille dem uten strømmetjeneste.**
- AK1: Brukeren velger filer eller mapper fra lokal disk.
- AK2: Filer indeksers uten å endre originalene; ødelagte filer håndteres med feilmelding.
- AK3: Biblioteket fungerer offline.

### MUS-002 — Spill av musikk lokalt [P1]
**Som gitarist vil jeg starte, pause og søke i en sang, slik at jeg kan øve på bestemte deler.**
- AK1: Avspilling har start/pause/stopp, tidslinje og volumkontroll.
- AK2: MP3-filens opprinnelige innhold endres ikke ved avspilling.

### MUS-003 — Transponer akkorder [P1]
**Som gitarist vil jeg flytte tonearten på et akkordark og justere capo, slik at jeg kan velge gitarvennlige grep.**
- AK1: Alle akkorder, inkludert moll og slash-akkorder, transponeres korrekt innenfor 12-tonesystemet.
- AK2: Capo endrer grepvisning uavhengig av ønsket klingende toneart.
- AK3: Originalutgaven kan gjenopprettes uten datatap.

### MUS-004 — Transponer lyd uten å endre tempo [P1]
**Som sanger vil jeg endre tonehøyden på MP3-avspillingen, slik at musikken følger den valgte tonearten.**
- AK1: Brukeren kan velge et helt antall halvtoner innenfor et spesifisert trygt intervall.
- AK2: Tempoet forblir uendret innenfor måledefinert toleranse.
- AK3: Brukeren får varsel om redusert kvalitet ved større endringer.

### MUS-005 — Importer egne akkorder og tabulatur [P1]
**Som gitarist vil jeg importere lovlig tilgjengelige akkordark og tabs, slik at de vises sammen med sangen.**
- AK1: ChordPro støttes i første omgang; flere formater vurderes separat.
- AK2: Kilde og eventuelle bruks-/lisensopplysninger kan dokumenteres.
- AK3: Ukjent eller ugyldig filinnhold kan ikke kjøre kode.

### MUS-006 — Finn og ranger tillatte kilder [P2]
**Som gitarist vil jeg se relevante akkordversjoner fra kilder vi har lov til å bruke, slik at jeg enklere finner riktig arrangement.**
- AK1: Integrasjoner med dokumentert tillatelse/API er eneste automatiske innholdskilder.
- AK2: Manglende rating og forskjeller i ratinggrunnlag vises ærlig; «mest populær» forveksles ikke med «mest korrekt».
- AK3: Manuelt importerte versjoner kan overstyre automatiske forslag.

### MUS-007 — Foreslå toneart fra stemmeprofil [P2]
**Som sanger vil jeg få anbefalt toneart basert på mitt komfortregister og sangens faktiske meloditoner, slik at melodien passer bedre.**
- AK1: Forslaget krever kjent eller målt melodiregister; akkordrekke alene gir ikke et gyldig forslag.
- AK2: Algoritmen vurderer både min-/maksnoter og hvor mye av melodien som ligger høyt/lavt, når slike data finnes.
- AK3: Resultatet er en anbefaling som brukeren alltid kan overstyre.

### MUS-008 — Vis avansert tabulatur [P2]
**Som gitarist vil jeg lese tabulatur i et notebasert grensesnitt, slik at jeg kan lære riff og soloer.**
- AK1: Et dokumentert tab-format med testfiler vises korrekt.
- AK2: Gripebrett- og strengbegrensninger tas hensyn til ved senere transponering av tabs.

## EPIK E – Gamifisert stemmetrening (senere)

### GAME-001 — Følg en målmelodi i sanntid [P3]
**Som sanger vil jeg se hvor min tonehøyde ligger mot en målmelodi, slik at jeg kan trene intonasjon på en motiverende måte.**
- AK1: Målt tonehøyde og målmelodi vises på samme tidsakse med tydelig markering av usikre målinger.
- AK2: Målfrekvensen kommer fra eksplisitte, rettighetsklarerte note-/melodidata, ikke fra akkordene alene.

### GAME-002 — Få poeng og mestringsmål [P3]
**Som sanger vil jeg få poeng for å treffe og holde toner, slik at øvelsene oppleves som et spill.**
- AK1: Poeng beregnes fra dokumenterte kriterier som presisjon, varighet og vanskelighetsnivå.
- AK2: Ingen poeng gis for ubehagelig høyt/lavt register eller for å presse stemmen.
- AK3: Resultatene lagres per lokal profil og kan slettes.

### GAME-003 — Velg trygge treningsnivåer [P3]
**Som sanger vil jeg kunne velge øvingsnivå og pauser, slik at treningen passer erfaring og dagsform.**
- AK1: Øvelser holder seg som standard innenfor profilens komfortregister.
- AK2: Brukeren kan avbryte/ta pause når som helst.
- AK3: Etiske spillmekanikker prioriterer mestring fremfor tvangsmessig progresjon.

### GAME-004 — Lokal fremgang uten sky [P3]
**Som sanger vil jeg se egen progresjon uten nettbasert konto, slik at historikken er privat.**
- AK1: Fremgang lagres lokalt og kan inngå i profilens eksportformat etter formatoppgradering.
- AK2: Ingen lydopptak deles automatisk.

## EPIK F – Sikkerhet og vedlikehold (tverrgående)

### SEC-001 — Kontroller tredjepartsavhengigheter [P0]
**Som vedlikeholder vil jeg kunne godkjenne enhver direkte og transitiv kodeavhengighet, slik at risiko for supply-chain-angrep reduseres.**
- AK1: En avhengighetsliste dokumenterer navn, kilde, versjon, lisens, formål og begrunnelse.
- AK2: Kun versjonslåste, kontrollerte versjoner brukes i bygg.
- AK3: Nye direkte avhengigheter krever eksplisitt godkjenning; ukjente eller høy-risiko transitive avhengigheter blokkeres.

### SEC-002 — Sårbarhetssøk og reproduksjon [P0]
**Som vedlikeholder vil jeg at avhengigheter og bygg skal sjekkes automatisk, slik at feil fanges før installasjonsfilene lages.**
- AK1: Automatiske sårbarhetssøk kjøres i pull requests og ved release.
- AK2: Release knyttes til konkret kildekoderevisjon, lockfiles og SBOM.
- AK3: Release stoppes ved kritisk sårbarhet uten godkjent unntak.

### SEC-003 — Lokal personvernkontroll [P0]
**Som lokal bruker vil jeg at mikrofondata og profil aldri sendes ut av maskinen uten mitt valg, slik at jeg kan stole på appen.**
- AK1: Stemmetest fungerer med nettverk deaktivert.
- AK2: Ingen rålyd lagres eller overføres som standard.
- AK3: Applikasjonen har ikke telemetri, analyse-SDK eller skjulte nettverkskall.

### SEC-004 — Trygg import [P0]
**Som lokal bruker vil jeg kunne åpne egne profildata uten å risikere kjøring av ukjent kode, slik at deling mellom maskiner er tryggere.**
- AK1: Profilformatet tolkes utelukkende som data gjennom en streng skjemavalidering.
- AK2: Størrelsesgrenser, filtypekontroll, integritetssjekk og beskyttelse mot zip-bomber/path traversal er implementert.
- AK3: Importerte filer kan ikke laste kode, sende nettverksforespørsler eller lese andre brukerfiler på egen hånd.

### SEC-005 — Kontrollerte installasjonsartefakter [P0]
**Som lokal bruker vil jeg kunne kontrollere hvor installasjonsfilene kommer fra, slik at jeg vet hva som er installert.**
- AK1: Hvert artefakt leveres med SHA-256-sjekksum og versjonsinformasjon.
- AK2: På Mac kreves en dokumentert signerings-/notariseringsstrategi før ekstern distribusjon; intern testing kan bruke dokumentert adhoc-signering.
- AK3: Ingen uautoriserte drivere, automatiske kodeoppdateringer eller runtime-nedlastinger tas inn i distribusjonen.


## Tillegg v0.2 — nye og presiserte brukerhistorier

**Presisering om prioritet:** SEC-001–005 har allerede P0 i v0.1 og forblir P0. APP-002 skal tolkes slik at normal bruk er uten admin. VOX-004/005 er kun deler av en bredere testprofil.

### PRF-006 — Les eldre profiler ved nye versjoner [P0]
**Som bruker vil jeg at nye appversjoner alltid skal kunne lese mine gamle stemmeprofiler, slik at historikken fortsatt har verdi.**
- AK1: Eldre stabile formater kan importeres direkte eller gjennom deterministiske, testede migreringer.
- AK2: Migrering endrer ikke originalfilen; oppdaterte data legges inn transaksjonelt.
- AK3: Manglende felt markeres `not-measured`, aldri oppdiktet.
- AK4: Historiske sesjoner får beholde opprinnelige analyse- og testmetodeversjoner.

### PRF-007 — Trygg behandling av framtidige profiler [P0]
**Som bruker vil jeg at en eldre app ikke skal ødelegge en profil fra en nyere versjon, slik at oppgradering og flytting er trygg.**
- AK1: Ukjent større filformat eller ukjente obligatoriske egenskaper fører til sikker avvisning med forståelig feilmelding.
- AK2: Ukjente valgfrie felter bevares ved round-trip eller dokumentet behandles som kun-lesbart.
- AK3: Ingen stumme konverteringer eller automatisk overskriving av originalfil.

### PRF-008 — Bevar grunnlagsdata for nye analyser [P0]
**Som bruker vil jeg bevare relevante måleobservasjoner og hvordan de ble produsert, slik at senere appversjoner kan analysere utviklingen på et pålitelig grunnlag.**
- AK1: Observasjoner og avledede vurderinger lagres separat, med eksplisitte enheter, tid, oppgave, algoritme og versjon.
- AK2: En definert, begrenset mengde kompakte F0-/signal- og kvalitetsdata kan lagres; ingen rå mikrofonopptak i MVP.
- AK3: Eldre observasjoner overskrives ikke av senere algoritmer; nye analyser får ny metodereferanse.
- AK4: Begrensninger ved framtidig reanalyse dokumenteres.

### PRF-009 — Sikker, valgfri opptaksfunksjon (senere) [P2]
**Som bruker vil jeg senere selv kunne velge å lagre et kort lydopptak lokalt, slik at jeg kan høre og analysere stemmen min, men uten automatisk innsamling.**
- AK1: Opptak krever separat, tydelig opt-in; standard er avslått.
- AK2: Brukeren kan høre, eksportere og slette opptaket lokalt; det lastes ikke opp.
- AK3: Råopptak legges ikke automatisk i `.voiceprofile` og holdes atskilt fra måledata.

### VOX-011 — Mål hvor lenge en tone kan holdes kontrollert [P0]
**Som sanger vil jeg få målt varighet og tonehøydekontroll på en komfortabel tone, slik at profilen beskriver mer enn register.**
- AK1: Brukeren velger selv en komfortabel tone; testen er ikke en maksimal belastningstest.
- AK2: Varighet, voiced-andel, pitch drift og målekvalitet registreres separat.
- AK3: Resultatet omtales som kontrollert tonevarighet, ikke diagnose eller objektivt mål på pustestøtte.

### VOX-012 — Mål intonasjon og stabilitet [P0]
**Som sanger vil jeg måle hvor stabilt jeg treffer en referansetone, slik at jeg kan se om jeg forbedrer kontrollen.**
- AK1: Median toneavvik, tidsvariasjon og antall gyldige måleframes beregnes med versjonert algoritme.
- AK2: Appen skiller støy, vibrato og ustabile/ugyldige målinger; resultater med lav kvalitet merkes usikre.
- AK3: Ingen negative helse- eller teknikklapper utledes automatisk.

### VOX-013 — Registrer korte fraser og pauser [P1]
**Som sanger vil jeg øve på korte fraser og kunne se lengde, pauser og tonekontroll, slik at jeg kan arbeide med frasering.**
- AK1: Testoppgaven har kjent start og slutt; fraselengder vises uten å hevde at fysisk lungekapasitet er målt.
- AK2: Støy, klipping og lav voiced-andel påvirker konfidens.
- AK3: Historikken lagrer testoppgave og metodeversjon.

### VOX-014 — Registrer vokal- og resonansøvelser [P1]
**Som sanger vil jeg sammenligne egne vokallyder, slik at jeg kan utforske klang og artikulasjon.**
- AK1: Brukeren synger/høytaler målrettede vokaler på en komfortabel tone.
- AK2: Formant- eller spektralanalyse lagres bare med eksplisitt metode, usikkerhet og mikrofonbegrensning.
- AK3: Appen beskriver aldri akustiske proxyverdier som faktisk målt tunge- eller strupeposisjon.

### VOX-015 — Vurder overgang mellom stemmeregistre [P1]
**Som sanger vil jeg registrere opplevde registeroverganger, slik at profilen gjenspeiler hvor sang føles komfortabel og krevende.**
- AK1: Testen er valgfri, og brukeren kan angi opplevd register/overgang som egenvurdering.
- AK2: Appen utleder ikke stemmekategori eller anatomi fra tonehøyde alene.
- AK3: Eventuelle akustiske analyser holdes atskilt fra egenvurderingen.

### EDU-001 — Vis forklarende anatomi for stemmen [P2]
**Som sanger vil jeg se en pedagogisk modell av hals, tunge og stemmebånd, slik at jeg bedre forstår hvordan vokaler og toneproduksjon henger sammen.**
- AK1: Alle bevegelser merkes som **illustrasjon**, **estimert** eller **målt** etter datagrunnlag.
- AK2: Det påstås aldri at mikrofonen har målt faktisk tungeplassering eller stemmebåndbevegelse.
- AK3: Modellen kan skrus av og er ikke nødvendig for stemmetesten.
- AK4: Valg av kodebibliotek/animasjonsressurs gjennomgår lisens- og sikkerhetsreview.

### GAME-005 — Spilløvelser for mer enn tonehøyde [P3]
**Som sanger vil jeg kunne trene varighet, intonasjon og fraser i lekpregede øvelser, slik at utviklingen føles motiverende.**
- AK1: Hver øvelse oppgir hva som faktisk måles, og hva som bare er en poengmodell.
- AK2: Poeng gir ingen belønning for smerte, press eller ekstremt register.
- AK3: Øvelsene kan brukes uten konto og har egen privat lokal historikk.

### SEC-006 — Ingen administratorrettigheter ved kjøring [P0]
**Som bruker vil jeg at applikasjonen fungerer med vanlige brukerrettigheter, slik at den ikke har unødig kontroll over PC-en min.**
- AK1: Programmet fungerer under standardbrukerkonto på både Windows og macOS.
- AK2: Verken oppstart, stemmetest, lokal lagring, eksport eller import utløser UAC/sudo/root.
- AK3: Enhver framtidig funksjon som reelt trenger forhøyede rettigheter krever ny eksplisitt beslutning, forklaring og sikkerhetstest.

### SEC-007 — Begrunn alle installerrettigheter [P0]
**Som bruker vil jeg vite hvorfor installasjonen eventuelt spør om administrative rettigheter, slik at jeg kan ta informerte valg.**
- AK1: Windows-installasjon for gjeldende bruker velges som standard, uten admin der OS-forutsetningene er på plass.
- AK2: Eventuell systemomfattende installasjon eller installasjon av manglende OS-kjøretid presenteres separat med leverandør, formål og nødvendige privilegier.
- AK3: Ingen skjult driverinstallasjon eller stilltiende nedlasting av kjørbar kode.

### SEC-008 — Beskytt utviklingsrepoet mot datalekkasjer [P0]
**Som vedlikeholder vil jeg holde persondata og hemmeligheter ute av Git-repoet, slik at ikke GitHub blir et ufrivillig datalager.**
- AK1: `.gitignore` avviser ekte `*.voiceprofile`, opptak og lokalt genererte database-/nøkkelfiler.
- AK2: Syntetiske eksempeldata med egne filendelser og dokumentert fiktivt innhold kan versjoneres.
- AK3: Første repo publiseres som Private; tilgangsstyring og MFA benyttes.
- AK4: Automatiske skanninger for avhengigheter og hemmeligheter vurderes, med notering av funksjoner som eventuelt krever betalt plan.
