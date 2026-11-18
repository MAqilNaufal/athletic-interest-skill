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

## Resume and invalidate by dependency, not filename

Record chunk ID, half-open integer frame range `[start_frame, end_frame)`, rational frame rate, expected frame count, renderer/version hash, script/contract hash, used asset hashes, relevant take/mix hashes, render settings hash, output SHA256, decode/probe receipt and status. Adjacent chunks must meet exactly with no missing or duplicated frame. The final boundary is the accepted edit's integer frame count; audio keeps its measured sample timeline, not repeatedly rounded chapter durations.

On resume inspect active owner/process and progress first. Reuse only chunks whose dependency hashes, range, frame count and decode check still match; partial files or names alone are not a cache hit. A shot-only change invalidates its affected chunks; a take-duration change invalidates downstream timing-dependent chunks, subtitles and music alignment. A renderer/font/settings change invalidates every dependent chunk. A mix-only change can reuse verified picture but requires a new mux and audio/sync review. Use bounded retries and atomic completed-file promotion; never start a duplicate worker over an active output.

Example: chunk A covers frames `[0, 240)`, B `[240, 480)`. A changed asset used only in B invalidates B, not A. If a preceding cue grows by frames, recompute both the cue/frame mapping and every shifted range instead of joining the old filenames. Hash the final mux, not a pre-mux picture file. Any changed master invalidates approval, even if only captions or loudness changed.
