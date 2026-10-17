#!/usr/bin/env python3
"""Standard-library checks for the public playbook documentation."""
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
cards = json.loads((ROOT / 'government/use-cases.json').read_text())
required = {'id', 'area', 'level', 'title', 'value', 'data', 'process', 'tools',
            'sample_output', 'risks', 'controls', 'metrics', 'dependencies', 'complexity', 'status'}
if len(cards) != 39:
    errors.append(f'Expected 39 cards, found {len(cards)}')
ids = [card.get('id') for card in cards]
if len(ids) != len(set(ids)):
    errors.append('Duplicate catalogue IDs')
areas = {card.get('area') for card in cards}
if len(areas) != 13:
    errors.append(f'Expected 13 functional areas, found {len(areas)}')
markdown = (ROOT / 'government/use-cases.md').read_text()
for card in cards:
    missing = required - card.keys()
    if missing or any(not str(card.get(field, '')).strip() for field in required):
        errors.append(f'{card.get("id")}: missing/empty fields {missing}')
    if card.get('level') not in (1, 2, 3) or card.get('status') != 'proposed':
        errors.append(f'{card.get("id")}: invalid level/status')
    if markdown.count(f'### {card.get("id")}:') != 1:
        errors.append(f'{card.get("id")}: Markdown card missing or duplicated')
    card_text = markdown.split(f'### {card.get("id")}:', 1)[-1].split('### GOV-', 1)[0]
    for field in ('title', 'value', 'data', 'process', 'tools', 'sample_output',
                  'risks', 'controls', 'metrics', 'dependencies', 'complexity'):
        if card.get(field) not in card_text:
            errors.append(f'{card.get("id")}: {field} differs from Markdown')
for area in areas:
    if Counter(c['level'] for c in cards if c['area'] == area) != Counter({1: 1, 2: 1, 3: 1}):
        errors.append(f'{area}: must contain exactly one card per level')
for file in ROOT.rglob('*.md'):
    for destination in re.findall(r'\[[^\]]*\]\(([^)]+)\)', file.read_text()):
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc:
            continue
        target = (file.parent / unquote(parsed.path)).resolve() if parsed.path else file.resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f'{file.relative_to(ROOT)}: missing local link {destination}')
        elif parsed.fragment and target.suffix == '.md':
            target_text = target.read_text()
            anchors = set(re.findall(r'<a id="([^"]+)"', target_text))
            for heading in re.findall(r'^#{1,6} (.+)$', target_text, re.M):
                anchors.add(re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-'))
            if unquote(parsed.fragment) not in anchors:
                errors.append(f'{file.relative_to(ROOT)}: missing anchor {destination}')
if not (ROOT / 'LICENSE').read_text().startswith('MIT License\n\nCopyright (c) 2026 caribbeanai'):
    errors.append('Existing licence/attribution changed')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print('PASS: 39 cards, 13 areas, 3 levels; schema, Markdown parity, local links and licence checks.')
print('Not checked: external link availability, rendered accessibility, legal compliance or factual accuracy.')
