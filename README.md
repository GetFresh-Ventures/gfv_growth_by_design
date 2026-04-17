# GetFresh GTM Enablement Kit

**Edge-Native Go-to-Market Operating System that turns any coding assistant into a personalized Chief of Staff.**

[![Version](https://img.shields.io/badge/version-1.32.2-blue.svg)](VERSION) · [Changelog](CHANGELOG.md) · [Release Notes](https://github.com/GetFresh-Ventures/gfv_growth_by_design/releases)

---

## What This Is

A plug-and-play **Edge-Native Go-to-Market Operating System** that turns Claude Code, Cursor, Gemini, or Copilot into a personalized, autonomous Chief of Staff. 

This kit enables the proprietary **Growth by Design (GxD)** architecture directly within your local environment. 

**Runtime:** Local / Edge-Compute · 73+ Domain Skills · SQLite FTS5 Memory Caching

**The Brand (GxD)**: Growth by Design is the architecture of predictable revenue, uniting Marketing, Sales, and RevOps data into a single, unified ontology.

**The Solution**: An Edge-Native intelligence layer that installs directly onto your laptop. It removes the friction between strategic planning and agentic execution, allowing you to orchestrate complex GTM strategies autonomously.

---

## What's New in v1.32.2
- **Unbiased Architecture & Bug Fixes**: Permanently decoupled legacy proprietary pipelines (`claude-mem`, `ccflare`, `claude_memory.py`) from macOS boots, and patched a catastrophic path hallucination across 72 skills.
- **E-E-A-T Content Pod**: Integrated a new 4-agent orchestration wrapper (`eeat-content-pod`) into the native deployment loop.

---

## Architecture

```
┌───────────────────────────────────────────────────────────────┐
│  AI Coding Assistants: Cursor · Windsurf · Claude Code        │
└────────────────────────────┬──────────────────────────────────┘
                             │
                             ▼
┌───────────────────────────────────────────────────────────────┐
│  AGENT.md (The Global Persona)                                │
│  Defines identity, constraints, memory rules, and syntax      │
│  Guides the LLM through the Sherpa UX Educational Protocol    │
└────────────────────────────┬──────────────────────────────────┘
                             │
                             ▼
┌───────────────────────────────────────────────────────────────┐
│  GetFresh GTM Enablement Kit                                  │
└──────┬──────────────┬─────────────────┬───────────────────────┘
       │              │                 │
       ▼              ▼                 ▼
┌──────────────┐ ┌─────────────┐ ┌──────────────────────┐
│  73 Domain   │ │ Background  │ │ Local CEO Brain      │
│  Skills      │ │ Telemetry   │ │ (SQLite FTS5 Edge)   │
│  (C-Suite,   │ │ (Python)    │ │ Unified Ontology     │
│   Ops, Dev)  │ └──────┬──────┘ └──────────────────────┘
└──────┬───────┘ ┌──────┴──────┐
       │         │  Event Hooks│  
       │         │  Pre/Post   │
       │         │  Execution  │
       │         └─────────────┘
 ┌─────┴──────────────────────────────────┐
 │  Data Integrations & Web Protocols     │
 │  Linear · HubSpot · Slack · ServiceTitan│
 │  Google Ads · SEMrush · Analytics       │
 └────────────────────────────────────────┘
```

**Zero SaaS Telemetry (Total Privacy)**:
When you upload financial documents to a web wrapper, you surrender data custody. Running this Executive Kit locally inside an IDE ensures that your data stays strictly on your machine and communicates *only* via secured API endpoints you control.

---

## How It Works

### The Agent Persona (AGENT.md)
The `AGENT.md` file defines the identity of the AI. It sets operational boundaries, memory rules, and ensures the LLM speaks in a decisive, action-oriented tone rather than generic "AI speak".
**Sherpa Protocol:** For non-technical users, it conditionally triggers "Working Out Loud" educational narratives to teach IDE command fluency.

### Edge-Native Memory
Local memory ensures contexts survive beyond a single terminal session.
- **`~/ceo-brain/`**: The runtime namespace storing your local profile (`profile.json`), expertise level, and historical SQLite databases.
- Background hooks run `session-start` and `session-stop` automatically.

### The Skills Layer
Over 73 discrete `.md` instruction files acting as programmatic apps. When you say "Run the weekly pipeline brief", the agent dynamically retrieves the `weekly-pipeline-brief` skill and follows its deep operational playbook step-by-step.

---

## Maslow Priority Hierarchy

All work is tiered based on your operational autonomy constraint inside `profile.json`.

| Tier | Name | Focus |
|------|------|-------|
| **Beginner** | Guided Operations | Manual confirmations on all tools, plain English explanations. |
| **Intermediate**| Partial Autonomy | Approves standard commands, requires hooks for sensitive actions. |
| **Advanced** | Hyper-Execution | Unlocked shell commands, no summaries needed, pure speed. |

---

## Core Integrations

| System | Role |
|----------|------|
| **Linear** | Project ops, sprint tracking, and blocked issue routing |
| **HubSpot** | CRM data, deal extraction, and sequence alignment |
| **ServiceTitan** | Dispatch mapping, tech routing, revenue tracking |
| **Slack** | Team communications, crisis monitoring, and auto-dispatch |
| **Google Ads** | PPC campaign structure, ROAS checking, landing pages |
| **CAAI** | Proprietary GetFresh centralized intelligence model |

---

## Governance & CI/CD

### Event Hooks
We wrap code actions with lifecycle triggers:
- `session-start.py` — Hydrates previous cross-session context.
- `session-stop.py` — Archives findings and indexes local SQLite caching.
- `pre-send-review.py` — Security scanner preventing accidental data drops before external API execution.

### Fast Iteration
Changes happen seamlessly within the IDE workspace. All backgrounds scripts execute in `$GFV_CEO_BRAIN/.core` silently.

---

## Key Engines & Skills

A subset of the 73 available skills:

| Skill | Purpose |
|--------|---------|
| `/chief-of-staff` | Orchestration layer — routes questions to the right advisor(s). |
| `/ceo-advisor` | Strategic direction, vision setting, investor narrative. |
| `/cfo-advisor` | Cash management, financial modeling. |
| `/pipeline-pulse`| Weekly pipeline health snapshot with trends, velocity metrics. |
| `/larry-loop` | Systematically generates, distributes, and iterates on marketing content. |
| `/ui-ux-pro-max` | AI-powered design intelligence scaling 161 industry-specific UI systems. |
| `/project-release`| Governed release workflow for GitHub/Linear propagation. |

*(For the complete machine-readable catalog, see **[AGENT-GUIDE.md](AGENT-GUIDE.md)**).*

---

## Documentation

| Doc | Purpose |
|-----|---------|
| [AGENT.md](AGENT.md) | Universal operating manual — all agents read this |
| [CHANGELOG.md](CHANGELOG.md) | Full release history |
| [SKILLS-REGISTRY.md](SKILLS-REGISTRY.md) | Registry of all active skills |
| [SKILL-AUTHORING-STANDARD.md](SKILL-AUTHORING-STANDARD.md) | Governance standard for writing new skills |
| [GETTING-STARTED.md](GETTING-STARTED.md) | Guided walk-through for first-time operation |

---

## Quick Start

```bash
git clone https://github.com/GetFresh-Ventures/gfv_growth_by_design.git ~/Documents/GTM-Enablement-Kit
cd ~/Documents/GTM-Enablement-Kit
./bootstrap.sh          # Mac/Linux
# .ootstrap.ps1       # Windows
```

Then open `~/Documents/GTM-Enablement-Kit` inside **Cursor** and type `/onboard` in the Composer chat.

---

## License & Repo

- **Repository:** [github.com/GetFresh-Ventures/gfv_growth_by_design](https://github.com/GetFresh-Ventures/gfv_growth_by_design)
- **Primary use:** Go-To-Market Enablement Operating System for GetFresh Ventures.
