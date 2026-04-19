---
hide:
  - navigation
---

# Projects

*A Project is a persistent workspace with its own instructions and files. Set it up once, skip the re-briefing forever.*

!!! tip "Read this first if nothing else"
    Projects are what turn Claude from a chat window into a real workspace. Teams that set up Projects well get hours back every week. Teams that do not set up Projects keep re-briefing Claude from scratch every time and wonder why it feels slow.

## What a Project is

Every new chat inside a Project inherits its instructions and its attached files. You set up the context once, and from then on every conversation inside that Project already knows who you are, what the project is, and what "good" looks like.

## How to create one

1. Click **Projects** in the sidebar, then **Create project**.
2. Name it (e.g., "Creative Summit 2026").
3. Add a description (optional but useful).
4. Set **Project instructions.** This is free text Claude will read at the start of every chat in this project. Tell it who you are, what the project is, what tone to use, what it should avoid.
5. Upload **Project knowledge** (optional). Drop in the brand guidelines, past decks, past emails, the brief. These files are available in every chat in this project.

## What to put in Project instructions

Keep it short and high-signal. A good template:

```
I am the marketing lead at MMA Vietnam. This project is for [event/workstream].
Key context: [3-5 bullet points].
Style: no em dashes, direct and CTA-driven, bold but not salesy. Use "MMA" not "mma.".
When I ask for drafts, give me one version unless I ask for options.
```

## What to put in Project knowledge

Files you keep referring to:

- MMA Brand Guidelines (draft 4 or whatever is current)
- Past event decks and emails you want Claude to match in tone
- The current brief or strategy deck
- Style examples (a LinkedIn post you liked, an email you wrote well)

Do **not** upload: client confidential material, unreleased financials, signed contracts, or anything you would not paste into a group chat.

## Why this matters

Every chat in a Project already knows the context. You can open a new chat and just say "draft the invite for sponsors" and Claude already knows what event, what audience, what tone. This is the single biggest productivity gain in the app.

## Ready-made Project scaffold (optional)

Setting up a Project from scratch is the hardest part. What goes into the instructions, what files belong in the knowledge base, how do you structure it so it still holds up three months in. Keeping Claude efficient as the project grows is harder still. More files mean more context to load, more tokens burned per message, slower responses, and more re-explaining.

A handful of structured `.md` files solves both problems. They give Claude a compact, always-current snapshot of who you are, what the project is, and where things stand, so every conversation starts from the right place without re-reading everything.

The **project-setup** skill is optional. It is what Yen found works best after running both work and personal projects with Claude over the past year. It runs a five-minute interview and produces a starter kit of five foundational files:

- **CLAUDE.md** → how Claude should work in this project
- **INITIAL_CONTEXT.md** → day-one background, who this is for, what problem it solves
- **DIARY.md** → a running log of decisions and turning points
- **SOUL.md** → the tone and personality you want Claude to use
- **PROJECT_STATUS.md** → a living dashboard showing where the project is right now, plus a workspace map

*New to `.md` files? See the [Markdown primer in Claude 101](claude-101.md#markdown-files) for what they are and how to open them.*

Paste the first two into Project instructions, upload the rest as Project knowledge, and your Project is structured from day one.

!!! note "Prefer something lighter?"
    You can also use the built-in `/init` command to set up a project. It is simpler, asks fewer questions, and gets you a basic scaffold fast. Neither option is "correct". Pick whichever fits how you work, and feel free to adapt the files or build your own structure.

!!! tip "Already have files in your folder?"
    You can still run `/project-setup`. Include this in your opening message so it reads what you already have and suggests improvements, rather than scaffolding from scratch:

    > Note that I already have some files and folders in this project. Make sure you read those first for initial context, as well as to suggest a more optimal folder and file structure.

[:octicons-download-24: Download project-setup.skill](assets/project-setup.skill){ .md-button .md-button--primary }

!!! note "Known quirk"
    The `project-setup` skill has a minor display error during setup when used in Cowork. It works best in Claude Code (and terminal). The error is cosmetic only and does not affect the generated files or their quality.

!!! note "Regret pill"
    Tried it and do not like it? Nothing is locked in. The five files are plain `.md` text, not code, and there is no background process to uninstall. Delete the files you do not want, edit them until they fit, or throw them all out and switch to `/init` or your own structure. Your Project keeps working either way. If you have already written content into a file you want to keep, copy it out before deleting.

Installation and live walkthrough are covered in the Claude Cowork training session.

[:octicons-arrow-up-24: Back to top](#){ .md-button }

---

**Last reviewed:** April 2026
