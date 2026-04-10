---
name: weekly-ceo-brief
description: Synthesize the week into a CEO-level summary — pipeline movement, key meetings, commitments, wins, risks, and priorities for next week.
---

# Weekly CEO Brief

Your week distilled into what actually matters.

## When to Use
- Friday afternoon / Sunday evening
- Before weekly leadership standup
- For investor or board reporting

## Output Format

```markdown
# CEO Brief — Week of [Date]

## 🎯 This Week in One Sentence
[One sentence that captures the most important thing that happened]

## Pipeline
- **New opportunities**: X ($X)
- **Deals progressed**: X
- **Deals won**: X ($X)
- **Deals lost**: X ($X)
- **Net change**: +/- $X
- **Total active pipeline**: $X

## Key Meetings (What Mattered)
| Meeting | With | Outcome | Next Step |
|---------|------|---------|-----------|

## Commitments Made
### We Owe
| What | To Whom | By When | Status |
|------|---------|---------|--------|

### They Owe Us
| What | From Whom | Expected | Status |
|------|-----------|----------|--------|

## Wins 🎉
- [Concrete win with numbers]

## Risks ⚠️
- [Risk with mitigation plan]

## Next Week Priorities
1. [Most important thing]
2. [Second priority]
3. [Third priority]
```

## Data Sources
Pull from (in order):
1. CRM — deal movement, new opportunities
2. Calendar — meetings attended
3. Email — commitments, follow-ups
4. Brain files — previous week's brief for comparison

## Rules
- Lead with "so what" — not a data dump
- Every risk must have a mitigation idea
- Every commitment must have a deadline
- Compare against last week (is pipeline growing or shrinking?)
- Be honest about losses — don't bury them

## Example Prompt
```
Generate my weekly CEO brief for this week.
Pull pipeline data from CRM and compare to last week's brief
in brain/weekly/. Use the weekly-ceo-brief skill.
```
