# Quality review

Use `PASS`, `FAIL`, `UNREVIEWED`, or `BLOCKED` for each gate. Do not average them into a similarity score.

| Gate | Evidence required | Common failure |
|---|---|---|
| Technical | Full decode, expected duration and aspect, visible assets, readable encoded frames, clean boundaries, and sync checks | Blank frame, cropped label, duplicate cadence, drift |
| Factual | Claim, source, date, units, subject match, evidence/illustration distinction, and rights status | Generic image presented as proof, stale claim, unlabeled schematic |
| Editorial | Candidate and reference compared by editorial job; clear question, proof, mechanism, and payoff | Decorative motion, repeated generic objects, slide resets, obscured mechanism |
| Audio | Direct listening to the delivered mix, narration clarity, phrase timing, music, effects, silence, and transitions | Audio exists but was not listened to, voice masked by music |

## Before implementation

Prepare a claim map, source and rights inventory, narration cue map, annotated sequence board, mechanism sketch, and missing-capability list. Confirm that each asset has a narrative job and that each diagram can be explained without decorative movement.

## Review questions

1. What new understanding does the sequence create?
2. Does the image establish a claim, context, or mechanism—or only echo a keyword?
3. Is the main change visible and legible while it happens?
4. Does continuity aid a comparison, or merely keep an object on screen?
5. Does the next section answer a genuinely new question?
6. Has delivered audio been directly reviewed?

After rejection, record the feedback, inspect the encoded sequence, and identify the smallest evidence-supported change. Do not treat a longer rule list or a successful export as artistic approval.

## Exact-master final approval

Keep upload permission separate from artifact approval. Record destination, visibility and authorization in the brief; default to no upload. After technical, factual, editorial and audio review, each gate records a receipt and the exact encoded master SHA256 reviewed. Final approval records that same hash, reviewer and approval receipt. Never prefill PASS or auto-approve on encoder success. If the picture, audio, facts, subtitles or mux changes, invalidate approval and repeat affected reviews against the new master. A prior chapter proof or sampled contact sheet does not approve the assembled film. Transfer only the approved artifact when upload is separately authorized, then verify remote size/hash where the destination supports it.
