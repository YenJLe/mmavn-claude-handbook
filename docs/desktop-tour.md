# Desktop App Tour

*A walkthrough of the Claude desktop app: where everything lives, what each feature does, and how the pieces fit together.*

!!! note "Screenshots"
    Screenshots will be added after the first team training session, so they reflect the exact build the team is using. In the meantime, follow along by opening the app alongside this page.

## 1. First launch

When you open Claude for the first time, you see a single chat window. Cursor in the input box at the bottom. A sidebar on the left. That is the entire app.

Three things worth knowing before you do anything else:

- **Every message you send is a new conversation unless you are inside an existing chat.** There is no "save" button because everything is saved automatically.
- **Conversations appear in the left sidebar.** Click any one to pick up where you left off.
- **You can attach files by dragging them into the message box** or clicking the paperclip icon.

## 2. The sidebar

From top to bottom, the left sidebar gives you:

- **New chat button.** Starts a fresh conversation with no prior context.
- **Search.** Finds text across all your past conversations. Useful when you half-remember asking Claude something three weeks ago.
- **Projects.** A list of your saved Projects. More on these below.
- **Recent chats.** Your conversation history, newest first. Click one to resume.
- **Your name / account** at the very bottom. Click to access settings, switch models, turn memory on or off, or sign out.

## 3. Starting a new chat

Click the **New chat** button (or use the keyboard shortcut, usually Cmd/Ctrl + N). You get an empty conversation.

Type your prompt. Press Enter to send, or Shift + Enter for a line break.

A new chat has **no memory of other chats**. If you want Claude to know something from a previous conversation, you have to tell it or paste it in. This is why Projects exist (next section).

## 4. Projects: the single biggest time-saver { #projects }

A **Project** is a persistent workspace with its own instructions and files. Every new chat inside a project inherits both. This means you set up the context once and never re-brief Claude again for that project.

!!! tip "Do not skip this section"
    If you read nothing else on this site, read this. Projects are what turn Claude from a chat window into a real workspace. Teams that set up Projects well get hours back every week. Teams that do not set up Projects keep re-briefing Claude from scratch every time and wonder why it feels slow.

### How to create one

1. Click **Projects** in the sidebar, then **Create project**.
2. Name it (e.g., "Creative Summit 2026").
3. Add a description (optional but useful).
4. Set **Project instructions.** This is free text Claude will read at the start of every chat in this project. Tell it who you are, what the project is, what tone to use, what it should avoid.
5. Upload **Project knowledge** (optional). Drop in the brand guidelines, past decks, past emails, the brief. These files are available in every chat in this project.

### What to put in Project instructions

Keep it short and high-signal. A good template:

```
I am the marketing lead at MMA Vietnam. This project is for [event/workstream].
Key context: [3-5 bullet points].
Style: no em dashes, direct and CTA-driven, bold but not salesy. Use "MMA" not "mma.".
When I ask for drafts, give me one version unless I ask for options.
```

### What to put in Project knowledge

Files you keep referring to:

- MMA Brand Guidelines (draft 4 or whatever is current)
- Past event decks and emails you want Claude to match in tone
- The current brief or strategy deck
- Style examples (a LinkedIn post you liked, an email you wrote well)

Do **not** upload: client confidential material, unreleased financials, signed contracts, or anything you would not paste into a group chat.

### Why this matters

Every chat in a Project already knows the context. You can open a new chat and just say "draft the invite for sponsors" and Claude already knows what event, what audience, what tone. This is the single biggest productivity gain in the app.

### Skip the blank page: the project-setup skill

Setting up a Project from scratch is the hardest part. What goes into the instructions, what files belong in the knowledge base, how do you structure it so it still holds up three months in.

The **project-setup** skill runs you through a five-minute interview and produces a starter kit of five foundational files:

- **CLAUDE.md** → how Claude should work in this project
- **INITIAL_CONTEXT.md** → day-one background, who this is for, what problem it solves
- **DIARY.md** → a running log of decisions and turning points
- **SOUL.md** → the tone and personality you want Claude to use
- **PROJECT_STATUS.md** → a living dashboard showing where the project is right now, plus a workspace map

