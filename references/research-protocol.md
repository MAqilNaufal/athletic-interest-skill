# Research protocol

## Scope and enumeration

Define the source set and date of collection. Canonical identifiers are stronger than search-result titles. Deduplicate by identifier, preserve category membership where useful, and keep absent or inaccessible material distinct from material that was reviewed.

## Evidence levels

- **Metadata only:** title, identifier, duration, and category; no editorial judgment.
- **Transcript read:** wording and structure only; timing remains separate.
- **Timeline sampled:** exact timestamps, ranges, display limits, and sampling method.
- **Native window:** bounded frame interval and inspected count; supports local motion observations only.
- **Continuous visual review:** actually played intervals and playback conditions.
- **Direct audio review:** listened intervals, speed, and sound observations.
- **Full audiovisual review:** complete, gap-free visual and audio coverage.

Do not promote a lower level into a higher one. Compute coverage by interval union rather than adding overlapping ranges.

## Handling media and rights

Check available storage and authorized sources before retrieval. At an authentication, verification, rate-limit, or access barrier, stop that route rather than bypassing it. Keep raw media, transcripts, frame caches, credentials, and private receipts outside version control. Retain only the minimum lawful metadata, method, and review-status records needed to reproduce a conclusion.

## Evidence language

Use `measured` for instrument output, `observed` for directly inspected material, `inferred` for a lesson derived from observations, and `provisional` for incomplete or model-generated interpretation. A caption, waveform, decode, or model report is not direct listening.

## Scope ledger and pack freshness

Before assigning work, resolve installed skill realpath, owning Git root, HEAD/dirty state and canonical remote revision. Inventory references, templates and validator at the selected revision. Preserve dirty installed work and inspect the published tree in isolation; never reset or pull over active edits. Record which revision actually directed production. A loaded entry point or missing local reference does not establish that a broader pack or prior study never existed.

Keep a private scope ledger: source set/canonical IDs, snapshot date, previously recorded review mode, this session's actual inspection mode, inaccessible entries, interval-union coverage and provenance receipts. A public generalized pack is not the private study itself. Do not copy corpus counts, timecodes, screenshots, private asset/voice locations or session IDs into the public skill. Transfer only general lessons and newly authored examples. Sampled images do not establish a soundtrack recipe; validate model audio methods with a silent control before using their descriptions, and never call model output direct listening.
