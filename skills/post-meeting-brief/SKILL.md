---
name: post-meeting-brief
description: Extract action items, decisions, and follow-up email drafts from meeting notes or transcripts. Never let action items fall through the cracks.
---

# Post-Meeting Brief

Turn meeting notes into action within 15 minutes of the meeting ending.

## When to Use
- Immediately after any client, prospect, or partner meeting
- When you have a transcript (Fathom, Otter, Krisp, manual notes)
- Before the meeting fades from memory

## How It Works

### Step 1: Ingest Meeting Content
Accept meeting notes from any format:
- Transcript from Fathom/Otter/Krisp
- Manual notes (bullet points, stream of consciousness)
- Calendar event description + your verbal summary

### Step 2: Extract Intelligence

```markdown
# Post-Meeting Brief: [Company] — [Date]

## Meeting Details
- **Attendees**: [names and roles]
- **Duration**: [length]
- **Type**: [Discovery / Follow-up / Negotiation / Check-in]

## Key Decisions Made
1. [Decision with context]
2. [Decision with context]

## Action Items

### Ours (We Committed To)
| Action | Owner | Deadline | Priority |
|--------|-------|----------|----------|

### Theirs (They Committed To)
| Action | Who | Expected By |
|--------|-----|-------------|

## Key Insights
- [Something we learned about their business/needs]
- [Buying signal or concern]
- [Relationship dynamic observation]

## Deal Impact
- **Stage change**: [Yes/No — if yes, what stage?]
- **Amount change**: [Yes/No — if yes, new amount?]
- **Close date**: [Confirmed / Moved / At risk]
- **Next meeting**: [Scheduled? When?]

## Follow-Up Email Draft
[Draft follow-up email using email-composer rules]
```

### Step 3: Update Systems
1. Create tasks in CRM for "Our" action items
2. Update deal stage/amount if changed
3. Save brief to `~/brain/meetings/[date]-[company]-post.md`
4. Log any learnings in `~/brain/learnings.md`

## Quality Check
- [ ] Every action item has an owner and deadline
- [ ] Follow-up email references specific meeting content
- [ ] Deal impact is honestly assessed (not just "went well")
- [ ] CRM is updated (not just the markdown file)

## Example Prompt
```
Process my notes from the Acme Corp meeting that just ended.
Here are my notes: [paste notes]. Use the post-meeting-brief skill.
```
