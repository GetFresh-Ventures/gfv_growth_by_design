---
name: pipeline-pulse
description: Weekly pipeline health snapshot with trends, velocity metrics, and stage conversion analysis. The CEO's dashboard in markdown.
---

# Pipeline Pulse

Your weekly pipeline health check — trends, velocity, and what changed.

## When to Use
- End of week (Friday afternoon)
- Before weekly team standup
- Monthly/quarterly business reviews
- Investor update preparation

## Output Format

```markdown
# Pipeline Pulse — Week of [Date]

## This Week at a Glance
- **Pipeline value**: $X (↑/↓ $X from last week)
- **Weighted pipeline**: $X
- **Deals won**: X ($X)
- **Deals lost**: X ($X)
- **New opportunities**: X ($X)

## Stage Distribution
| Stage | Count | Value | Avg Days in Stage |
|-------|-------|-------|-------------------|

## Velocity Metrics
- **Average deal cycle**: X days
- **Win rate (30d)**: X%
- **Average deal size**: $X

## What Moved This Week
### Forward ✅
- [Deal] → [New Stage] (was [Old Stage])

### Backward ⚠️
- [Deal] → [Regression reason]

### New 🆕
- [Deal] — [Source/Channel]

### Closed Won 🎉
- [Deal] — $X

### Closed Lost 💀
- [Deal] — [Reason]

## Next Week Focus
1. [Priority deal/action]
2. [Priority deal/action]
3. [Priority deal/action]
```

## Example Prompt
```
Generate this week's pipeline pulse using the pipeline-pulse skill.
Compare against last week's numbers in brain/pipeline.md.
```
