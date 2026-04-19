---
hide:
  - navigation
---

# Prompting Basics

*The handful of prompting habits that actually change the quality of what Claude gives you back. Each tip has a weak example and a strong example so you can see the difference.*

!!! abstract "Why context is the whole game"
    Claude's strongest capability is context engineering: understanding a brief, holding it across a long conversation, and producing work that fits. That strength is dormant until you feed it. Every tip on this page is, at heart, a different way of giving Claude better context. A one-line ask gets a one-line generic answer. A full brief gets work that fits on the first try.

There is no special prompting language. You are just briefing a smart colleague who does not know your project. The habits below are what that brief looks like when done well.

## 1. Give context before you ask

Claude has no idea what you are working on, who the audience is, or what "good" looks like in your world. Tell it first.

**Weak**

> Write me an email to invite sponsors to Creative Summit.

**Strong**

> I am the marketing lead at MMA Vietnam. Creative Summit 2026 is our flagship half-day event for senior creative and marketing leaders in Ho Chi Minh City on April 24. I want to invite three CMOs from categories we do not yet have sponsorship coverage for: banking, edtech, and QSR. The tone should be confident and peer-to-peer, not salesy. Max 180 words. Write the email.

The strong version front-loads the role, the event, the audience, the tone, and the constraint. You will still need to edit, but you get a usable draft on the first try instead of the third.

## 2. Show an example of "what good looks like"

Adjectives are weak signals. Examples are strong ones. One example of a tone, structure, or format you want Claude to match beats a paragraph of descriptors.

**Weak**

> Write a LinkedIn post announcing INNOVATE 2026 in a confident, forward-looking tone.

**Strong**

> Write a LinkedIn post announcing INNOVATE 2026 in the same voice and structure as this past post we wrote:
>
> [paste your best past LinkedIn post here]
>
> Details for the new post: 21 to 22 May, Ho Chi Minh City, theme is "The Next Growth Frontier," registrations open now.

Claude will reverse-engineer the rhythm, length, and phrasing of your example and apply it.

## 3. Be specific about format

Say the length, the structure, the tone, and the language. Vague inputs produce vague outputs.

**Weak**

> Summarise this brief.

**Strong**

> Summarise this brief in three bullets under the headings "What we are doing," "Who it is for," and "What success looks like." Each bullet under 25 words. Neutral tone. Keep it in English.

If you need Vietnamese, say so. If you want a table, say so. If you want exactly five items, say exactly five.

## 4. Upload the source, do not paraphrase it

If the document is the thing, attach it. Claude reads PDFs, Word, PowerPoint, Excel, CSV, and images directly. Your paraphrase of a 40-page deck is lossy; the deck itself is not.

**Weak**

> The sponsorship deck basically has three tiers called Platinum, Gold, and Silver, and the prices are roughly like USD 15k, 10k, and 5k, and Platinum gets a keynote slot. Can you write the pitch?

**Strong**

> [Upload: MMA_Vietnam_2026_Sponsorship_Deck.pdf]
>
> Based on the attached deck, draft a one-page pitch for the Gold tier aimed at a CMO at a consumer brand. 300 words.

## 5. Iterate, do not restart

Once you have a first draft, edit it in place. Ask Claude to adjust the previous answer. Do not throw the whole thing out and start a new chat. You lose context, you lose what was already working, and you make yourself re-brief.

**Weak**

> *(After a draft you mostly like, you write a brand new prompt from scratch asking for "a version that is shorter and more formal.")*

**Strong**

> Good draft. Three changes: cut the second paragraph entirely, make the CTA more direct (try "Confirm your seat by Friday"), and keep it under 150 words. Keep everything else exactly as is.

The second prompt preserves what you liked and changes only what you did not.

## 6. Break big tasks into steps

Asking for "a full marketing plan" gets you a generic marketing plan. Asking for one section at a time gets you a plan that actually fits.

**Weak**

> Write the full INNOVATE 2026 marketing plan.

**Strong**

> We are going to build the INNOVATE 2026 marketing plan together. First, propose the high-level structure as a table of contents, with a one-line purpose for each section. Do not write any section yet. We will go through them one at a time.

Then, section by section: "OK, draft section 1 now. Target audience is senior marketers in Ho Chi Minh City. Include three KPIs." This produces much better work than one giant prompt, because you steer at every step.

## 7. Tell Claude to push back

Claude tends to be agreeable. If you want stress-testing, ask for it explicitly.

**Weak**

> Here is my pitch. Thoughts?

**Strong**

> Here is my pitch. Act as a skeptical CMO who has seen 100 of these this year. What three things would you push back on, and what would make you stop reading?

This turns Claude from a cheerleader into a critic, which is usually what you need before you send something out.

## 8. Pick the right model for the task

- **Sonnet** for most daily work: drafting, summarising, rewriting, translation. Good balance of speed and quality.
- **Opus** for hard strategy problems, long documents, and anything where one extra round of thinking is worth the wait. Slower but noticeably smarter.
- **Haiku** for quick, throwaway tasks: "format this as a table," "fix the grammar," "extract the three dates from this email."

Defaulting to Sonnet is fine. Reach for Opus when the stakes are high or the problem is genuinely complex. Reach for Haiku when you just want speed.

## 9. Turn on extended thinking for hard calls

"Extended thinking" makes Claude reason visibly before answering. Slower, but the quality jump on strategic questions is real. Use it when:

- You are making a decision with meaningful consequences (pricing, positioning, a strategic trade-off).
- The input is long and you want Claude to connect dots across it.
- You want to see the reasoning, not just the conclusion, so you can sanity-check it.

Do not use it for "rewrite this paragraph." It will just take longer.

## A reusable brief template

When in doubt, prompt in this order:

1. **Role:** who you are, what team you are on.
2. **Context:** what the project or event is, why it matters, what has been tried.
3. **Audience:** who will read or receive the output.
4. **Task:** the specific thing you want Claude to produce.
5. **Constraints:** length, format, tone, language, must-haves, must-not-haves.
6. **Example:** one concrete sample of the target style, if you have one.

Stick to this for a week. You will notice the difference.

---

**Last reviewed:** April 2026
