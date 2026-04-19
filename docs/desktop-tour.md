---
hide:
  - navigation
---

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

## 4. Projects { #projects }

Projects are the single biggest productivity gain in the app. There is enough to cover that they live on their own page.

[:octicons-arrow-right-24: Go to Projects](projects.md){ .md-button .md-button--primary }

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
