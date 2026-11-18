# Shot grammar

## Give every shot one editorial job

| Job | What it answers | Suitable media | Visible operation |
|---|---|---|---|
| Hook | Why should this matter? | decisive footage, document, chart delta | contrast, reveal, interruption |
| Proof | How do we know? | primary document, quoted reporting, measured chart | isolate, highlight, source hold |
| Context | Where and who are we? | footage, map, archival photo | establish, locate, scale |
| Mechanism | How does it work? | diagram, process model, annotated interface | transfer, constraint, accumulation |
| Comparison | What differs? | aligned chart, split evidence, repeated axis | align, rank, before/after |
| Consequence | So what changes? | outcome footage, chart, document | propagate, replace, payoff |
| Reset | What question comes next? | held frame, concise bridge, new evidence class | cut, reframing, silence |

A shot can have a secondary job, but do not ask one generic image to establish proof, context, and mechanism at once.

## Build the operation

Write each shot as:

`claim -> evidence -> actor/resource/unit/relation/constraint -> entry state -> visible operation -> result -> consequence`

Example, using fictional data:

`A club shifted revenue risk to long contracts -> published accounts -> club / guaranteed wages / £m / contract duration / league rules -> four contracts appear with annual cost -> contract bars extend while revenue line falls -> fixed commitments exceed current revenue -> cash flexibility narrows.`

The graphic need not be complex. It must make the relevant relation visible.

## Continuity rules

- Persist an element only if it preserves a comparison or causal link.
- Introduce a new evidence class with a cut or a clearly motivated transition.
- Keep charts on a stable axis while comparing values.
- Use labels as anchors, not as an alternative to showing the operation.
- Hold real documents long enough to establish attribution and reading task; do not flash them as decoration.

## Avoid these substitutes

- Product next to icon = no explanation of value flow.
- Trophy or skyline = no proof of a business claim.
- Generic dashboard = no evidence of a metric.
- Animated arrows without units or constraints = no mechanism.
- A headline that explains what the image cannot = a failed shot concept.

## Original worked shot repairs

These are invented staging exercises, not claims about a company, channel or measured outcome. Numbers, if supplied during production, require scoped sources. Phase lengths follow the measured narration and reading task, never a universal cut rate.

| Exercise | Bad panel | Before / operate / land | Evidence and consequence |
|---|---|---|---|
| Training then inference | Three cards saying data, training, answer | BEFORE: one toy context and stable parameter IDs. OPERATE: reveal a target, compare prediction, expose error and update the same parameters. LAND: hold changed values and next prediction. Cut to serving: lock those exact parameter values, append context and generate the next token without changing weights. | Original schematic, explicitly simplified. Numerically test any claimed loss decrease. Check inference parameter-region equality across phases, not just a "frozen" label. Context/output change does not establish retraining; online-learning exceptions need their own scope. |
| Equity versus compute commitment | Investor logos connected by identical animated cash arrows | BEFORE: persist investor, model developer and supplier as distinct actors. OPERATE: reveal an ownership-right relation separately from a service-purchase obligation, attaching currency, ceiling, term and conditional status to each. LAND: keep both obligations visible and leave actual payment unfilled unless evidence establishes it. | Show the authentic source excerpt first, then a labelled explanatory map. Commitment is not disbursement; ownership is not delivered compute. Never animate a closed same-dollar loop without transaction evidence. |
| Environmental scope | A giant AI icon fills an all-data-center energy total | BEFORE: source table owns the screen with year, geography and denominator. OPERATE: outline the measured population, retain that boundary while distinguishing estimate from projection. LAND: hold the reported scale and explicitly unmeasured AI subset. Cut to cooling: direct site water and upstream electricity-associated water occupy separate boundaries. | Use a sourced chart for magnitude, then an original schematic for physical paths. Do not add unlike water measures or claim a facility result from a global aggregate. Show task intensity and task count as separate variables; their net effect needs evidence. |
| Proposed offering versus proceeds | An IPO headline sends money into an issuer account | BEFORE: hold the attributed announcement and its proposed status. OPERATE: reveal proposed/filed/priced/completed milestones only where checked sources support them. For a conditional proceeds explanation, branch primary sales toward issuer and secondary sales toward selling holders. LAND: keep incomplete milestones and conditional routes visibly unresolved. | A proposal is not closing evidence. "Completion not established by checked sources as of cutoff" is narrower than "did not complete." Do not depict a completed cash transfer from an announcement. |

### One executable beat, not a universal layout

Original toy shot S-TOY uses cue N-TOY and asset A-TOY, an authored schematic. Its renderer consumes `parameter_id`, `before_value`, `after_value`, and phase boundaries. At the measured cue start it establishes a parameter at the prediction site; at the error phrase it changes that same value; after the update it holds the result through the next phrase. A reviewer should be able to point to the state difference without reading a title. If the renderer ignores `after_value`, this is a contract failure, not a stylistic preference. The JSON contract in [production specification](production-specification.md) records support; actual encoded proof must still show it.

Do not frame every shot with a chapter header, footer, caption panel and card. Accessible subtitles and attribution remain necessary, but their placement cannot turn every evidence class into the same scene. Let an authentic document, contextual footage or stable comparison surface own the frame when that is its job. A purposeful static evidence hold is valid; repeated static summary cards are not a substitute for causal operations. Inspect one complete before/operate/land sequence at normal speed before scaling a treatment across the film.
