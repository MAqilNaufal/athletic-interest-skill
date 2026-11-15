# Publication manifest

## Included files

| File | Public purpose | Source origin |
|---|---|---|
| `SKILL.md` | Entry-point editorial workflow | Curated, rewritten public adaptation of private working notes |
| `README.md` | Scope, non-affiliation, and limits | New public documentation |
| `LICENSE` | MIT license for this repository's authored text | New public licensing notice |
| `.gitignore` | Prevents local media, credentials, and generated artifacts from tracking | New public configuration |
| `references/editorial-framework.md` | General argument, evidence, and mechanism guidance | Curated, rewritten public adaptation |
| `references/production-specification.md` | Renderer-neutral sequence contract | Curated, rewritten public adaptation |
| `references/quality-review.md` | Independent production review gates | Curated, rewritten public adaptation |
| `references/render-reliability.md` | Generic render and delivery checks | Curated, rewritten public adaptation |
| `references/research-protocol.md` | Generic evidence and review-level protocol | Curated, rewritten public adaptation |
| `references/audiovisual-review.md` | Review limitations and model-assisted-analysis cautions | Curated, rewritten public adaptation |

## License and attribution rationale

The repository contains original, generalized documentation authored for public release. The MIT License applies only to that documentation. It does not grant rights in any third-party audiovisual work, trademark, logo, channel identity, source-media frame, transcript, music, or other external material. The documentation is independent editorial-analysis guidance and is not affiliated with Athletic Interest.

## Excluded from publication

- Private agent configuration and internal instructions
- Corpus inventories, coverage ledgers, batch receipts, test/QA logs, and ephemeral experiment artifacts
- Personal or project-specific case studies, timecoded source observations, and rejected-output diagnoses
- Local paths, machine-specific locations, credentials, tokens, and runtime configuration
- Source media, frames, audio, transcripts, contact sheets, assets, and other copyrighted audiovisual material
- Internal scripts and artifacts that depend on the private corpus or local environment

## Verification

Before commit, the export must pass: repository-wide secret scanning; exact-content duplicate detection within the export; exact-file-hash comparison against the private source tree; YAML/front-matter parsing; Markdown-link checks; tracked-file review; and a check that no forbidden local-path or internal-artifact markers are present. Results are recorded in the release commit and verified again from the public remote.
