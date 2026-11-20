# Detailed chat assessment

Use this reference only in detailed mode. Standard mode stays concise. Both modes
use `rank.py` and the same weighted score; this is an explanation view, not a
second scoring engine. Excel remains opt-in and uses concise descriptions.

## Freeze the requirement checklist

Before rating candidates, add `jobs[].requirements`: a list of `{id, text, group,
criterion_id, jd_evidence}`, where `group` is `must_have` or `nice_to_have`. These are individual,
distinct JD requirements, separate from the broader weighted scoring criteria.
Keep the JD wording/meaning: a named required tool may be its own requirement,
but "Python or Bash" is one alternative requirement, not two mandatory skills.
Deduplicate repeated JD wording and keep this same checklist for every candidate.
Do not invent requirements to match a target denominator or count CV keywords.
Exclude languages and employer reputation from skill counts; retain language
checks separately. Include explicit education/tenure prerequisites once each,
labelled as qualifications rather than technical skills in the evidence table.

Link every requirement to its weighted criterion with `criterion_id` (defaults
to the requirement ID when identical). When requirement text is identical to that
criterion, reuse its existing rating automatically: do not duplicate the rating or
quote in JSON. For older individual checklists with different IDs, add the
corresponding `criterion_id` links once using the frozen rubric. Only independently
worded subrequirements need
`requirement_ratings`, keyed by requirement ID, with
`status`, `reason` and `evidence`. Statuses are `met`, `partial`, `not_met`,
`unknown`; use short exact CV quotes with filename/page for supported findings.
`met` means fully evidenced; partial evidence does not count as a full match.
Missing evidence is "Not evidenced", not proof the candidate lacks the skill.
These counts never feed back into the weighted score or employer bonus. The
calculator rejects conflicting statuses for the same requirement, a fully met
criterion containing an unverified subrequirement, and an unknown criterion with
supported subrequirements. Reconcile genuine interpretation conflicts across all
candidates; never change ratings merely to improve match counts.

`rank.py` returns `match_summary` and `requirement_details`. Use their values
unchanged. A group with no requirements displays `N/A (none specified)`, not 0%.
For legacy assessments, `basis: grouped_criteria` counts the existing broad
criteria only. Build the missing checklist from the JD and rate it from cached
evidence before presenting individual-skill counts; do not pretend grouped
criteria are individual skills. This enrichment does not change old ratings.

## Presentation order

For each displayed candidate, use their full name as the heading. Start with the
three-row synthesis below. Columns are the actual JD role titles, even for one
JD; never use "Result" or candidate names as those column headers. For multiple
JDs, place eligible role results side by side. Keep the existing >=60 display
threshold unless the user explicitly requests other results. Preserve each JD's
calculated rank/order; do not invent a cross-role aggregate ranking.

| Metric | Intent Engineer | AI Engineer |
| --- | --- | --- |
| Must-Have Skills Matched | 18 / 25 (72.0%) | 19 / 26 (73.1%) |
| Good-to-Have Skills Matched | 1 / 5 (20.0%) | 1 / 5 (20.0%) |
| Overall Weighted Score | 61.6% | 62.5% |

Then create **one combined evidence/evaluation table per JD**, headed by the
actual role title. Requirements differ between roles: never pool them in one
shared evidence table or reuse one JD's evidence mapping for another.

| JD Requirement | Resume Evidence | Evaluation |
| --- | --- | --- |
| Example required platform | Used in the current role at Example Company. | Matched; criterion points / weight |
| Example optional tool (nice-to-have) | Related delivery documented; requested tool not stated. | Partial; criterion points / weight |
| Example prerequisite | Source explicitly confirms a shortfall. | Not met; criterion points / weight |
| Example required method | Not stated in the CV. | Not evidenced; criterion points / weight |

Cover the complete frozen requirement checklist, including preferred requirements
and gaps. Keep evidence concise and factual, using the CV's employer/client and
role context where available. Keep exact quotes, filenames and page references
in private assessment data unless the user asks for citations. Distinguish partial,
confirmed shortfall and missing evidence in the Evaluation column itself.

Combine weighted evaluation with the evidence rows; never add a separate scoring
breakdown table. When several requirements share one weighted criterion, show its
awarded points/weight only once, clearly labelled with that criterion; do not
repeat or invent individual requirement points. Add role-fit subtotal, employer
bonus and final total as bottom rows of that same table. Counts and all totals
come from the calculator unchanged. This presentation never changes scores.

Do not add introductory methodology/counting explanations, source-file preambles,
standalone evaluation prose, warnings about interpreting the score, conclusions,
interview questions or a "Points to validate" section. Keep those notes private;
show material gaps directly in the table. Provide extra explanation only when
explicitly requested. Contact details follow the >=80 display rule, before the
final background block.

Finish each candidate with these fields, after all their JD tables:
- **Industries:** CV-supported sectors, deduplicated; "Not stated" if absent.
- **Recent employers / clients:** the three latest assignments by supported dates
  (or fewer if available). Keep employer and client distinct; include role and
  source date range. Preserve ongoing/overlapping roles without inventing months.
- **Location:** supported city/country; "Not provided" if absent.

Store industries as `candidates[].industries: [{name, evidence}]` and assignment
history as `recent_assignments: [{employer, client, role, period, evidence}]`.
Extract these from the CV once. These fields are background context, never extra
score components. The example numbers/roles above illustrate layout only; never
copy them into real assessments. Do not add these fields as workbook columns.
