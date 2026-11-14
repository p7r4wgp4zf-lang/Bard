# `.voiceprofile` — formatkontrakt v0.2 (forslag)

> **Retning, ikke ferdig standard.** Kontrakten skal godkjennes før produksjonsdata opprettes. Syntetisk JSON-eksempel finnes i `voiceprofile-eksempel.json`.

## 1. Hva betyr bakoverkompatibilitet?

- **Bakoverkompatibilitet:** En ny appversjon kan importere **alle historiske stabile profilversjoner** ved å lese dem direkte eller kjøre dokumenterte, testede migreringer.
- **Foroverkompatibilitet:** Eldre app skal ikke miste data ved møte med nyere profil. Det er *ikke* et løfte om at en eldre app kan forstå eller redigere fremtidige funksjoner.
- **Skrivepolicy:** Bare gjeldende format skrives ved ny eksport; migrering er tapsfri for de data som var tilgjengelige. Original fil endres aldri.
- **Ukjent obligatorisk funksjon:** Avvis skrive-/importforsøk med tydelig forklaring og krav om nyere app.
- **Ukjent valgfritt felt:** Bevar råverdi ved lagring/eksport **dersom** appversjonen støtter korrekt round-trip. Hvis ikke: importer kun som lesbar forhåndsvisning uten omskriving.
- **Retensjon:** Manglende data fra gamle tester skal forbli `null`/`not-measured`, ikke syntetiseres. Historiske prøver bevares som eget revisjonsspor.

## 2. Versjonsnummer og konvensjoner

- `formatMajor`: heltall (starter på 1). Økes ved inkompatibel filstruktur/semantikk.
- `formatMinor`: heltall (starter på 0). Økes ved additive, ikke-brytende endringer.
- `testMethod.id` og `testMethod.version`: angir testprotokoll, ikke filformat.
- `algorithm.name`, `algorithm.version` og `algorithm.configHash`: kan sammenligne tolkninger.
- `sourceRecordSchemaVersion`: versjon for registrerte observasjoner.
- `createdAt` og `exportedAt`: UTC ISO-8601.
- `uuid` brukes for profil, sesjon og observasjoner. Oppdatering ved konflikt skjer aldri lydløst.
- `extensions` er navnerom (f.eks. `org.example.articulation`) med dokumentert størrelse og schema. Ukjent innhold er passiv JSON uten URL-/kodeutførelse.

Semantisk versjonering av appen og av datakontrakten er **ikke samme ting**.

## 3. Filstruktur

```text
MinProfil.voiceprofile  (ZIP)
├── manifest.json
└── profile.json
```

Tillatte oppføringer er disse to (første format). ZIP-filnavn må være eksakte, entydige og normaliserte. Ingen absolutte stier, `..`, symlinker, kjørbare elementer, ukjente filer, eksterne referanser eller dynamisk innhold.

`manifest.json` inneholder `formatMajor`, `formatMinor`, `exportedAt`, `appVersion`, `requiredFeatures` og SHA-256 for `profile.json`. Hash gir integritetssjekk, **ikke** bevis for signert utgiver eller beskyttelse mot en angriper som endrer både JSON og hash.

`profile.json` inneholder identitet, preferanser og `sessions[]`. Alle tall oppgis med eksplisitte enheter og inkluderer `null` når verdier ikke er målt.

## 4. Feltfamilier som tåler fremtidig utvidelse

| Feltfamilie | Registreres i v1? | Hensikt |
|---|---|---|
| `profileId`, `sessionId`, dato, protokollversjon | Ja | Historikk og sammenlignbarhet |
| `targetMidi`, `referenceFrequencyHz`, `measuredF0Hz`, `midi`, `centDeviation` | Ja når målt | Grunnlag for intonasjon |
| `f0Series`/utvalgte F0-frame-trekk med tidsstempler og confidence | Valgfritt/bundet antall | Senere algoritmesammenligning og spillmekanikker |
| `voicedFraction`, `durationMs`, `stableDurationMs`, `rmsDbFS` | Ja når målt | Utholdenhet, stabilitet, signalnivå |
| `noiseFloorDbFS`, `clipping`, device/samplerate, frame/hop | Ja når tilgjengelig | Datakvalitet; unngå feil konklusjoner |
| `comfort`, `perceivedEffort`, `registerModeSelfReport`, `vowelPrompt` | Valgfritt | Subjektiv kontekst og vokaløvelser |
| `pitchDrift`, `pitchVariability`, onset metrics, phrase breaks | Avledet når metode finnes | Progresjon og frasering |
| `formants`/LPC/spektrale mål | Bare P1+ med kvalitet og metodeversjon | Framtidig vokalanalyse – **ikke** fysisk tungekartlegging |
| `anatomicalModelEstimate` | Bare P2+ | Estimat for illustrasjon, aldri medisinsk/fysisk observasjon |
| `rawAudioPath`, `rawAudioBytes` | **Nei** | Råopptak inngår ikke i profilen i MVP |

`rmsDbFS` er digitalt referert signalnivå og skal ikke omtales som kalibrert lydtrykknivå (dB SPL).

## 5. Kompatibilitetsregler og migrering

1. Les manifest og sjekk størrelsesgrense, allowlist, schema og requiredFeatures.
2. Sjekk `formatMajor`; importer støttet major eller kjør eksplisitt migreringskjede.
3. Valider alle JSON-filer, feltgrenser, Unicode-normalisering og hash.
4. Les filen inn i en isolert, ikke-aktiv mellomstruktur.
5. La brukeren forhåndsvise profilidentitet, sesjoner og migreringskonsekvenser.
6. Hvis UUID finnes: velg avbryt, kopi eller senere en kontrollert sammenslåing.
7. Migrer atomisk til lokal SQLite innenfor én transaksjon. Ved feil: rollback. Bevar importfilen uendret.
8. `legacy/v0.1` eksempel kan mangle rå observasjoner. Migreringen skal fylle **ukjent** som ukjent, ikke finne på målinger.

**Testmatrise:** Samme fil må være identisk mht. historikk og UUID etter Win→Mac og Mac→Win; testsamling må også omfatte v0.1, v1.0, framtidig 1.x med ukjente valgfrie felter, framtidig ukjent 2.x, korrupte og overstore arkiv.

## 6. Importgrenser (første foreslåtte verdier)

- Maks komprimert arkiv: **5 MiB**.
- Maks samlet dekomprimert innhold: **20 MiB**.
- Maks antall ZIP-oppføringer: **2**.
- JSON-resursgrenser: maksimalt antall sesjoner/observasjoner og nesting må fastsettes i skjema og parser.
- Null nettverkskall og null sideeffekter ved preview/import, unntatt eksplisitt databaseinnlegging etter samtykke.

Disse grensene er *forslag* og skal revideres hvis vi lagrer kompakte akustiske tidsserier. Ingen automatiske interne ZIP-uttrekk til filsystemet er nødvendige.

## 7. Viktig kompromiss

Ved ikke å lagre rå lyd kan vi ikke reanalysere gamle opptak med en helt ny spektral algoritme. Vi lagrer derfor et bevisst utvalg av kompakte signaltrekk. Hvis senere funksjoner krever egenskaper vi ikke har, gjennomfører brukeren en ny test eller aktiverer et separat, eksplisitt samtykkebasert lokalt opptak.
