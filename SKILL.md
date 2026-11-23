---
name: athletic-interest-editorial-analysis
description: "Plan and review evidence-led documentary video essays."
version: 1.2.0
author: MAqilNaufal, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [editorial, documentary, production]
    related_skills: []
---

# Editorial analysis for sports and business documentaries

Use this skill to turn a factual question into an evidence-led documentary essay: research plan, script, visual asset plan, narration, music cues, sequence board, production brief, and independent review gates. It is an original method, not a recipe for reproducing any channel's protected expression, media, branding, scripts, or production assets.

## When to use

- Developing a sports, business, finance, technology, or culture video essay whose factual claims need evidence.
- Translating research and narration into an executable visual, voice, and music plan.
- Diagnosing why a draft feels like a slide deck, repeats the voice-over, uses generic B-roll, or has music that fights narration.
- Reviewing an animatic, render, or final mix against factual, editorial, technical, and audio gates.

Do not use it to infer facts from unreviewed media, treat a transcript as a complete audiovisual review, or imitate a named creator's visual identity.

## Required project dossier

Create one folder for the episode and copy the files from `templates/` into it:

- `production-brief.md` - audience, thesis, authorization, runtime, narrator, rights, budget, source cutoff, scope ledger and blockers.
- `storyboard-contract.json` - machine-checkable cue/shot/renderer contract and exact-master gate receipts.
- `claim-map.md` — claims, evidence, uncertainty, and section handoffs.
- `asset-ledger.csv` — provenance, rights status, narrative role, and gaps.
- `visual-asset-plan.csv` — asset class and treatment for every beat.
- `narration-cue-map.csv` — complete spoken script, clone-take status, and final timing.
- `music-cue-map.csv` — licensed/original instrumental selection and energy map.
- `sequence-board.md` — shot-level visual operations and timing.
- `review-gates.md` — technical, factual, editorial, and audio verdicts.

Run `terminal(command="python3 scripts/validate_dossier.py <dossier>")` for planning structure, then add `--strict` before production and `--release` before final delivery. Fill the contract and brief first; untouched templates intentionally fail strict validation. A clean validation confirms dossier structure only; it is not factual, rights, voice, music, or artistic approval.

## Production control loop

Treat the dossier as the film's source of truth and the encoded master as the thing being approved. Do not substitute a renderer's green status, a contact sheet, or a project preview for review of the actual delivery file.

1. **Preflight the selected path.** Confirm the renderer/editor, fonts, codecs, asset paths, narration method, audio tools, output dimensions, frame rate, and available storage before building scenes. Record the exact toolchain and supported properties in the storyboard contract. Completion: a short probe can render, decode, and play with sound.
2. **Choose one production route.** Mark each sequence material-led, footage/NLE, browser/canvas, compositor, or hybrid. The route follows the visual job: sourced action stays sourced; a mechanism can be diagrammed; a chart can be generated. Completion: every sequence has one route owner and no diagram silently replaces unavailable proof.
3. **Build the hardest representative sequence first.** Use final narration timing, intended asset treatment, captions, music behavior, and transition into the next idea. Render a short encoded proof, inspect its full-resolution frames and listen to its delivered audio. Completion: the proof passes the relevant review gates or has a named revision decision; do not scale an unreviewed approach across the episode.
4. **Lock approved contracts, not pixels by accident.** After the proof is accepted, retain its source, cue IDs, asset IDs, take hashes, timings, style decisions, and review receipt. A claim, take, asset, subtitle, or mix change invalidates only its dependent sequences plus downstream timing; it never inherits approval just because filenames remain the same.
5. **Render and review in bounded units.** Use deterministic time, integer-frame boundaries, bounded retries, and resumable chunks. Before reusing a chunk, verify its dependency hashes, frame range, duration, decode, and audio alignment. Completion: every reused or newly rendered unit has an explicit receipt.
6. **Inspect motion and sound before final encoding.** Inspect frame zero, cuts, transitions, full-resolution suspect frames, and normal-speed playback; listen to the delivered mix rather than inferring it from waveforms. Completion: no gate is passed by a proxy artifact or unreviewed audio.
7. **Approve the exact master.** Technical, factual, editorial, and audio reviewers independently record the encoded master SHA256. Any picture, subtitle, fact, or mux change creates a new master and reopens affected gates. Completion: final approval, if granted, names the same hash that may be transferred or uploaded.

## Procedure