*New to `.md` files? See the [Markdown primer in Claude 101](claude-101.md#markdown-files) for what they are and how to open them.*

Paste the first two into Project instructions, upload the rest as Project knowledge, and your Project is structured from day one.

!!! note "A note before you download"
    Yen put this skill together. She finds it fits well for both her work and personal-life projects, but there are plenty of ways to set up a Project and no single right answer. Give it a try, and if a different structure suits how you work, feel free to adapt the files or build your own.

[:octicons-download-24: Download project-setup.skill](assets/project-setup.skill){ .md-button .md-button--primary }

!!! note "Known quirk"
    This skill has a minor display error during setup when used in Cowork. It works best in Claude Code (and terminal). The error is cosmetic only and does not affect the generated files or their quality.

Installation and live walkthrough are covered in the Claude Cowork training session.

## 5. File uploads

In any chat, you can upload files by:

- Dragging them into the message box.
- Clicking the paperclip or plus icon.
- Pasting an image directly (screenshots work).

Supported formats: PDF, Word, PowerPoint, Excel, CSV, images (PNG, JPG), and plain text.

Limits: up to 20 files per chat, 30MB each.

Claude reads the full content of each file, including tables inside PDFs and text inside images. You do not need to describe what the file contains; just attach and ask.

## 6. Artifacts: the side panel

When Claude produces something substantial, a side panel opens on the right. This is an **Artifact**. Examples of what shows up there:

- A written document (a draft email, a one-pager, an article)
- A table (sponsor matrix, speaker shortlist, budget)
- A piece of code (rare for this team, but supported)
- A diagram (flowcharts, org charts)
- A small working prototype (e.g., an interactive HTML preview)

Artifacts are useful because:

- You can **edit them** directly in the panel.
- You can ask Claude to **revise them**, and it updates in place.
- You can **copy or download** the final version cleanly, without scrolling through chat.

If you do not see the side panel and think Claude should have opened one, ask: "Put that in an artifact."

## 7. Voice mode

Click the microphone icon in the input box. Claude listens, transcribes what you say, and responds by voice (or text, depending on settings).

Useful for:

- Thinking out loud when you are stuck.
- Dictating a rough draft while walking around.
- Asking quick questions when your hands are full.

Vietnamese transcription works well. Switch language in settings if you want the voice output in Vietnamese too.

## 8. Search across conversations

The search box in the sidebar (Cmd/Ctrl + K) searches your **entire chat history**, not just the current conversation. Type any phrase and it surfaces every chat where that phrase appeared.

Useful when you know you talked about something but cannot remember when.

## 9. Settings worth knowing

Click your name at the bottom of the sidebar to open settings. The ones worth adjusting:

- **Default model.** Set it to Sonnet for daily work. You can override per-chat.
- **Memory.** Claude can remember facts about you across chats. You can view, edit, or clear what it remembers. Turn it on for personal efficiency; turn it off if you are doing sensitive work.
- **Appearance.** Light, dark, or auto.
- **Incognito / temporary chats.** Chats that are not saved and do not train anything. Use for one-off sensitive queries.

## 10. Keyboard shortcuts worth learning

Even five of these will change how fast you move.

| Shortcut              | What it does                              |
|-----------------------|-------------------------------------------|
| Cmd/Ctrl + N          | New chat                                  |
| Cmd/Ctrl + K          | Search across all conversations           |
| Cmd/Ctrl + /          | Show all shortcuts                        |
| Shift + Enter         | New line in the message box               |
| Enter                 | Send message                              |
| Cmd/Ctrl + Shift + O  | Open a specific project                   |
| Esc                   | Stop Claude mid-response                  |

## 11. A sensible daily workflow

Once you are set up, most days look like this:

1. Open Claude. Pick the right Project (or a new chat if it is a one-off).
2. Upload any relevant files for this specific task.
3. Write the prompt using the [reusable brief template](prompting.md#a-reusable-brief-template).
4. Review the artifact. Ask for specific changes in the same chat.
5. Copy or download the final version. Close the chat. Move on.

Five minutes of setup per Project saves you hours of re-briefing across the week.

---

**Next step:** [Prompting Basics](prompting.md) → the tips that actually change output quality.

**Last reviewed:** April 2026
