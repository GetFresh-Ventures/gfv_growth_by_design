# High-Payoff Prompts for Executives

As an executive, you shouldn't be prompting for code snippets or fun facts. You should be using Claude Code to multiply your strategic leverage.

Here is a cheat sheet of high-payoff prompts designed to work with the `~/ceo-brain` architecture. Copy and adapt these — they work out of the box.

---

## The Daily Power Prompts

### 1. The Pre-Meeting Intelligence Brief
*Run this 30 minutes before crucial meetings.*

> "I have a meeting with [Name] from [Company] in 30 minutes. Use the `meeting-prep` skill. Search my recent emails and calendar for context. Check the CRM for their current deal stage. Give me a 1-page brief focused on my strategic angle and three talking points."

**Why it works**: You walk into the meeting with an unfair information advantage. The AI cross-references CRM data, past emails, and public news — work that would take you 20 minutes manually.

### 2. The Post-Meeting Action Extractor
*Run this immediately after hanging up on a Zoom call.*

> "Here are the raw notes/transcript from my call with [Company]: [paste]. Use the `post-meeting-brief` skill. Extract the commitments we made, what they owe us, and any shifts in the deal stage. Then, draft a follow-up email that I can send today."

**Why it works**: The 15-minute window after a call is when details are freshest. This prompt captures everything before it fades and produces a follow-up email *immediately*, not "I'll send that tomorrow" (which becomes never).

### 3. The Friday Pipeline Sanity Check
*Run this on Friday afternoon before you close out your week.*

> "Use the `deal-review` skill. Review all my active deals. I want you to be brutally honest: flag any deal that hasn't had activity in 14 days or has a close date in the past. Highlight the top 3 deals I am ignoring but shouldn't be."

**Why it works**: Deals die in silence. This prompt forces accountability on your pipeline and surfaces the ones slipping through the cracks before they're lost.

---

## The Strategic Prompts

### 4. The Authentic Outreach Sequence
*Run this when you identify a high-value target.*

> "I need to reach out to [Name] at [Company]. We have a mutual connection in [Mutual Name]. Use the `outreach-sequence` skill to build a 4-touch cadence. Do NOT use standard sales jargon. Reference my `~/ceo-brain/voice-model.md` to ensure it sounds like I actually wrote it."

**Why it works**: Cold outreach that sounds AI-generated gets deleted. This prompt forces voice model adherence and produces sequences that sound authentically human.

### 5. The Weekly Synthesis
*Run this Sunday night or Monday morning.*

> "Look at the meetings I had last week and the deals that moved in the CRM. Use the `weekly-ceo-brief` skill. Give me a clean summary of what actually mattered last week, and what my top 3 priorities *should* be going into Monday morning."

**Why it works**: Prevents the "busy but not productive" trap. Forces a structured review and forward-look.

### 6. The Competitive Response
*Run this when a competitor does something notable.*

> "Use the `competitive-intel` skill. [Competitor] just [announced X / launched Y / hired Z]. Analyze: (1) what this means for our positioning, (2) how it affects our active deals where they're also in the evaluation, and (3) what messaging adjustments we should make in the next 48 hours."

**Why it works**: Competitive moves require fast, structured response. This prompt turns panic into a playbook.

### 7. The Board Prep Sprint
*Run this 3-5 days before a board meeting.*

> "Use the `board-deck-builder` skill. I have a board meeting on [date]. Pull the latest pipeline numbers, key wins from the last quarter, and the 3 biggest risks. Structure a deck outline that leads with momentum, addresses the elephant in the room (which is [X]), and ends with a clear ask for [what you need from the board]."

**Why it works**: Board decks are the #1 CEO time sink. This prompt produces a structured outline with real data in minutes, not days.

### 8. The Contract Red Flag Scan
*Run this when you receive a new contract or term sheet.*

> "Use the `contract-reader` skill. Here's a contract from [Company]: [paste or attach]. Flag any clauses that limit our flexibility: auto-renewal terms, non-compete scope, liability caps, IP assignment, and termination notice periods. Summarize the 5 most important things I need to negotiate."

**Why it works**: Most CEOs sign contracts without reading the dangerous clauses. This prompt surfaces the traps in 60 seconds.

### 9. The "Should I Do This?" Decision Framework
*Run this when facing a significant strategic decision.*

> "Use the `strategic-decision` skill. I'm considering [decision — e.g., hiring a VP Sales / entering a new market / raising a bridge round]. Give me: (1) the 3 strongest arguments FOR, (2) the 3 strongest arguments AGAINST, (3) what I'm probably not considering, and (4) what decision you'd recommend if you were my Chief of Staff, and why."

**Why it works**: CEOs often make big decisions with confirmation bias. This prompt forces devil's advocacy.

### 10. The Financial Quick-Look
*Run this when you need a fast financial sanity check.*

> "Use the `financial-analyst` skill. Here are our numbers for [period]: Revenue: $X, Expenses: $Y, Pipeline: $Z. Calculate our burn rate, runway at current spend, and the revenue growth rate I'd need to hit [target] by [date]. Don't sugarcoat it."

**Why it works**: Founders often avoid looking at hard numbers. This prompt delivers the truth without emotion.

---

## Pro-Tips for Better Prompting

### Do's
- **Always set the persona**: "Be brutally honest," "Act like my Chief of Staff," "Write as if you're advising a board member"
- **Provide constraints**: "Keep this to 200 words," "Only give me bullet points," "No jargon"
- **Reference your brain**: "Base this on the notes in `~/ceo-brain/meetings/`"
- **Chain skills**: "After you finish the meeting prep, draft the follow-up email using `email-composer`"
- **Ask for alternatives**: "Give me 3 versions of this email — formal, casual, and bold"

### Don'ts
- **Don't accept the first draft** — iterate ("Make it shorter," "Change the tone")
- **Don't over-explain** — the AI has your context from `~/ceo-brain/`
- **Don't ask for generic advice** — anchor to your specific situation with names, numbers, dates
- **Don't skip the voice model** — 20 minutes of setup saves 200 hours of rewriting