0. **Verify scope and freshness.** Resolve installed realpath, owning repository, HEAD, dirty state and canonical remote revision. Preserve dirty work; inspect a pinned published copy separately if stale. Inventory the full pack, not just SKILL.md. Keep public guidance separate from private study receipts; record prior coverage and what this session actually inspected in the brief. A missing local file is not proof prior research never existed.
1. **Frame the question.** State the question, stakes, audience, target duration, named actors, and what evidence could disprove the intended answer. Completion: the opening question is answerable and falsifiable.
2. **Build the evidence base.** Record every source, date, scope, review level, and rights status in the claim map and asset ledger. Keep metadata, transcript reading, frame samples, continuous visual review, and direct listening distinct. Completion: every factual claim has a source or is explicitly marked provisional.
3. **Choose the argument shape.** Select a causal chain, comparison, clue-and-reveal, or list only when it fits the evidence. Give every section one obstacle to remove and one handoff question. Completion: the section order makes the answer progressively clearer.
4. **Write the spoken script.** Split the voice-over into retimable meaning units. Each unit must contain a claim or transition, one visual job, and a stated delivery intent. Completion: no line relies on generic B-roll or repeated headline text to carry its meaning.
5. **Plan final user-clone VO.** Final narration uses the user's authorized private clone unless the user explicitly selects another narrator. Synthesize per-line takes, verify ASR and speaker similarity, then regenerate final cue times. Completion: the cue map records take, checks, and timing without committing private reference material.
6. **Plan visual assets.** For each cue select a primary asset class: evidence, licensed context, original chart/diagram, disclosed reconstruction, or labelled generated illustration. Record treatment, credit, operation, and fallback. Completion: every visual is sourced and has an editorial job; missing exact assets stay blocked.
7. **Specify the sequence operation.** For each beat, use `argument -> visual evidence -> operation -> consequence`. Name actor, resource, unit, relation, constraint, entry state, visible change, and result. Completion: the shot can be understood without its headline.
8. **Map background music.** Select original or licensed instrumental music only after the final VO cue map exists. Map narrative state, energy, entry/exit, stems/edit points, and ducking or silence. Completion: music supports narrative contrast and cannot mask VO, quotes, or source audio.
9. **Build an animatic before production polish.** Test the claim map, final cue timing, asset treatment, handoffs, and key mechanisms in playback. Completion: every section has a clear question, answer, and visual change.
10. **Prove the hardest sequence.** Build and encode the most demanding representative passage before scaling production. Inspect full-resolution frames, transitions, and delivered audio against the dossier. Completion: the visual treatment has passed review or has a recorded revision decision.
11. **Choose a toolchain after the plan.** Use footage/NLE for lived action, documents for attribution, charts for measured change, diagrams for mechanisms, and HTML/3D only where they clarify the operation. Completion: implementation serves the edit instead of substituting for it.
12. **Run independent review gates.** Technical, factual, editorial, and audio approval are separate verdicts against the encoded master. Completion: every gate is `PASS`, `FAIL`, `UNREVIEWED`, or `BLOCKED`; none is implied by a successful export.
13. **Package delivery accurately.** Label the result storyboard, animatic, draft, or final film. Preserve sources and project records according to rights and retention requirements. Completion: delivered status matches what was actually reviewed.

## Visual and editorial rules

- Use footage for lived action; documents and quotations for attribution; charts for measured changes; diagrams for relationships and mechanisms; interviews for attributed testimony.
- Every shot must have a legible state change: comparison, transfer, accumulation, replacement, reordering, reveal, or a purposeful cut/hold. Sub-pixel drift is not motion.
- Keep a comparison axis, actor, badge, or legend only while it improves comprehension. Cut when a new evidence class needs the frame.
- Make designed quotations, reconstructions, and illustrative documents visibly distinct from authentic records.
- Use an original project identity. Palette, type, texture, camera, and transition are tools for comprehension, not a fixed channel imitation.
- Narration is led by the approved user clone. Retiming follows final take duration; never stretch old timing to fit it.
- Treat background music as a cue-mapped mix element. Use original/licensed instrumental sources and direct listening to confirm its relationship with VO and source audio.

## Reference materials

- [Workflow](references/workflow.md) — stage outputs and approval criteria.
- [Visual asset direction](references/visual-asset-direction.md) — sourcing, selection, treatment, and fallback rules.
- [Script and user voice](references/script-voice-direction.md) — spoken-script and authorized-clone contract.
- [Background music](references/music-direction.md) — energy, license, cue, and mix rules.
- [Shot grammar](references/shot-grammar.md) — editorial jobs and visual operations.
- [Pacing and narration](references/pacing-and-narration.md) — practical beat construction.
- [Troubleshooting](references/troubleshooting.md) — diagnose common draft failures.
- [Research protocol](references/research-protocol.md) and [audiovisual review limits](references/audiovisual-review.md) — evidence boundaries.
- [Editorial framework](references/editorial-framework.md) and [production specification](references/production-specification.md) — argument and build contract.
- [Quality review](references/quality-review.md) and [render reliability](references/render-reliability.md) — final gates.

## Verification

- Dossier structure passes `scripts/validate_dossier.py`.
- Each factual claim has evidence, scope, and uncertainty recorded.
- Each sequence has an intelligible operation and consequence.
- Every visual asset has a provenance, treatment, and narrative-role record.
- Every narration cue has final-clone verification and retimed shot cues.
- Every music cue has a source/license and ducking/silence plan.
- The hardest representative sequence has an encoded proof and a recorded review decision before full-scale production.
- Reused render chunks have matching contract/asset/take dependencies, duration, and decode receipts.
- Delivered video passes all four independent review gates; unresolved gates stay labeled.
