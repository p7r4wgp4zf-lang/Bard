# Prosjektkonstitusjon — SDD og kodeutvikling

**Gjelder fra:** SDD v0.2. Endringer i disse punktene krever en ny eksplisitt beslutning.

1. **Spec først:** Ingen implementering uten en funksjonsspesifikasjon, tilhørende brukerhistorie(r) og målbare akseptansescenarier.
2. **Brukerkontroll:** Lokal først; brukeren eier profil og eksport. Ingen konto, server eller telemetri som standard.
3. **Minste privilegium:** Applikasjonen kjører aldri som administrator/root og ber aldri om å bli det. Installasjonsunntak dokumenteres i forhåndsinformasjon.
4. **Profiler er en kontrakt:** Historiske data beskyttes. Ingen stille endring av semantikk, algoritme eller profilidentitet. Test alle støttede gamle formater mot ny programversjon.
5. **Dataminimering med nytte:** Lagre nødvendig teknisk metainformasjon, målbare features og eksplisitte egenvurderinger; ikke råopptak i MVP. Skill målt/estimert/simulert data.
6. **Ukjent er ukjent:** Manglende målinger, algoritmeusikkerhet og feil skal vises, ikke «repareres» ved å finne på plausible verdier.
7. **Trygg stemmetrening:** Ikke fremkall press, smerte eller maksimumsøk. Ingen diagnose- eller behandlingspåstander.
8. **Kontrollert kodebase:** Ikke kjør ukjent installasjonsskript, fjernkode eller plugin. Godkjenn dependencies før bruk; lås alle versjoner.
9. **Sporbarhet:** Hver feature knyttes til story-ID, spec-ID, tester og Git-commit/PR. `main` skal alltid være en godkjent baseline.
10. **Liten leveranse:** En funksjon/PR om gangen. Fritt valg av utviklingsverktøy, men ikke arkitekturendring uten beslutningslogg.
11. **Kryssplattform:** Samme datakontrakt Windows/macOS; tester i begge miljøer og installerbar pakke ved release.
12. **Sannferdig visualisering:** Anatomiske bilder kan brukes pedagogisk, men aldri merkes som direkte målinger fra lyd hvis de er beregnet/simulert.

**Instruks for AI-kodeassistent:** Følg prosjektkonstitusjon og feature-spesifikasjon. Ved konflikt mellom kode og krav: foreslå spesifikasjonsendring, ikke gjetting. Nye avhengigheter, brukerrettigheter, nettverkskall eller endringer i profilformat krever eksplisitt godkjenning og en testplan.
