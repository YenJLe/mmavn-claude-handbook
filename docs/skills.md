# MMA Skills

*Skills are the "already done for you" layer of Claude. Pre-loaded knowledge and workflows tailored to MMA and to the work we do, firing automatically when relevant.*

## What skills are

Skills are reusable capabilities Claude uses to handle specific kinds of work. The MMA admin has installed five plugins in your workspace, plus a handful of built-in commands. Each plugin bundles a set of related skills. Together they cover MMA org context, brand voice, marketing workflows, productivity, Slack, and enterprise search.

!!! tip "How skills work"
    Everything listed below is pre-installed in your workspace. You can also add your own at any time, see [Build your own](#build-your-own). Once a skill lives in your workspace it fires automatically when relevant. You do not need to enable or name it. Type `/` in any chat to see the full list currently available to you.

## Skills installed in the MMA workspace

### `mma-skills-and-context`

MMA's own plugin: org knowledge, brand voice, content formats, and workflow helpers built for our work.

| Skill | What it does |
|-------|--------------|
| `mma-org-context` | Structure, programs, events, leadership, SharePoint, Slack channels |
| `mma-brand-guidelines` | Naming rules, colors, fonts, visual identity |
| `mma-writing-style` | Tone and formatting standards for MMA copy |
| `mma-pptx-builder` | Build decks using MMA templates and branding |
| `content-draft` | General-purpose content drafting in MMA voice |
| `content-strategy` | Content planning for programs and campaigns |
| `press-release` | Press releases formatted and toned for MMA |
| `social-post` | LinkedIn and social copy in MMA voice |
| `email-draft` | Professional email drafting |
| `case-study` | Case study write-ups of MMA program results |
| `event-promo` | Copy and assets for MMA event promotion |
| `member-comms` | Onboarding, renewals, and member-facing comms |
| `meeting-followup` | Post-meeting recaps and follow-up emails |
| `briefing-prep` | Pre-meeting briefings and exec summaries |
| `launch-strategy` | Launch plans for programs and campaigns |
| `research` | General research workflow |
| `research-brief` | Structured research briefs for Think Tanks |
| `lab-summary` | Summaries of Future Lab / CAP lab results |
| `slack-summary` | Summarize Slack threads and channels |
| `sharepoint-find` | Locate MMA documents in SharePoint |
| `asana-task` | Create and format Asana tasks |
| `zapier-workflow-builder` | Design Zapier automation workflows |

### `marketing`

General-purpose marketing workflows. Not MMA-specific, so pair with `mma-brand-guidelines` when you want output in MMA's voice.

| Skill | What it does |
|-------|--------------|
| `draft-content` | Draft marketing content of any format |
| `content-creation` | Generate campaign content |
| `email-sequence` | Build multi-step email sequences |
| `campaign-plan` | Full campaign planning templates |
| `competitive-brief` | Competitive landscape briefs |
| `brand-review` | Check copy against brand guidelines |
| `seo-audit` | Audit a page or site for SEO |
| `performance-report` | Marketing performance reporting |

### `productivity`

Personal workflow, memory, and task management.

| Skill | What it does |
|-------|--------------|
| `start` | Begin a work session with a briefing |
| `update` | End-of-day or status updates |
| `task-management` | Task tracking workflows |
| `memory-management` | Manage Claude's cross-chat memory |

### `slack-by-salesforce`

Slack search, summaries, drafting, and posting.

| Skill | What it does |
|-------|--------------|
| `slack-search` | Search across Slack |
| `find-discussions` | Locate relevant threads |
| `summarize-channel` | Summarize a channel's recent activity |
| `channel-digest` | Digest of activity across channels |
| `standup` | Daily standup summaries |
| `draft-announcement` | Draft Slack announcements |
| `slack-messaging` | Compose and post Slack messages |

### `enterprise-search`

Search and synthesis across your connected enterprise sources.

| Skill | What it does |
|-------|--------------|
| `search` | Run an enterprise-wide search |
| `search-strategy` | Plan a multi-source search |
| `source-management` | Manage which sources Claude searches |
| `knowledge-synthesis` | Synthesize findings from multiple sources |
| `digest` | Produce digests from search results |

### Built-in commands

Shipped with Claude by default.

| Command | What it does |
|---------|--------------|
| `init` | Initialize a project workspace |
| `review` | Review a pull request or document |
| `security-review` | Security review of pending changes |

## A worked example

Ask Claude: *"Draft a press release announcing the next Think Tank result."*

Behind the scenes, `press-release` handles the format (headline, dateline, quotes, boilerplate) while `mma-brand-guidelines` and `mma-writing-style` make sure the copy uses "Marketing + Media Alliance" on first mention, lands the right tone, and avoids off-brand phrasing. You get a near-final draft without naming any of them.

## Build your own

Anyone can build a skill in under five minutes.

1. Go to [claude.ai/customize/skills](https://claude.ai/customize/skills), or ask Claude to create one for you.
2. Give it three things:
    - **Name.** What you will call it (e.g., `weekly-report`).
    - **Description.** When it should activate (e.g., "Use when drafting weekly status reports for MMA Vietnam").
    - **Instructions.** The step-by-step rules you want Claude to follow.
3. Save. It is now available in every conversation.

Good candidates for custom skills: recurring formats you keep re-explaining (a specific report type, a meeting-prep template, a proposal structure), or anything with fixed steps that benefits from being done the same way every time.

[:octicons-arrow-up-24: Back to top](#){ .md-button }

---

**Last reviewed:** April 2026
