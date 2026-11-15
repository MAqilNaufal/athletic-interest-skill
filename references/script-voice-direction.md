# Script and user-voice direction

## Script style

Write for spoken understanding and visual consequence, not for an essay read aloud.

- Open with a concrete tension, question, or measured change—not a generic promise that the viewer will learn something.
- Establish the claim before escalating it. State who, what changed, on what scale, and why it matters.
- Alternate assertion, evidence, mechanism, and consequence. Do not stack abstract claims without showing how one creates the next.
- Prefer short clauses around numbers, names, and causal turns. Let the picture carry labels, sources, and comparisons rather than reading them verbatim.
- End every section with an earned answer and the exact unresolved question that starts the next section.
- Use a calm, precise, conversational delivery. Avoid trailer language, unsupported superlatives, rhetorical filler, and repeated headline text.

## Narration cue map

Write the complete spoken text in `narration-cue-map.csv`, split into retimable meaning units. Each row maps to a sequence ID, visual job, intended delivery, and final start/end cue. Acronyms, names, and numbers must be written phonetically when the voice engine mispronounces them.

## User-authorized clone policy

For this project family, final VO uses the user's own authorized voice clone unless the user explicitly requests another narrator.

- Keep the reference recording, clone configuration, raw takes, and any biometric/speaker-embedding outputs private and outside this repository.
- Use one approved reference for an entire film. Do not mix sessions or substitute a different reference midway.
- Produce per-line takes, a master WAV, a video delivery encode, SRT, and cue JSON.
- Verify each take with ASR round-trip against the script and speaker-similarity against the approved reference. Record outcomes in the cue map, not the private reference path or embedding.
- Rebuild cue times and retime the sequence board after final clone synthesis. Do not stretch a previous narration timing map to fit the clone.
- Any missing approved reference, failed ASR, failed speaker check, or unreviewed delivered mix leaves the audio gate `BLOCKED` or `UNREVIEWED`.

Use the `voice-cloning-tts` skill for engine setup, synthesis, loudness normalization, ASR, and speaker verification. The final mix must be directly listened to at normal playback speed.
