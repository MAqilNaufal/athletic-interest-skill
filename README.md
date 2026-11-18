# Evidence-led documentary editorial skill

An independent, evidence-led workflow for developing documentary essays: brief, claim map, visual-asset plan, spoken script, user-clone VO cues, background-music cues, sequence board, production handoff, and separate review gates.

> **Not affiliated with Athletic Interest.** This repository does not redistribute Athletic Interest videos, frames, audio, transcripts, logos, channel branding, or other source media. It provides a general editorial-production method, not a claim of studio equivalence or permission to imitate protected expression.

## What it provides

- Evidence and audiovisual-review boundaries
- A concrete episode workflow from brief to delivery
- Claim, asset, visual-plan, narration, music, sequence, and review templates
- Visual asset sourcing/treatment rules and shot grammar
- Script-style, authorized user voice-clone, pacing, and retiming rules
- Original/licensed background-music selection and mix-cue rules
- Draft-diagnosis guidance and a lightweight dossier validator
- Separate technical, factual, editorial, and audio review gates

## Quick start

1. Copy `templates/` into a new episode dossier.
2. Fill the production brief, claim map, visual asset plan, narration cue map, music cue map and executable storyboard contract before production. Missing authorization, sources, rights or narrator provenance remain explicit blockers.
3. Generate and verify the approved user-clone narration; retime the sequence board from final cues.
4. Run:

```bash
python3 scripts/validate_dossier.py episode-dossier
python3 scripts/validate_dossier.py episode-dossier --strict
python3 scripts/validate_dossier.py episode-dossier --release
python3 -m unittest discover -s tests -v
```

5. Review the animatic and final encoded video using `review-gates.md`.

The validator verifies dossier structure only. It does not prove factual accuracy, rights clearance, voice similarity, music licensing, visual approval, or direct audio review.

## Repository layout

- `SKILL.md` — execution procedure and verification criteria.
- `references/` — workflow, visual sourcing, script/voice, music, shot grammar, pacing, evidence, production, and QA guidance.
- `templates/` — reusable project dossier files.
- `scripts/validate_dossier.py` — stdlib-only structural validator.

## Privacy and rights

Private voice references, clone configurations, takes, embeddings, raw media, and copyrighted source material remain outside this repository. The public templates record status and private reference IDs only.

## Limitations

- Metadata, transcripts, frame samples, and model descriptions are not substitutes for continuous viewing or direct listening.
- Source material and music need their own rights, attribution, and clearance review.
- A strong method does not certify factual accuracy, artistic approval, or legal clearance for a particular production.
- The repository contains no source-media corpus and makes no channel-wide style claims.

## Version 1.1 compatibility

Planning retains the original command and CSV headers, but now requires `production-brief.md` and validates each review verdict independently. Add the brief to older dossiers. `--strict` requires measured cue/CSV agreement, resolved IDs, renderer-supported properties, asset provenance and proof receipts in `storyboard-contract.json`. `--release` also checks exact-master review and final-approval declarations. Neither flag performs listening, authenticates receipts, verifies actual renderer pixels or authorizes upload. Fresh templates pass planning structure and intentionally fail production/release gates until filled.

The public pack contains generalized guidance and original worked exercises, not the private study corpus. Compare installed and canonical revisions before production without overwriting dirty local work. See [production contract](references/production-specification.md), [shot repairs](references/shot-grammar.md) and [brief](templates/production-brief.md).

## License and attribution

The original text and code in this repository are released under the MIT License. That license covers only this repository's authored material; it does not grant rights in third-party audiovisual media, trademarks, channel names, clips, screenshots, music, voice recordings, or other external materials.
