# PBJ News Research System

The system has two jobs:

1. Find fresh AI and tech stories.
2. Rank them for PBJ, which means ranking for conversation, tension, and clips,
   not just importance.

## Source Tiers

### Tier 1: Official Sources

Use these to verify what actually launched:

- OpenAI News
- Anthropic News and Engineering
- Google AI, Google Shopping, Google Ads, YouTube Blog
- Shopify News, Shopify Blog, Shopify Engineering
- Stripe, Visa, Mastercard for agentic payments
- Triple Whale, Klaviyo, Meta, TikTok, Amazon, Microsoft

### Tier 2: High-Signal Analysis

Use these to find the angle:

- Simon Willison
- Latent Space
- Ben Thompson / Stratechery
- Lenny's Newsletter when ecommerce/product relevant
- A16Z, First Round, Every, and similar operator analysis

### Tier 3: News and Discovery

Use these to catch what the official feeds miss:

- TechCrunch AI
- The Verge AI
- VentureBeat AI
- MIT Technology Review
- Axios AI
- Techmeme
- Hacker News
- Shopifreaks for ecommerce

### Tier 4: Social Proof and Weirdness

Use these carefully. They are good for what people are reacting to, not for
unverified facts:

- X posts from founders/operators
- Reddit threads
- YouTube comments
- LinkedIn posts from ecommerce operators
- Product Hunt and launch communities

## Weekly Process

### Monday: Wide Net

Run:

```sh
python3 scripts/news_scan.py --days 7 --limit 50
```

Look for weirdness, emotional reactions, and early stories that could develop.

### Wednesday: Serious Ranking

Run:

```sh
python3 scripts/news_scan.py --days 10 --limit 75
```

Pick 6-8 candidates. For each candidate, write:

- emotional hook
- why normal people care
- why operators care
- strongest disagreement
- best visual anchor
- likely Short

### Thursday: Episode Build

Choose:

- 4 main stories
- 1 backup story
- 1 pattern interrupt
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

## Story Scoring

Score each story 1-5 on:

- Freshness
- Audience impact
- Paddy relevance
- Bora relevance
- Disagreement potential
- Visual potential
- Clip potential
- "What changes?" clarity

PBJ priority is high when a story hits at least three of:

- money
- jobs
- human behavior
- power
- culture

## Search Queries To Reuse

Use web search for gaps the feed scanner misses:

```text
AI agents ecommerce latest week
agentic commerce Shopify Google OpenAI latest
AI marketing automation ecommerce brand latest
creator affiliate marketing AI YouTube latest
OpenAI Anthropic Google agents latest
MCP agents ecommerce retail latest
site:openai.com/index agents May 2026
site:anthropic.com/news Claude agents May 2026
site:blog.google/products shopping AI agents May 2026
site:blog.youtube AI creator shopping Brandcast 2026
site:shopify.com agentic commerce AI shopping 2026
```

## Verification Rule

Before a story makes the final rundown:

- verify from the original company/source
- add one independent source for controversial or numbers-heavy claims
- mark speculation clearly
- avoid building a segment around a number unless the number is sourced

## Output Rule

Every final segment should have:

- hook
- setup
- talking points
- tension
- Paddy angle
- Bora angle
- questions
- clip moment
- visual anchors
- sources

