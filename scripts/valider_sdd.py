#!/usr/bin/env python3
"""Kontroll av SDD-baseline uten tredjepartsavhengigheter.

Dette er kun metadata-/eksempelfilkontroll. Gir IKKE garanti for
migreringslogikk eller sikkerhet i en fremtidig applikasjon.
"""
from pathlib import Path
from uuid import UUID
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'produktbacklog.md', 'beslutningslogg.md',
    'standards/prosjektkonstitusjon.md',
    'standards/sikkerhet-og-leveransekvalitet.md',
    'specs/001-stemmetest-profil/spec.md',
    'kontrakter/voiceprofile-format.md',
    'kontrakter/voiceprofile-eksempel.json',
    'tester/akseptansetestmatrise.md',
    '.gitignore',
]
PRIVATE_ENDINGS = ('.voiceprofile', '.mp3', '.wav', '.flac', '.m4a',
                   '.aac', '.ogg', '.sqlite', '.sqlite3', '.db', '.p12',
                   '.pfx', '.key', '.pem')

def verify():
    missing = [f for f in REQUIRED if not (ROOT / f).is_file()]
    if missing:
        raise ValueError('Mangler obligatoriske spesifikasjonsfiler: ' + ', '.join(missing))
    j = json.loads((ROOT/'kontrakter/voiceprofile-eksempel.json').read_text(encoding='utf-8'))
    if j.get('formatMajor') != 1 or j.get('formatMinor') != 0:
        raise ValueError('Eksempelprofilen må ha formatversjon 1.0')
    UUID(j['profileId'])
    if not isinstance(j.get('sessions'), list):
        raise ValueError('sessions må være liste')
    if not isinstance(j.get('extensions'), dict):
        raise ValueError('extensions må være et objekt')
    session_ids = set()
    for ses in j['sessions']:
        sid = str(UUID(ses['sessionId']))
        if sid in session_ids:
            raise ValueError('Duplisert sessionId')
        session_ids.add(sid)
        if not isinstance(ses.get('observations'),list):
            raise ValueError('observations må være liste')
        for obs in ses['observations']:
            UUID(obs['observationId'])
            features = obs.get('audioFeatures', {})
            if features and (not isinstance(features,dict) or
                not isinstance(features.get('algorithm'), dict)):
                raise ValueError('Ugyldig audioFeatures/algorithm')
    # Kontroll av indekserte filer, ikke bare filene i arbeidsmappen.
    r = subprocess.run(['git','ls-files','-z'], cwd=ROOT,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode == 0:
        files = [name.decode('utf-8', errors='replace')
                 for name in r.stdout.split(b'\0') if name]
        flagged = [f for f in files if f.lower().endswith(PRIVATE_ENDINGS)]
        if flagged:
            raise ValueError('Mulig privatdata/nøkkel funnet i Git-indeksen: '+', '.join(flagged))
    print('OK: SDD-baseline og syntetisk profildata er validert.')
    print('OBS: App-bygg, stemmeanalyse og profil-migrering testes ikke i denne fasen.')

if __name__ == '__main__':
    try: verify()
    except (ValueError,KeyError,TypeError,json.JSONDecodeError) as exc:
        print(f'FEIL: {exc}',file=sys.stderr)
        sys.exit(1)
