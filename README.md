<div align="center">
  <img src="assets/gfv-logo-dark.png" alt="GetFresh Ventures Logo" height="180">

  # Growth by Design™ CEO AI Kit

  <p align="center">
    <strong>194 local AI skills that turn any coding assistant into a private Chief of Staff for Go-To-Market orchestration.</strong><br>
    <em>Powered by the <a href="https://www.getfreshventures.com?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit">Growth by Design™</a> methodology from GetFresh Ventures.</em>
  </p>

  [![Version](https://img.shields.io/badge/version-v1.40.0-blue.svg)](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit/releases)
  [![Status](https://img.shields.io/badge/status-production-success.svg)]()
  [![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()
  [![License](https://img.shields.io/badge/license-MIT-green.svg)]()

  [📰 Newsletter](https://growthbydesign.substack.com/) · [🌐 Official Page](https://www.getfreshventures.com/ceo-ai-kit?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit) · [🔍 Free Growth Diagnostic](https://www.getfreshventures.com/diagnostic?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit) · [🤝 Book a Discovery Call](https://www.getfreshventures.com/contact?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit)
</div>

---

## Stop Adding Headcount. Start Engineering Growth.

Revenue generation is a systems engineering problem — not a hiring problem. Pipelines, conversion paths, attribution loops, campaign orchestration, lead scoring — these are interconnected subsystems with feedback mechanisms. Treating them as tasks assigned to humans creates latency. Every handoff is a delay. Every weekly sync is a batch process in a world that demands real-time.

**Growth by Design™** is the exact methodology [GetFresh Ventures](https://www.getfreshventures.com?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit) uses to embed agentic AI into GTM systems for growth-stage CEOs — the same approach that has impacted **$500M+ in client revenue** and engineered **6 successful exits** across 50+ companies.

This kit is that methodology, open-sourced.

---

## What This Kit Does

The GxD CEO AI Kit installs directly into your local development environment — Cursor, Claude Code, Windsurf, Gemini, or Copilot — and transforms it from a generic chatbot into an **autonomous Chief of Staff** that knows your voice, your deals, and your weekly rhythm.

| What changes | Before | After |
|-------------|--------|-------|
| **Email drafting** | Generic AI tone | Writes in *your* voice, trained on your actual emails |
| **Meeting prep** | Walk in cold | AI delivers intelligence dossiers before every call |
| **Pipeline management** | Weekly spreadsheet review | Continuous monitoring with stale-deal alerts |
| **Content strategy** | Ad hoc posts | System-driven content calendar with buyer-stage mapping |
| **Strategic decisions** | Gut feel | 5-perspective GO/NO-GO/DEFER framework |

**Your data stays on your machine.** No cloud uploads. No SaaS telemetry. The AI communicates only via secured API endpoints you control.

---

## The Growth by Design™ Architecture

This kit implements the same three-layer architecture that powers GetFresh Ventures' client engagements:

```
┌───────────────────────────────────────────────────────────────┐
│  AI Coding Assistants: Cursor · Claude Code · Windsurf       │
│                        Gemini · Copilot · Codex              │
└────────────────────────────┬──────────────────────────────────┘
                             │
                             ▼
┌───────────────────────────────────────────────────────────────┐
│  AGENT.md — The Growth by Design™ Persona                    │
│  Stage-aware identity, 90-day sprint thinking, voice model   │
└────────────────────────────┬──────────────────────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     ┌────────────────┐ ┌──────────┐ ┌──────────────────┐
     │  194 Domain    │ │  Event   │ │  Local CEO Brain  │
     │  Skills        │ │  Hooks   │ │  (SQLite FTS5)    │
     │                │ │          │ │                    │
     │  GTM Strategy  │ │  Pre/    │ │  Voice Model      │
     │  AI Execution  │ │  Post    │ │  Pipeline State   │
     │  AI Adoption   │ │  Safety  │ │  Decision History  │
     └────────┬───────┘ └──────────┘ └──────────────────┘
              │
     ┌────────┴──────────────────────────────┐
     │  Integrations                          │
     │  HubSpot · Linear · Google Ads · Slack │
     │  GA4 · QuickBooks · PandaDoc · SEMrush │
     └───────────────────────────────────────┘
```

### Three Pillars (from the Growth by Design™ Methodology)

| Pillar | What It Means | Kit Implementation |
|--------|--------------|-------------------|
| **GTM Strategy** | Pipeline intelligence, revenue systems, and sprint planning | C-Suite Advisory skills, Revenue Enablement skills |
| **AI Engineering** | Hands-on sprints that ship AI into your GTM | Developer & DevOps skills, automation hooks |
| **AI Adoption** | Personal AI operating systems configured to your voice and context | Voice model, onboarding wizard, Sherpa Protocol |

---

## Quick Start

```bash
git clone https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit.git ~/Documents/gxd-ceo-ai-kit
cd ~/Documents/gxd-ceo-ai-kit
./bootstrap.sh          # Mac/Linux
# .\bootstrap.ps1       # Windows
```

Then open the folder in **Cursor** (or your preferred AI IDE) and type `/onboard` in the chat.

The onboarding wizard takes ~15 minutes. It will:
1. **Calibrate your voice** — Paste a few emails, and the AI learns to write like you
2. **Map your team** — Who handles what, so the AI routes correctly
3. **Load your pipeline** — Enter your top deals for continuous monitoring

> **You don't need to be technical.** If you can open a terminal and paste a command, you can do this. The kit includes a Sherpa Protocol that teaches IDE fluency to first-time users.

For the full walkthrough, see **[GETTING-STARTED.md](GETTING-STARTED.md)**.

---

## Full Capabilities: 194 Domain Skills

Skills are composable instruction sets that augment the baseline intelligence of an LLM. Instead of generic chat completion, the AI retrieves a proven playbook at runtime — ensuring it operates with the rigor of a seasoned operator, not an entry-level assistant.

### 🎯 Execution Infrastructure (13 skills)
*The agent's brain, coordination, and decision-making.*

| Skill | Description | Key Pattern |
|-------|-------------|-------------|
| [`chief-of-staff`](skills/chief-of-staff/) | 3-layer triage with sprint execution cadence and memory hierarchy | Resolve, don't summarize |
| [`experiment-loop`](skills/experiment-loop/) | Scientific method for business: baseline → change → measure → keep/discard | One variable per cycle |
| [`strategic-decision`](skills/strategic-decision/) | 5-perspective GO/NO-GO/DEFER framework | Multi-lens evaluation |
| [`decision-logger`](skills/decision-logger/) | Two-layer memory with team activity log syncing | Nothing lost |
| [`verify-execution`](skills/verify-execution/) | Runtime observation instead of diff-reading | Trust but verify |
| [`gfv-hooks`](skills/gfv-hooks/) | Event-driven lifecycle hooks with safety gates | Governance without friction |
| [`agent-protocol`](skills/agent-protocol/) | Inter-agent communication for C-suite skills | Structured delegation |
| [`context-engine`](skills/context-engine/) | Company context loading for advisory skills | Know before advising |
| [`dedupe-entities`](skills/dedupe-entities/) | Mathematically resolves duplicate records using ML active linkage | Entity Resolution |
| [`notion-manager`](skills/notion-manager/) | Safely connect and map Notion workspaces | Verification First |
| [`cron-scheduler`](skills/cron-scheduler/) | Configure recurring loops with 6-layer diagnostic | Verify Silent Failures |
| [`agent-orchestrator`](skills/agent-orchestrator/) | Coordinate multi-agent pipeline tasks using DAG and Debate modes | Structured dispatch |
| [`automation-recommender`](skills/automation-recommender/) | Analyze a codebase and recommend automations | Optimize your setup |

> 💡 **Want this deployed with live data sources and autonomous agents?** Explore [Revenue Foundations →](https://www.getfreshventures.com/solutions/revenue-foundations?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit)

### 👔 C-Suite Advisory (8 skills)
*Specialized strategic advisory from each leadership perspective.*

| Skill | Description | Key Pattern |
|-------|-------------|-------------|
| [`ceo-advisor`](skills/ceo-advisor/) | Strategic leadership: portfolio oversight, GTM, talent | The buck stops here |
| [`cfo-advisor`](skills/cfo-advisor/) | Financial modeling, unit economics, fundraising | Show me the numbers |
| [`cmo-advisor`](skills/cmo-advisor/) | Brand positioning, growth models, marketing budget | Market-facing strategy |
| [`coo-advisor`](skills/coo-advisor/) | Process design, OKR execution, operational cadence | Run-rate excellence |
| [`cro-advisor`](skills/cro-advisor/) | Revenue forecasting, sales model, pricing strategy | Revenue engine |
| [`executive-mentor`](skills/executive-mentor/) | Adversarial thinking partner — stress-tests plans | Your brutal board prep |
| [`founder-coach`](skills/founder-coach/) | Personal leadership, delegation, archetype identification | CEO as a human |
| [`negotiation-advisor`](skills/negotiation-advisor/) | BATNA analysis, concession architecture, tactical deal scripts | Close the deal |

> 💡 **Need a senior operator, not just advisory prompts?** Explore [Fractional GTM + AI Co-Pilot →](https://www.getfreshventures.com/solutions/fractional-gtm?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit)

### 💰 Revenue Enablement (8 skills)
*Everything that directly generates or accelerates revenue.*

| Skill | Description | Key Pattern |
|-------|-------------|-------------|
| [`pipeline-pulse`](skills/pipeline-pulse/) | Active pipeline management with resolve-first bias | Act, don't report |
| [`deal-review`](skills/deal-review/) | Honest CRM review: flags stale deals, missing next steps | No happy ears |
| [`sales-enablement`](skills/sales-enablement/) | Pitch decks, objection docs, demo scripts, playbooks | Arm the reps |
| [`fundraise`](skills/fundraise/) | Investor materials + outreach with SSoT consistency | All numbers agree |
| [`outreach-sequence`](skills/outreach-sequence/) | Multi-touch prospecting sequences | Persistent, not annoying |
| [`competitive-intel`](skills/competitive-intel/) | Systematic competitor tracking | Know the battlefield |
| [`contract-reader`](skills/contract-reader/) | 4-layer legal contract analysis with red-flag detection | Know before you sign |
| [`domain-intel`](skills/domain-intel/) | WHOIS, DNS, and domain expiry intelligence | Research the terrain |

> 💡 **Want AI agents running your revenue stack 24/7?** Explore [AI Operations Engineering →](https://www.getfreshventures.com/solutions/ai-revops?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit)

### 📄 Document Processing (5 skills)
*Creating, editing, and processing business documents.*

| Skill | Description | Key Pattern |
|-------|-------------|-------------|
| [`spreadsheet-builder`](skills/spreadsheet-builder/) | IB-grade Excel with color coding, formulas, scenarios | Blue = input, Black = formula |
| [`pdf-toolkit`](skills/pdf-toolkit/) | PDF merge, split, watermark, fill, encrypt, OCR | Contract processing |
| [`doc-builder`](skills/doc-builder/) | Word docs: proposals, contracts, memos | Professional formatting |
| [`doc-coauthoring`](skills/doc-coauthoring/) | 3-stage writing: Context → Section Refinement → Reader Test | Catch blind spots |
| [`google-doc-creation`](skills/google-doc-creation/) | Branded Google Docs via API | Executive-ready styling |

### 📅 Daily Operations (13 skills)
*The CEO's day-to-day operating system.*

| Skill | Description | Key Pattern |
|-------|-------------|-------------|
| [`weekly-ceo-brief`](skills/weekly-ceo-brief/) | Week distilled to what matters | Lead with "so what" |
| [`meeting-prep`](skills/meeting-prep/) | Pre-meeting intelligence dossiers | Never walk in cold |
| [`post-meeting-brief`](skills/post-meeting-brief/) | Meeting → action with "not handled until in system" rule | Reading ≠ processing |
| [`email-composer`](skills/email-composer/) | CEO voice email drafting | No AI smell |
| [`voice-model`](skills/voice-model/) | Personal writing voice capture | Sound like you |
| [`scenario-war-room`](skills/scenario-war-room/) | Multi-variable what-if modeling | Plan for chaos |
| [`change-management`](skills/change-management/) | Rolling out org changes without chaos | ADKAR model |
| [`launch-strategy`](skills/launch-strategy/) | Product/feature launch planning | Coordinate the blast |
| [`support-triage`](skills/support-triage/) | Auto-classify and route inbound support queries | The dash-brief output |
| [`news-digest`](skills/news-digest/) | Marketplace surveillance against current pipeline entities | Verified Extracted Signal |
| [`slack-connector`](skills/slack-connector/) | Slack workspace integration — monitor, post, search, route | Team comms hub |
| [`sms-outreach`](skills/sms-outreach/) | SMS/WhatsApp multi-channel outreach with TCPA compliance | Beyond email |
| [`scheduling-infra`](skills/scheduling-infra/) | Meeting scheduling with pre/post automation | Calendar intelligence |

> 💡 **Want a personal AI operating system that compounds over time?** Explore [GFV Fellowship →](https://www.getfreshventures.com/fellowship?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit)

### 🚀 Growth Engine (17 skills)
*Marketing, content, and growth optimization.*

| Skill | Description | Key Pattern |
|-------|-------------|-------------|
| [`content-strategy`](skills/content-strategy/) | Pillars, calendars, buyer-stage keywords with A/B hook testing | System, not posts |
| [`social-engine`](skills/social-engine/) | Platform-native content with analytics dashboard | No AI slop |
| [`larry-loop`](skills/larry-loop/) | Algorithmic content loop with winner scoring | System over Creativity |
| [`eeat-content-pod`](skills/eeat-content-pod/) | 4-agent orchestration pod for verified content | Deployable content factory |
| [`seo-growth`](skills/seo-growth/) | Technical SEO, schema, site architecture, AI search opt | Discovery engine |
| [`seo-audit`](skills/seo-audit/) | Deterministic single-page SEO audits with Python scripts + HTML reports | Script + LLM two-layer |
| [`conversion-optimizer`](skills/conversion-optimizer/) | Forms, signups, landing pages, onboarding CRO | Fix the leaks |
| [`financial-analyst`](skills/financial-analyst/) | Ratio analysis, DCF, budget variance, rolling forecasts | Deep number work |
| [`copy-master`](skills/copy-master/) | 7-pillar copywriting with narrative submode | The Rule of One |
| [`ai-search-optimizer`](skills/ai-search-optimizer/) | Answer Engine Optimization — get AI to recommend your brand | Own the AI answer |
| [`social-scheduler`](skills/social-scheduler/) | Cross-post to 28+ channels with CEO approval gate | One command, all channels |
| [`ugc-video`](skills/ugc-video/) | Script-to-video UGC production with AI talking heads | Video at scale |
| [`voice-synth`](skills/voice-synth/) | AI voice synthesis for narration, podcasts, audio content | Sound human anywhere |
| [`geopolitical-monitor`](skills/geopolitical-monitor/) | Global intelligence with country instability scoring | International risk radar |
| [`paid-ads-strategy`](skills/paid-ads-strategy/) | Google, Meta, LinkedIn, Reddit, TikTok campaigns | Platform decision matrix |
| [`partnership-marketing`](skills/partnership-marketing/) | Influencer, affiliate, creator, referral, PR programs | Partnership-driven growth |
| [`programmatic-seo`](skills/programmatic-seo/) | Template-based SEO page generation at scale | Pages × data = traffic |

> 💡 **Need engineering sprints that compress 6-month roadmaps into 30 days?** Explore [Growth Engineering →](https://www.getfreshventures.com/solutions/growth-engineering?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit)

### 🛠️ Developer & DevOps (14 skills)
*Infrastructure skills for the technical operator.*

| Skill | Description | Key Pattern |
|-------|-------------|-------------|
| [`onboard`](skills/onboard/) | Interactive setup wizard for the GTM Kit | First-run config |
| [`context-prime`](skills/context-prime/) | Repository scanning for baseline context | Map before moving |
| [`product-spec`](skills/product-spec/) | Rough idea → structured 6-part PRD | Idea to spec |
| [`analyze-issue`](skills/analyze-issue/) | GitHub/Linear issue → implementation plan | Issue to plan |
| [`review-pr`](skills/review-pr/) | PR security, logic, and strategy review | Code gate |
| [`commit-fast`](skills/commit-fast/) | Automated semantic git commits | Ship. Now. |
| [`project-release`](skills/project-release/) | Governed release: version bump, changelog, tag, privacy audit | No manual steps |
| [`autoresearch`](skills/autoresearch/) | Autonomous skill optimization via repeated scoring | Self-improving skills |
| [`board-deck-builder`](skills/board-deck-builder/) | Board/investor update decks from live data | Data-driven slides |
| [`create-skill`](skills/create-skill/) | Create, modify, and optimize skills | Skills that build skills |
| [`import-skill`](skills/import-skill/) | Import external repos/skills into the kit | Zero-stone intake |
| [`feature-architect`](skills/feature-architect/) | Guided feature development with architecture focus | Architect first |
| [`hubspot-architect`](skills/hubspot-architect/) | HubSpot architecture for syncing and data pipelines | CRM engineering |
| [`dev-browser`](skills/dev-browser/) | Sandboxed browser automation with persistent Playwright pages | Headless-first |

### 🤖 Agent Intelligence (1 skill)

| Skill | Description | Key Pattern |
|-------|-------------|-------------|
| [`audio-briefing`](skills/audio-briefing/) | Synthesize outputs into executive audio briefings using cloned voice | Hear, don't read |

*(For the complete machine-readable catalog, see **[SKILLS-REGISTRY.md](SKILLS-REGISTRY.md)**.)*

---

## Free Kit vs. GFV Services

This kit is the **DIY foundation** of the Growth by Design™ methodology. For companies that need full deployment with autonomous agents and measurable revenue lift, GetFresh Ventures provides hands-on engineering sprints.

| | **GxD CEO AI Kit** (Free) | **GFV Services** (Engaged) |
|---|---|---|
| **Skills** | 194 AI skills, self-serve | Custom skill engineering + proprietary playbooks |
| **Intelligence** | Local SQLite memory | Proactive Intelligence Layer: 491K+ embeddings, 19 live sources |
| **Orchestration** | Manual integrations | OpenClaw: coordinated agentic swarms with audit trails |
| **Onboarding** | Self-serve wizard | White-glove executive intake + voice calibration |
| **Support** | Community / GitHub | Fractional GTM leadership + dedicated AI GTM Engineer |
| **Timeline** | Set your own pace | 90-day sprints with measurable lift |
| **Outcome** | Better-informed decisions | **4-14% revenue growth**, guaranteed |

<div align="center">
  <a href="https://www.getfreshventures.com/diagnostic?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit"><strong>📊 Take the Free Growth Diagnostic →</strong></a><br>
  <em>5 minutes. Custom scorecard. Prioritized gaps and next steps.</em>
</div>

---

## Safety & Privacy

| Guarantee | Details |
|-----------|---------|
| **📧 No Autonomous Sending** | AI never sends email, Slack, or any message without showing you the full draft and getting explicit "send it" approval |
| **🔒 Local-First Data** | Voice model, pipeline, and meeting prep live on YOUR machine in `~/ceo-brain` and `~/gtm-brain` — not uploaded to any cloud |
| **✅ Source Verification** | AI verifies claims against live data sources before asserting pipeline facts — it doesn't guess, it checks |
| **🛡 Credential Security** | API keys stored in your system's secure credential manager (macOS Keychain / Windows Credential Manager) |

---

## Repository Structure

```text
gxd-ceo-ai-kit/
├── bootstrap.sh               # macOS/Linux setup installer
├── bootstrap.ps1              # Windows setup installer
├── AGENT.md                   # The Growth by Design™ Persona
├── README.md                  # This file
├── CHANGELOG.md               # Version release history
├── SKILLS-REGISTRY.md         # Full index of all 194 capabilities
├── SKILL-AUTHORING-STANDARD.md# Architecture rules for new skills
├── GETTING-STARTED.md         # Executive walkthrough (first 30 min)
├── skills/                    # 194 Executable Domain Skills
│   ├── chief-of-staff/
│   ├── pipeline-pulse/
│   ├── eeat-content-pod/
│   └── ...
├── templates/                 # Reusable Markdown frameworks
├── workflows/                 # Operational multi-step playbooks
├── hooks/                     # Pre/post-execution safety validation
└── tools/                     # Underlying automation scripts
```

---

## Documentation

| Doc | Purpose |
|-----|---------|
| [AGENT.md](AGENT.md) | Growth by Design™ operating persona — all agents read this |
| [GETTING-STARTED.md](GETTING-STARTED.md) | Executive walkthrough for first-time setup |
| [CHANGELOG.md](CHANGELOG.md) | Full release history |
| [SKILLS-REGISTRY.md](SKILLS-REGISTRY.md) | Registry of all 194 active skills |
| [SKILL-AUTHORING-STANDARD.md](SKILL-AUTHORING-STANDARD.md) | Governance standard for writing new skills |

---

## About Growth by Design™

**Growth by Design™** is the proprietary methodology of [GetFresh Ventures](https://www.getfreshventures.com?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit), an AI-native growth engineering firm based in North Vancouver, Canada. We embed agentic AI into GTM systems for growth-stage CEOs through fixed-fee, 90-day engineering sprints that deliver measurable revenue lift.

### Our Solutions

| Stage | Solution | What You Get |
|-------|---------|-------------|
| **Pre-Revenue** | [Revenue Foundations](https://www.getfreshventures.com/solutions/revenue-foundations?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit) | First revenue system + Personal AI OS |
| **Growth Stage** | [AI Operations Engineering](https://www.getfreshventures.com/solutions/ai-revops?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit) | AI agents in your CRM, pipeline, and customer success stack |
| **Growth Stage** | [Fractional GTM + AI Co-Pilot](https://www.getfreshventures.com/solutions/fractional-gtm?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit) | Senior GTM leadership without the $400K hire |
| **Scale** | [Growth Engineering](https://www.getfreshventures.com/solutions/growth-engineering?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit) | 6-month roadmaps compressed into 30-day deliveries |
| **Exit-Ready** | [Exit Engineering](https://www.getfreshventures.com/solutions/exit-engineering?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit) | Operations redesigned for 1.5-3x higher multiples |

### Stay Connected

- **Newsletter:** [Growth by Design™ on Substack](https://growthbydesign.substack.com/) — Founder-first publication on scaling sustainably with AI
- **Website:** [The CEO AI Kit](https://www.getfreshventures.com/ceo-ai-kit?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit) | [GetFresh Ventures](https://www.getfreshventures.com?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit)
- **Repository:** [github.com/GetFresh-Ventures/gxd-ceo-ai-kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit)

---

<div align="center">
  <strong>Built by operators who have sat in your seat.</strong><br>
  <em>Fixed-fee execution. Working systems in 90 days. Measurable lift guaranteed.</em><br><br>
  <a href="https://www.getfreshventures.com/contact?utm_source=github&utm_medium=readme&utm_campaign=ceo_ai_kit">🤝 Book a Discovery Call →</a>
</div>
