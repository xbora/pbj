# PBJ News Research System

PBJ research is not trying to produce a serious analyst memo. It is trying to
find fresh stories that two friends can argue about in a pub-style AI and tech
conversation, with enough facts underneath that the jokes and hot takes have
rails.

The scanner has three jobs:

1. Catch fresh AI, tech, ecommerce, creator, payments, and marketing stories.
2. Surface the stories with tension, weirdness, money, jobs, power, or human
   behavior.
3. Keep the candidate list varied enough that one company blog cannot dominate
   the show.

## How The Scanner Works

The source config lives in `config/sources.json`.

It includes:

- `feeds`: RSS/Atom feeds from official sources, newsrooms, analysts,
  newsletters, ecommerce publications, creator publications, and community
  discovery sites.
- `pages`: curated index pages that do not have good feeds, such as Anthropic
  News, Anthropic Engineering, Shopify News, OpenRouter announcements, Stripe
  changelog, and MCP.
- `keywords`: terms that make an item relevant to PBJ.
- `boost_keywords`: terms that make an item more talkable, such as lawsuits,
  layoffs, pricing, data leaks, autonomous agents, revenue, or weirdness.
- `penalty_keywords`: terms that usually create boring segments, such as
  webinars, awards, conference recaps, customer stories, and challenge winners.
- `per_source_limit`: default round-robin diversity cap for the generated
  rundown.

Run the standard scan:

```sh
python3 scripts/news_scan.py --days 14 --limit 75
```

Run a wider backlog scan:

```sh
python3 scripts/news_scan.py --days 30 --limit 100 --per-source-limit 3
```

Disable the source cap only when debugging source quality:

```sh
python3 scripts/news_scan.py --days 14 --limit 100 --per-source-limit 0
```

## Source Lanes

### 1. Official Verification

Use official sources to confirm what actually launched. They are usually not
the best place to find the fun angle.

- OpenAI News and OpenAI developer changelogs
- Anthropic News, Engineering, and Claude release notes
- Google AI, Google DeepMind, Google Developer AI, Google Cloud AI
- Microsoft AI, GitHub Blog, GitHub Changelog
- Meta AI, Hugging Face, AWS Machine Learning, Cloudflare AI
- Shopify News, Shopify Blog, Stripe Blog, Stripe Changelog
- YouTube Blog, Google Shopping, Google Ads, Google Marketing Platform

### 2. Builder And Agent Signal

Use these for what AI engineers, agent builders, and tool nerds will care about.

- Simon Willison
- Latent Space
- AI News
- TLDR AI
- LangChain
- LlamaIndex
- Vercel
- n8n
- Zapier
- Replicate
- OpenRouter announcements
- Model Context Protocol
- Cursor changelog
- Hacker News AI search
- Lobsters AI

### 3. Analysis And Skepticism

Use these to find the argument, the backlash, or the second-order effect.

- One Useful Thing
- Import AI
- Interconnects
- Every Chain of Thought
- Stratechery
- Not Boring
- Understanding AI
- AI Snake Oil
- Gary Marcus
- Lenny's Newsletter

### 4. Tech Journalism And Weirdness

Use these for public-facing stories, drama, consumer impact, and oddball topics.

- TechCrunch AI
- The Verge AI
- VentureBeat AI
- MIT Technology Review
- Axios
- Ars Technica Technology Lab
- ZDNET
- The Information (manual check; often blocks automated feeds)
- Platformer
- Wired AI
- The Decoder
- 404 Media
- Techmeme

### 5. Ecommerce, Ads, And Operator Sources

Use these when the story could touch ecommerce brands, affiliates, paid media,
conversion, retention, or merchant tooling.

- Shopifreaks
- Practical Ecommerce
- Retail Dive
- Modern Retail
- Marketing Dive
- Social Media Today
- Digiday
- Search Engine Journal
- Search Engine Land
- AdExchanger
- MarTech
- PYMNTS
- Payments Dive
- Triple Whale
- Klaviyo

### 6. Creator And Culture Sources

Use these for platform shifts, creator monetization, YouTube behavior, and
stories that can become less technical segments.

- YouTube Blog
- Tubefilter
- Passionfruit
- Product Hunt
- X posts from founders/operators
- LinkedIn posts from ecommerce operators
- Reddit threads when they show real user reaction

## What Counts As PBJ-Worthy

Prioritize a story when it has at least two of these:

- Someone is making or losing real money.
- A job, workflow, or agency service is being replaced or transformed.
- A big company is changing consumer behavior.
- Builders are arguing about whether something works.
- The story has a visual demo, awkward product screenshot, leaked chart, or
  simple prop.
- Paddy has an operator/customer/acquisition angle.
- Bora has an agent/build/AI engineering angle.
- There is a clean disagreement: hype vs reality, useful vs creepy, cheap vs
  expensive, democratizing vs platform lock-in.

Demote a story when it is only:

- a routine product launch
- a customer case study
- a partner announcement
- a benchmark without a human consequence
- a conference recap
- a thought-leadership post with no news
- a feature announcement that cannot be explained in one sentence

## Weekly Process

### Monday Or Tuesday: Wide Net

Run:

```sh
python3 scripts/news_scan.py --days 10 --limit 75
```

Skim for weirdness, money, outrage, funny product behavior, and early stories
that could develop.

### Wednesday: Serious Ranking

Run:

```sh
python3 scripts/news_scan.py --days 14 --limit 75
```

Pick 8-10 candidates. For each one, write:

- one-sentence hook
- why normal people care
- why ecommerce/operators care
- Paddy angle
- Bora angle
- likely disagreement
- visual anchor
- possible Short title

### Thursday: Episode Build

Choose:

- 4 main stories
- 1 backup story
- 1 silly or weird pattern interrupt
- 5 Shorts hooks
- 3 title options
- 2 thumbnail concepts

### Friday: Record

Mark timestamps live when one of these happens:

- hot take
- disagreement
- laugh
- prediction
- simple explanation
- surprising number
- "wait, that is actually weird" moment

## Manual Search Queries

Use web search when the feed scan feels stale:

```text
AI agents ecommerce latest week
agentic commerce Shopify Google OpenAI latest
AI marketing automation ecommerce brand latest
creator affiliate marketing AI YouTube latest
OpenAI Anthropic Google agents latest
MCP agents ecommerce retail latest
AI pricing backlash startup LLM bill latest
AI agent security prompt injection latest
Google AI shopping ads merchant latest
YouTube AI creator monetization latest
site:openai.com/news agents May 2026
site:anthropic.com/news Claude agents May 2026
site:blog.google/products/shopping AI agents May 2026
site:blog.youtube AI creator shopping Brandcast 2026
site:shopify.com agentic commerce AI shopping 2026
site:stripe.com/blog AI payments agents 2026
```

## Verification Rule

Before a story makes the final rundown:

- Verify the launch or claim from the original company/source.
- Add one independent source for controversial or numbers-heavy claims.
- Mark speculation clearly.
- Do not build a segment around a number unless the number is sourced.
- If the story comes from social media, treat it as reaction until verified.

## Final Segment Format

Every final segment should have:

- hook
- setup
- confirmed facts
- host takes
- tension/debate
- Paddy angle
- Bora angle
- questions
- clip moment
- visual anchors
- sources
