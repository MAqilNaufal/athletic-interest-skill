# Production specification

## Sequence contract

For each sequence, record:

- The question, evidence-supported claim, consequence, and handoff question.
- Approved narration cue range and whether timing was human-checked or provisional.
- Subject, asset provenance, clearance status, and evidence class.
- Medium and reason for it.
- Entry state, intelligible change, and result.
- What persists, exits, or returns, and why.
- Focal hierarchy, reading task, framing, palette, and transition purpose.
- Audio intention and review status, separately from picture.

## Pacing and evidence

Time edits to meaning, voice phrasing, reading time, information density, and contrast. A held interview, progressive list, and fast cutaway can each be appropriate. Charts need units, dates, scales, and labels. Conceptual diagrams must not imply measured proportions or facts they do not show.

## Visual language

Use an original project identity. Full-frame footage, pale documents, sparse holds, diagrams, and dense explanatory sequences can all be useful. Graphics must carry a relationship; moving a product beside an icon does not explain allocation, causality, or value transfer without a legible mechanism.

## Renderer-neutral implementation

Choose tools against asset and edit requirements. If HTML is used, drive all state from deterministic time, support reverse seeks, wait for assets before capture, and inspect encoded output. Do not claim native frame cadence from duplicated low-frame-rate captures.

## Final gates

Technical integrity, factual accuracy, editorial approval, and audio approval are independent. Missing review is not a pass.

## Executable storyboard contract

Use [storyboard-contract.json](../templates/storyboard-contract.json) alongside the existing CSVs and sequence board, not as a replacement research pack. IDs are exact strings: do not normalize `001` to `1`. Each cue binds stable cue/take IDs, canonical display text, synthesis text, subtitle text, measured start/end seconds and a duration measurement receipt. Each shot binds cue IDs, asset IDs, registered visual type, renderer-consumed properties, and integer `before_frame < operate_frame < land_frame < end_frame` within its start/end range. Asset IDs resolve to source, rights status, provenance receipt and evidence class. An original drawing still needs authorship/provenance and a schematic label.

Export `renderer.types` from the actual renderer: each type lists `required_props` and `supported_props`; record renderer revision and support-test receipt. Unknown types/properties fail, never fall back to a generic panel. A declared registry is not proof of implementation: exercise every changed type, capture encoded before/change/settled frames, reverse-seek determinism where applicable, and play a continuous proof. Record that receipt per shot. Units, interpolation semantics, asset decode readiness and property meanings belong in the renderer adapter. Strict validation checks the contract, not pixels or source truth. It checks cue/shot overlap, not complete interval coverage, word alignment or typed property semantics; the renderer adapter and encoded review own those tests. Numeric toy parameters are not measured production data.

Keep canonical narration equal to narration CSV `spoken_text`; take IDs, times and subtitle text must agree. Synthesis-only pronunciation changes need a meaning-review receipt. Rewording a claim is an editorial revision, not a pronunciation fix. Measured take changes invalidate affected edit, captions and music cues, even if the words are unchanged. Proportional phrase allocation is not forced alignment.

Run through `terminal`:
```text
python3 scripts/validate_dossier.py episode
python3 scripts/validate_dossier.py episode --strict
python3 scripts/validate_dossier.py episode --release
python3 -m unittest discover -s tests -v
```

Compatibility: existing CSV columns and planning invocation are retained. The brief is now required; legacy dossiers must copy and fill it. Planning mode permits unfinished content but checks each named gate's exact verdict. Strict mode additionally requires the JSON contract, completed brief fields, measured cue consistency, resolved IDs, renderer support and provenance. Release implies strict and requires all four PASS receipts and final approval tied to the same master SHA256. Approval is an external human/editor decision recorded after QA, never set by this validator. These checks do not certify art, truth, rights or listening. A release check does not authorize upload.
