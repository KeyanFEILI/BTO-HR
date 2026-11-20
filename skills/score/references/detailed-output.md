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

Start with the JD title and a three-row synthesis table, matching the user's
reference layout. Candidate names are columns; for many candidates, split into
readable groups while preserving ranking order. Keep the default >=60 threshold
unless the user explicitly requests a lower-scoring candidate.

| Metric | Example Candidate |
| --- | --- |
| Must-Have Skills Matched | 3 / 5 (60.0%) |
| Good-to-Have Skills Matched | 1 / 2 (50.0%) |
| Overall Weighted Score | 74.5% |

Then provide each candidate's rank, name and location, followed by a table:

| Required Skill / JD Requirement | Resume Evidence |
| --- | --- |
| Example required platform | **Matched** — delivered in the stated assignment; CV filename p.2, short quote. |
| Example optional tool | **Partial (nice-to-have)** — related delivery documented; requested tool unverified. |
| Example prerequisite | **Not met** — source explicitly confirms the shortfall. |
| Example required method | **Not evidenced** — no supporting CV statement found. |

Cover the complete frozen checklist, including gaps and preferred requirements.
Each row must make the JD requirement and supporting CV evidence easy to trace;
name the employer/client/role when explicitly supported. Keep quotes short and
reasons specific. Follow with a concise evaluation rationale: strongest evidence,
material gaps, and missing evidence versus confirmed shortfalls. Never hide a prerequisite gap behind a high total. Include
the weighted criterion breakdown (criterion, weight, awarded points) and
state role-fit subtotal and employer bonus separately so the final score is
auditable; do not repeat evidence/reasons already in the requirement table or put
calculations into the fit/gap description. Keep all validation questions in the
single final points-to-validate list.

Finish each candidate with:
- **Industries:** CV-supported sectors, deduplicated; use "Not stated" if absent.
- **Recent employers / clients:** the three most recent assignments by supported
  dates (or fewer if available), preserving ongoing/overlapping roles. Show employer,
  client when named, role and source date range. Do not combine client and employer
  into one company or invent months to resolve ambiguous order.
- **Points to validate:** a short actionable list, including language/availability
  prerequisites when relevant. Contact details follow the >=80 display rule.

Store industries as `candidates[].industries: [{name, evidence}]` and assignment
history as `recent_assignments: [{employer, client, role, period, evidence}]`.
Extract these from the CV once, using its industry context rather than guessing
from company names. These fields are background context, never extra score
components. Do not copy screenshots' example people, numbers or technologies into
real assessments. Do not add these fields as workbook columns.
