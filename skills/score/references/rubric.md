# Scoring contract

## Understand the role before scoring

First state the client's need, operating environment and expected outcomes using
evidence from the JD. Identify explicit prerequisites and distinguish core outcomes
from preferred qualifications. Group overlapping tools under the capability they
serve. Give comparable credit for documented equivalent delivery only where the JD
allows it, and record accepted equivalents. Keep strict product, version and
certification requirements explicit; a related title or certificate alone does
not prove equivalence.

Only after this context is clear, define and freeze criteria and weights before
reviewing candidates. Use positive integer weights totalling 95 for role fit.
Aim for 4–10 distinct criteria when the JD supports that level of detail; allow
fewer when it does not, rather than inventing requirements or splitting one
requirement into artificial criteria. Cap the list at 10. Combine overlap so one
requirement is not scored twice. Weight core outcomes and prerequisites by their
importance in this role, then preferred qualifications. A typical starting
allocation is core skills 40, responsibility/delivery fit 30, relevant
experience/seniority 15 and sector/nice-to-haves 10; adapt to the JD. Do not score
CV design or keyword volume. Languages and employer prestige are outside the
95 role-fit points.

Each criterion records `priority` (`core`, `prerequisite`, `preferred`) and
`jd_evidence`, with optional frozen `accepted_equivalents`. A supported rating
uses `match_basis`: `direct`, `equivalent` or `adjacent`. An equivalent must name
the frozen `equivalent` and explain `equivalence_reason`. Adjacent evidence cannot
receive more than 0.5. For example, labs, awareness training or operational KPIs
do not by themselves establish production ownership, programme coaching or Agile
delivery metrics.

Each rating has a status, value, evidence references and a concise reason:

| Status | Rating | Meaning |
| --- | --- | --- |
| met | 1 | Evidence meets the criterion's required level/scope |
| partial | 0.75 | Strong relevant evidence with a specific remaining gap |
| partial | 0.5 | Some direct match, materially incomplete scope |
| partial | 0.25 | Limited or adjacent evidence, not an exact match |
| not_met | 0 | Explicit evidence confirms a shortfall |
| unknown | 0 | Insufficient CV evidence to assess |

Points = weight × rating. `met`, `partial` and `not_met` require a short CV quote
and filename/page reference. `unknown` requires an explanation, not fabricated
negative evidence. Zero for unknown means no demonstrated-match points; it does
not mean inability. Report weighted evidence coverage alongside major uncertainty.
Uncertainty should prompt verification, not an automatic hiring decision. The
calculator reports unknown weight separately from confirmed shortfall points,
and preserves required partial/unknown/not-met items as points to validate.
Evidence coverage is not confidence, capability or a hiring probability.

Use the same criterion interpretation for all candidates. A listed tool may
support basic familiarity but not years, production ownership or expert-level
delivery. A plan is not a delivered result. Count time without overlapping periods
twice; training/personal projects retain that context. Do not invent achievements,
degrees or experience duration. Keep confirmed must-have shortfalls visible even
if another criterion or the bonus raises the total. No automated exclusion.

## Relevant-employer bonus: up to 5 points

- 0: no evidenced relevant assignment at a qualifying employer, or unverified
  employer classification. State when classification remains uncertain.
- 2.5: at least one relevant assignment at a recognised large company or
  consulting firm, with both role relevance and company classification evidenced.
- 5: relevant assignments at two or more distinct qualifying employers/clients.

Use CV evidence for relevance and an employer-register entry for classification
(user-approved list, well-established company identity, or official company
reference). Apply the same register to everyone. A consulting employer and its
client on the same assignment count once. Repeat roles at the same employer count
once; parent company/subsidiary names do not multiply points. Bonus evidence must
identify the distinct assignments supporting the claimed tier. Do not give a
bonus merely for a company logo or unrelated role. Cap total score at 100.

## Language flags: zero scoring weight

Create one check per actual JD language condition, including an OR condition as
one combined check. Required and desirable conditions remain distinct. Allowed
statuses: `met`, `below_required`, `not_met`, `unknown`. Cite evidence for the first
three. If a language is listed without a level, report unknown when the required
level cannot be established; do not say it is not spoken. If the JD provides no
language conditions, use an empty list. Languages never affect score, rank,
bonus, evidence-coverage percentage or tie-breaks.

## Output and limits

Assess every supplied CV for every supplied JD. Scores represent demonstrated
CV-to-JD fit under an explicit rubric, not objective quality or hiring probability.
Keep evidence, weighted gaps and score calculations in private assessment data.
In chat, show only rank, match percentage, name, city/country, and a brief fit/gap
description for candidates at 60/100 or above; add phone and email only at 80/100
or above. Keep the description free of scoring commentary. Keep evidence and
temporary files local; no external API, package installation or CV upload is
required for scoring arithmetic.
