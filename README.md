# Evidence-led documentary editorial skill

An independent, evidence-led workflow for developing sports and business documentary essays: brief, claim map, asset ledger, narration allocation, sequence board, production handoff, and separate review gates.

> **Not affiliated with Athletic Interest.** This repository does not redistribute Athletic Interest videos, frames, audio, transcripts, logos, channel branding, or other source media. It provides a general editorial-production method, not a claim of studio equivalence or permission to imitate protected expression.

## What it provides

- Evidence and audiovisual-review boundaries
- A concrete episode workflow from brief to delivery
- Claim-map, asset-ledger, sequence-board, and review-gate templates
- Shot grammar for proof, context, mechanisms, comparisons, and consequences
- Pacing and narration rules for explanatory video
- Draft-diagnosis guidance and a lightweight dossier validator
- Separate technical, factual, editorial, and audio review gates

## Quick start

1. Copy `templates/` into a new episode dossier.
2. Fill the claim map before sourcing decorative assets.
3. Build the sequence board from narration meaning units.
4. Run:

```bash
python3 scripts/validate_dossier.py /path/to/episode-dossier
```

5. Review the animatic and final encoded video using `review-gates.md`.

The validator verifies dossier structure only. It does not prove factual accuracy, rights clearance, visual approval, or direct audio review.

## Repository layout

- `SKILL.md` — execution procedure and verification criteria.
- `references/` — workflow, shot grammar, pacing, evidence, production, and QA guidance.
- `templates/` — reusable project dossier files.
- `scripts/validate_dossier.py` — stdlib-only structural validator.

## Limitations

- Metadata, transcripts, frame samples, and model descriptions are not substitutes for continuous viewing or direct listening.
- Source material needs its own rights, attribution, and clearance review.
- A strong method does not certify factual accuracy, artistic approval, or legal clearance for a particular production.
- The repository contains no source-media corpus and makes no channel-wide style claims.

## License and attribution

The original text and code in this repository are released under the MIT License. That license covers only this repository's authored material; it does not grant rights in third-party audiovisual media, trademarks, channel names, clips, screenshots, music, or other external materials.
