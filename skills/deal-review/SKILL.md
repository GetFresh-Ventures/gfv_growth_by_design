---
name: deal-review
description: Honest CRM pipeline review — flags stale deals, missing next steps, and unrealistic close dates. Surfaces what needs attention before it's too late.
---

# Deal Review

An honest assessment of your pipeline — not a dashboard screenshot.

## When to Use
- Weekly pipeline review (Friday recommended)
- Before board meetings or investor updates
- When something "feels off" about your pipeline
- After a deal is won or lost (retrospective)

## How It Works

### Step 1: Pull Pipeline Data

From your CRM, pull all active deals with:
- Company name, deal name
- Stage, amount, close date
- Owner, last activity date
- Days in current stage
- Next scheduled step

### Step 2: Health Assessment

For each deal, evaluate:

**🟢 Healthy** — Clear next step, recent activity (< 7 days), realistic close date
**🟡 At Risk** — No activity 7-14 days, next step unclear, close date may slip
**🔴 Stale** — No activity 14+ days, no next step, close date passed or unrealistic

### Step 3: Build the Review

```markdown
# Pipeline Review — [Date]

## Summary
| Metric | Value |
|--------|-------|
| Total pipeline | $X |
| Weighted pipeline | $X |
| Deals at risk | X |
| Stale deals (14+ days) | X |
| Expected to close this month | $X |

## 🔴 Needs Immediate Action
[Deals that are stale, past close date, or at serious risk]

| Deal | Stage | Amount | Last Activity | Days Stale | Issue |
|------|-------|--------|-------------|-----------|-------|

**Recommended actions:**
1. [Specific action for deal 1]
2. [Specific action for deal 2]

## 🟡 Watch List
[Deals showing early warning signs]

| Deal | Stage | Amount | Last Activity | Risk Signal |
|------|-------|--------|-------------|------------|

## 🟢 On Track
[Deals progressing normally]

| Deal | Stage | Amount | Next Step | Expected Close |
|------|-------|--------|----------|---------------|

## Pipeline Trends
- Deals added this week: X ($X)
- Deals moved forward: X
- Deals lost/closed: X
- Net pipeline change: +/- $X
```

### Step 4: Save & Update

After review:
1. Update `~/brain/pipeline.md` with current state
2. Create follow-up tasks in CRM for any 🔴 deals
3. Note pattern observations in `~/brain/learnings.md`

## Red Flags to Always Call Out
- Close date in the past (deal is technically overdue)
- No next step defined (deal will die)
- No activity in 14+ days (prospect has gone cold)
- Amount seems unrealistic for stage
- Multiple deals at same company with conflicting stages
- "Nurture" stage for > 30 days (it's dead, be honest)

## Example Prompt
```
Run a full pipeline review using the deal-review skill.
Flag anything stale and recommend specific next steps.
```
