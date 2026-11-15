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
