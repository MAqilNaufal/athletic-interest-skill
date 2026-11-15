# Publication manifest

## Included files

| File/group | Public purpose | Source origin |
|---|---|---|
| `SKILL.md` | Entry-point episode workflow and verification | Curated, rewritten public adaptation of private working notes |
| `README.md` | Scope, quick start, privacy, and limitations | New public documentation |
| `LICENSE` | MIT license for this repository's authored material | New public licensing notice |
| `.gitignore` | Excludes local media, credentials, and generated artifacts | New public configuration |
| `references/*.md` | General evidence, workflow, visual asset, script/voice, music, production, and QA guidance | Curated, rewritten public adaptation |
| `templates/*` | Original dossier formats for claims, visual assets, narration, music, sequences, and reviews | New public templates |
| `scripts/validate_dossier.py` | Original stdlib-only structural dossier validator | New public utility |

## License and attribution rationale

The repository contains original, generalized documentation, templates, and code authored for public release. The MIT License applies only to those materials. It does not grant rights in any third-party audiovisual work, trademark, logo, channel identity, source-media frame, transcript, music, voice recording, speaker embedding, or other external material. The documentation is independent editorial-production guidance and is not affiliated with Athletic Interest.

## Excluded from publication

- Private agent configuration and internal instructions
- Corpus inventories, coverage ledgers, batch receipts, test/QA logs, and ephemeral experiment artifacts
- Personal or project-specific case studies, timecoded source observations, and rejected-output diagnoses
- Local paths, machine-specific locations, credentials, tokens, and runtime configuration
- Source media, frames, audio, transcripts, contact sheets, assets, and other copyrighted audiovisual material
- Voice references, clone configurations, raw takes, embeddings, and biometric verification output
- Internal scripts and artifacts that depend on the private corpus or local environment

## Verification

Before commit, review tracked files for secrets, local paths, private source material, private voice data, and unintended artifacts. Validate the example dossier from `templates/`; run Python compilation for the utility; check Markdown links; and inspect the final staged diff. Verify the public remote after push.
