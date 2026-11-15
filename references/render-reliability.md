# Render reliability

1. Validate a short motion sequence with audio before a full render.
2. Benchmark representative photo, document, and diagram sequences, not only frame zero.
3. Render resumable chunks with bounded retries and integer-frame boundaries.
4. Before reusing a chunk, verify frame count, duration, and decode integrity.
5. Gate post-processing on renderer success and all chunk checks; do not let trailing logging mask failure.
6. After concatenation or muxing, independently check full duration, boundary continuity, audio sync, dimensions, codecs, and measured loudness.
7. Report fresh progress and label estimates.

## Delivery

Distinguish a storyboard, motion preview, rendered draft, and final film. Source corrections do not automatically change already-rendered output. Keep temporary media and copyrighted source material out of version control, and verify destination hashes for any authorized transfer.
