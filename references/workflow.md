# Documentary episode workflow

This is the execution loop behind the dossier. Work in order: prove the pipeline, prove the difficult sequence, then scale. A clean render, a contact sheet, or a timeline preview is not a substitute for reviewing the encoded sequence that will be delivered.

## 1. Preflight and route selection

Before drafting scenes, test the actual selected stack: renderer/editor, fonts, codecs, assets, narration, music, target dimensions, frame rate, and delivery container. Create a short probe that renders, decodes, and plays with sound. Record versions, supported properties, and output settings in `storyboard-contract.json`.

Assign one route owner per sequence:

- **Material-led:** licensed or supplied footage, documents, quotations, and photographs remain the primary evidence.
- **NLE/compositor:** documentary assembly, typography, captions, sound, and sourced footage need timeline control.
- **Browser/canvas/3D:** an explicit mechanism, chart, map, interface, or reconstruction needs deterministic generated movement.
- **Hybrid:** a named handoff joins the material-led and generated layers without disguising either.

Do not select a route for style alone. A missing source asset remains a blocker or an explicitly labelled substitution; a diagram is not proof of an event.

**Output:** a short encoded probe and route assignment for every sequence. Stop if the selected stack cannot make a reviewable proof.

## 2. Brief

Record audience, target duration, delivery format, central question, stakes, named entities, and the decision the viewer should be able to make after watching. State what would falsify the working thesis.

**Output:** completed [production brief](../templates/production-brief.md) and a question with a measurable or attributable answer. Include narrator consent/provenance, runtime authorization, source cutoff, rights, budget, deliverables, scope and upload gates; missing inputs remain named blockers. A one-paragraph creative premise alone is not a production brief.

## 2. Research and evidence map

Create claims before collecting decorative assets. For each claim record source, publication date, source scope, evidence level, counterevidence, and uncertainty. A source can support only the proposition it actually establishes.

**Output:** populated `claim-map.md`; unsupported claims are removed, narrowed, or labeled provisional.

## 3. Argument architecture

Choose one primary structure:

- **Causal chain:** explains how one condition creates another.
- **Comparison:** tests two entities against a stable axis.
- **Clue and reveal:** withholds an answer only while evidence earns the reveal.
- **Progressive list:** accumulates distinct factors toward a conclusion.

Each section must answer one question and create the next. Do not reset to a new topic without a handoff.

**Output:** section outline with opening question, answer, evidence, and handoff per section.

## 4. Narration and visual allocation

Divide narration into meaning units. Allocate one primary visual job per unit: proof, context, mechanism, comparison, consequence, or transition. If a line has no visual job, revise or remove it.

**Output:** narration cue map and initial sequence board.

## 5. Asset planning

Search only for assets that serve a named visual job. Record proof/context/analogy/reconstruction status, provenance, rights status, expected crop, credit requirement, and missing alternatives.

**Output:** asset ledger. Missing licensed assets remain blockers or explicit substitutions.

## 6. Animatic

Use rough footage, stills, diagrams, and temporary VO to test comprehension. Evaluate at normal speed; a static board does not prove timing or audio clarity.

**Output:** reviewable motion draft with section boundaries and timing notes.

## 7. Representative proof

Build the hardest or most characteristic sequence before producing the full film. It must use final timing, intended asset treatment, captions, audio behavior, transition logic, and delivery resolution. Inspect frame zero, every cut, any suspect full-resolution frame, and normal-speed playback with sound.

Record the result as `PASS`, `FAIL`, `UNREVIEWED`, or `BLOCKED` in `review-gates.md`. A failed proof calls for a sequence-concept correction first; changing colors or adding decorative movement does not repair an absent visual operation.

**Output:** encoded proof, reviewed master hash, and a decision to lock the approach or revise it. Do not scale an unreviewed proof across the episode.

## 8. Production

Upgrade approved shots without changing their editorial role. Use deterministic time and integer-frame ranges; render in bounded, resumable chunks where a full render is expensive or unreliable. Before reusing a chunk, verify its contract, script, take, mix, asset, renderer, and settings dependencies; then verify expected duration/frame count and decode integrity. A filename or non-empty partial file is never a cache hit.

Any substantial claim, narration, asset, subtitle, or audio change returns the affected sequence to review. A changed narration duration also retimes later dependent sequences, captions, and music cues.

**Output:** encoded draft plus changed sequence IDs and render receipts.

## 9. Encoded review and independent approval

Run technical, factual, editorial, and audio gates separately against the encoded master. Review full-resolution frames where the defect is suspected, not only a downsampled contact sheet; inspect normal-speed playback and listen directly to the delivered mix. Do not convert missing review into an assumed pass.

**Output:** completed `review-gates.md`, exact master hash, and clearly labeled delivery status.

## 10. Transfer and resume

Upload authorization is separate from master approval. Transfer only the approved encoded hash, then read back destination metadata where possible. On resumption, inspect active processes, prior receipts, logs, and completed outputs before starting work; do not launch a duplicate renderer or regenerate validated narration. Preserve editable project sources, timing maps, provenance records, font information, and output hashes outside prunable scratch storage.

**Output:** verified transfer receipt or a truthful blocker; retained project state sufficient to revise the approved master.
