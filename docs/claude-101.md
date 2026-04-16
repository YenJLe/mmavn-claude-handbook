# Claude 101

*What Claude is, how it compares to ChatGPT and Gemini, and which features actually matter for MMA work.*

## What Claude is

Claude is an AI assistant built by Anthropic. It reads what you write, thinks about it, and responds in text, code, tables, or structured documents. The current model family is **Claude 4.6** (Opus, Sonnet, and Haiku), each tuned for different speed and reasoning needs. Opus is the smartest and slowest. Haiku is the fastest and cheapest. Sonnet sits in the middle and is what most of us use day to day.

## Claude vs. ChatGPT vs. Gemini: the honest comparison

All three are strong. They are not identical, and the differences matter for the work we do.

### Where Claude is stronger

- **Long-form writing and nuance.** Claude follows complex briefs more faithfully and keeps tone consistent across long documents. For decks, articles, and client copy, it usually needs fewer rewrites.
- **Following instructions literally.** If you say "no em dashes, under 200 words, in bullet form," Claude tends to respect all three. The others often drop one.
- **Document analysis.** Stronger at reading PDFs, spreadsheets, and uploaded files accurately. Less prone to making up numbers that are not there.
- **Honest about limits.** Claude tells you when it does not know something. ChatGPT and Gemini are more likely to produce a confident-sounding but wrong answer.
- **Coding and structured workspaces.** Claude Code (for developers) and Claude Cowork (for knowledge work) are best-in-class for turning folders and projects into persistent AI workspaces. More on this in a later training.

### Where ChatGPT is stronger

- **Image generation.** DALL-E is built in and produces solid results with minimal prompting.
- **Ecosystem maturity.** The Custom GPTs marketplace is large, with pre-built assistants for almost any niche task.
- **Voice mode.** More conversational and expressive than Claude's or Gemini's.
- **Video understanding.** Can analyse video frames, which Claude cannot.

### Where Gemini is stronger

- **Google Workspace integration.** Native in Gmail, Docs, Sheets, Slides, and Drive. If your day lives inside Google, Gemini is already sitting next to your work.
- **Real-time information.** Uses Google Search under the hood, so it is stronger on breaking news, live data, and anything time-sensitive.
- **Video and audio understanding.** Handles full video files and long audio natively, which neither Claude nor ChatGPT match.
- **Very long context.** Gemini Pro handles up to 2 million tokens, the largest of the three, useful for dumping a full library of reports into one chat.
- **Free tier.** More generous than the others, which matters for teams trialling AI without a paid plan.

!!! abstract "Our take for MMA"
    Claude is the better default for writing, analysis, and brand-voice work, which is most of what we do. Use ChatGPT when you need image generation or a specific custom GPT. Use Gemini when your work lives inside Google Workspace or you need video analysis. Most of the team will settle on Claude for 80% of tasks and reach for the others only when a specific feature is needed.

## Features that actually matter for MMA work

### 1. Projects

A Project is a persistent workspace with its own files, instructions, and chat history. Think of it like a shared folder that Claude reads every time you open a new chat inside it. Drop in brand guidelines, templates, and past decks once, and every future conversation in that project already knows the context. This is the single biggest time-saver for recurring work.

> **Use case:** one project per major event (Creative Summit, INNOVATE, SMARTIES). Upload the brand deck, past copy, and sponsor list once. Future drafts take 30 seconds instead of 10 minutes of re-briefing.

### 2. File uploads

Claude reads PDFs, Word docs, PowerPoint, Excel, CSV, images, and plain text. Up to 20 files per chat, 30MB each. It extracts text, tables, and image content, and answers questions across all of it in one pass.

> **Use case:** paste the event feedback survey as a CSV and ask "what are the top three complaints and which segments do they come from?"

### 3. Artifacts

When Claude produces something substantial (a document, code, a diagram, a working prototype), it appears in a panel next to the chat instead of inside the message. You can edit it, ask for revisions, or copy it out cleanly. Much better than scrolling through a wall of chat to find the final version.

### 4. Extended thinking

For hard problems, you can turn on extended thinking and Claude will reason through the problem visibly before answering. Slower, but noticeably better output on strategy questions, complex analysis, and multi-step decisions. Off by default. Turn it on when the stakes are high.

### 5. MCP connectors

Claude can connect directly to Gmail, Google Calendar, Microsoft 365 (Outlook, SharePoint, Teams), and other tools. Once connected, it can search your email, read calendar invites, pull SharePoint docs, and act on them. This turns Claude from a chat window into something closer to an assistant that can actually see your work.

> **Use case:** "find the three most recent emails about SFDC and summarise the open asks."

### 6. Skills

Skills are reusable capabilities you install once and call anytime. Think of them as saved workflows. There are pre-built skills for creating slide decks, editing Word docs, building spreadsheets, designing posters, and more. When a skill is relevant, Claude uses it automatically.

> **Use case:** ask for a slide deck and Claude pulls in the slide-deck skill, producing a proper .pptx instead of a text outline.

### 7. Web search

Claude can search the web when you ask. It is off by default in some interfaces and on in others. Useful for anything time-sensitive. Always verify quotes and numbers.

### 8. Voice mode

Tap the mic and talk to Claude. Works well for thinking out loud, dictating rough drafts, or asking questions when you are away from the keyboard. It transcribes cleanly, including in Vietnamese.

### 9. Memory

Claude remembers facts about you across conversations if you let it. It will save things like your role, your team, your preferences, and past decisions, and recall them when relevant. You can view, edit, or clear memory anytime in settings.

### 10. Claude Cowork (preview)

The feature we will cover in the next training. Turns a local folder on your computer into a persistent AI workspace with its own instructions, decision log, and status tracker. This is how we run the MMA Vietnam project internally. More in the second session.

## The one rule that changes everything

Claude's core strength is context. It was built to hold long briefs in its head, draw on the files you attach, and keep tone and constraints consistent across a full document. That strength only shows up when you feed it context. Paste the brand guidelines. Upload the brief. Share the example you liked. Tell it who the audience is, what has been tried, and what "good" looks like.

The difference between a weak output and a strong one is almost always how much context you provided. A one-line ask gets a one-line generic answer. A full brief gets work that fits. Claude responds to what you feed it. Garbage in, polite garbage out.

## Your responsibilities

- Do not paste client confidential material without checking with the project lead first.
- Always review Claude's output before sending or publishing. You are accountable, not the tool.
- Verify numbers, names, dates, and quotes against the source.
- Flag anything Claude gets wrong so the team can learn from it.

---

**Next step:** [Desktop App Tour](desktop-tour.md) → see where everything lives in the app, then read [Prompting Basics](prompting.md) to get more out of each chat.

**Last reviewed:** April 2026
