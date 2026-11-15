---
name: athletic-interest-editorial-analysis
description: "Plan and review evidence-led documentary video essays."
license: MIT
---

# Editorial analysis for sports and business documentaries

Use this skill to turn a factual question into an evidence-led documentary essay: research plan, argument, narration, sequence board, asset ledger, production brief, and independent review gates. It is an original method, not a recipe for reproducing any channel's protected expression, media, branding, scripts, or production assets.

## When to use

- Developing a sports, business, finance, technology, or culture video essay whose factual claims need evidence.
- Translating research and narration into an executable visual plan.
- Diagnosing why a draft feels like a slide deck, repeats the voice-over, or uses motion without explanation.
- Reviewing an animatic, render, or final mix against factual, editorial, technical, and audio gates.

Do not use it to infer facts from unreviewed media, treat a transcript as a complete audiovisual review, or imitate a named creator's visual identity.

## Required project dossier

Create one folder for the episode and copy the files from `templates/` into it:

- `claim-map.md` — claims, evidence, uncertainty, and section handoffs.
- `asset-ledger.csv` — provenance, rights status, narrative role, and gaps.
- `sequence-board.md` — shot-level visual operations and timing.
- `review-gates.md` — technical, factual, editorial, and audio verdicts.

Run `terminal(command="python3 scripts/validate_dossier.py <dossier>")` before storyboard approval and before delivery. A clean validation confirms dossier structure only; it is not factual, rights, or artistic approval.

## Procedure

1. **Frame the question.** State the question, stakes, audience, target duration, named actors, and what evidence could disprove the intended answer. Completion: the opening question is answerable and falsifiable.
2. **Build the evidence base.** Record every source, date, scope, review level, and rights status in the claim map and asset ledger. Keep metadata, transcript reading, frame samples, continuous visual review, and direct listening distinct. Completion: every factual claim has a source or is explicitly marked provisional.
3. **Choose the argument shape.** Select a causal chain, comparison, clue-and-reveal, or list only when it fits the evidence. Give every section one obstacle to remove and one handoff question. Completion: the section order makes the answer progressively clearer.
4. **Write narration as visual instructions.** Split the voice-over into meaning units, not arbitrary sentence-sized shots. For each unit, specify whether the visual must prove, contextualize, compare, or explain a mechanism. Completion: no line relies on a generic B-roll placeholder to carry its meaning.
5. **Specify the sequence operation.** For each beat, use `argument -> visual evidence -> operation -> consequence`. Name actor, resource, unit, relation, constraint, entry state, visible change, and result. Completion: the shot can be understood without its headline.
6. **Assign assets deliberately.** Mark each asset as proof, context, analogy, or reconstruction. Record source, date, clearance, crop constraints, and on-screen credit need. Completion: decorative material is not presented as proof.
7. **Build an animatic before production polish.** Test the claim map, reading time, handoffs, and key mechanisms in playback. Completion: every section has a clear question, answer, and visual change.
8. **Choose a toolchain after the plan.** Use footage/NLE for lived action, documents for attribution, charts for measured change, diagrams for mechanisms, and HTML/3D only where they clarify the operation. Completion: implementation serves the edit instead of substituting for it.
9. **Run independent review gates.** Technical, factual, editorial, and audio approval are separate verdicts. Completion: every gate is `PASS`, `FAIL`, `UNREVIEWED`, or `BLOCKED`; none is implied by a successful export.
10. **Package delivery accurately.** Label the result storyboard, animatic, draft, or final film. Preserve sources and project records according to rights and retention requirements. Completion: delivered status matches what was actually reviewed.

## Visual and editorial rules

- Use footage for lived action; documents and quotations for attribution; charts for measured changes; diagrams for relationships and mechanisms; interviews for attributed testimony.
- Every shot must have a legible state change: comparison, transfer, accumulation, replacement, reordering, reveal, or a purposeful cut/hold. Sub-pixel drift is not motion.
- Keep a comparison axis, actor, badge, or legend only while it improves comprehension. Cut when a new evidence class needs the frame.
- Make designed quotations, reconstructions, and illustrative documents visibly distinct from authentic records.
- Use an original project identity. Palette, type, texture, camera, and transition are tools for comprehension, not a fixed channel imitation.
- Treat audio as a separate deliverable. Narration clarity, music, clips, silence, timing, and transitions require direct listening to the delivered mix.

## Reference materials

- [Workflow](references/workflow.md) — stage outputs and approval criteria.
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
- Every asset has a provenance and narrative-role record.
- Delivered video passes all four independent review gates; unresolved gates stay labeled.
