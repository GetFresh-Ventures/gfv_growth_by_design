---
name: email-composer
description: Write emails in the CEO's authentic voice — no buzzwords, no AI smell. Uses the voice model to match writing patterns, word choices, and formality levels.
---

# Email Composer

Write outbound emails that sound like *you* wrote them — not a chatbot.

## When to Use
- Drafting prospect outreach
- Following up after meetings
- Client communications
- Intro emails connecting two people
- Any email that represents you or your company

## How It Works

### Step 1: Load Voice Model
Read `~/brain/voice-model.md` before drafting. This contains your:
- Word choices and phrases you actually use
- Sentence structures and patterns
- Formality levels by audience
- Anti-patterns (words/phrases you'd never say)

### Step 2: Gather Context
Before writing, check:
1. **CRM** — What's the deal status? Last interaction? Open tasks?
2. **Email history** — When did you last email this person? What did you say?
3. **Meeting notes** — Any recent meetings with this contact?

### Step 3: Draft with Rules

**Format:**
```html
<body style="font-family: Arial, Helvetica, sans-serif; font-size: 14px; color: #333; line-height: 1.5;">
  <!-- Email content here -->
</body>
```

**Rules:**
- Match the voice model's tone for this audience type
- Never use banned words (see CLAUDE.md Rule #3)
- Keep it concise — CEOs don't write novels
- Include a clear ask or next step
- CC relevant team members on client outreach
- Before intro emails: verify both parties don't already know each other

### Step 4: Present for Approval
Show the full email inline. Wait for explicit "send it" before any action.

**Never auto-send. Never.**

## Banned Phrases (Always Enforced)
- "I wanted to reach out"
- "circle back" / "touch base"
- "align" (as verb) / "leverage" (as verb)
- "unlock" / "seamlessly" / "holistic"
- "transformative" / "game-changer" / "robust"
- "empower" / "move the needle"

## Quality Check
Before presenting, verify:
- [ ] Sounds like a real person, not an AI
- [ ] Has a specific ask or next step
- [ ] References something concrete (meeting, deal, shared context)
- [ ] No banned words or AI-sounding filler
- [ ] Appropriate length for the relationship stage
- [ ] CC list is correct

## Example Prompt
```
Draft a follow-up email to Sarah at Acme Corp. We met last Tuesday
and discussed their Q3 expansion plans. I want to propose a discovery
session next week. Use the email-composer skill.
```
