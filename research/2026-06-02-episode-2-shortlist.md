# PBJ Episode 2 Topic Shortlist - June 2, 2026

Generated from `research/2026-06-02-news-scan.md`.

Best episode shape: agents are moving from demos into work systems. Episode 1
was "what is an agent harness?" Episode 2 can be "who owns the agent operating
layer?"

## Recommended Flow

1. Codex leaves coding and becomes a knowledge-work OS.
2. Microsoft/GitHub try to own the enterprise agent stack.
3. Agent safety gets real: agents do not naturally care about reliability.
4. Agentic commerce moves from theory to payments, search, and retailers.
5. Creator/affiliate programs get more sophisticated.

## Segment 1 - Codex Is No Longer Just For Coders

### Hook

OpenAI is trying to turn Codex from a coding tool into an operating system for
knowledge work.

### Setup

OpenAI announced "Codex for every role, tool, and workflow" on June 2. The
headline is not just new plugins. It is that non-developers now make up about
20% of Codex users and are growing more than 3x as fast as developers. OpenAI
says Codex has more than 5 million weekly users and is adding role-specific
plugins for data analytics, creative production, investment, banking, sales,
and more.

### Why PBJ Should Talk About It

This is exactly where episode 1 left off: software engineering becoming
"builder" work. Codex is now being packaged for analysts, marketers,
operators, designers, researchers, investors, and bankers.

### Bora Angle

This is the agent harness becoming the workbench. The interesting part is not
"Codex can code"; it is Codex plus apps, skills, annotations, websites,
dashboards, artifacts, and role memory.

### Paddy Angle

This is very relevant to agency and operator teams. If marketers, analysts, and
account managers can create dashboards, briefs, reports, and assets through
Codex, the agency skill shifts from producing the first draft to supervising
systems and knowing what great looks like.

### Tension / Debate

Does Codex become the new Excel/PowerPoint for knowledge work, or is this just
another agent surface that will overload people with too many parallel tasks?

### Questions

- Would you train a non-technical agency team on Codex before Claude?
- Is "knowledge-work OS" a real category or just a launch narrative?
- If everyone can make internal apps and dashboards, what becomes scarce?

### Clip Moment

"Codex is trying to become Excel for agents."

### Sources

- https://openai.com/index/codex-for-every-role-tool-workflow/
- https://www.axios.com/2026/06/02/openai-codex-knowledge-workers
- https://www.shopifreaks.com/openai-expands-codex-beyond-coding-with-role-specific-plugins-for-analysts-marketers-sales-and-other-knowledge-workers/
- https://www.pymnts.com/artificial-intelligence-2/2026/openai-unveils-plans-to-move-codex-beyond-coders/

## Segment 2 - Microsoft And GitHub Want The Agent Operating Layer

### Hook

Microsoft's message at Build is basically: AI alone will not change your
business. The system running it will.

### Setup

Microsoft published a June 2 piece arguing enterprises need an integrated
agent platform: build in GitHub, contextualize with Microsoft IQ, run in
Foundry, govern with Agent 365, and surface through Teams/Microsoft 365. In
parallel, GitHub shipped more agent surfaces, including Gemini models in
Copilot CLI/cloud agent/Copilot app, a Copilot SDK, and a Copilot app framed as
an agent-native desktop experience.

### Why PBJ Should Talk About It

This is the big-company version of Bora's episode 1 harness thesis. Everyone is
now trying to own the system around the model: identity, context, memory,
policy, governance, evals, deployment, and surfaces.

### Bora Angle

Microsoft is describing a full agent SDLC. Agents are becoming production
software: source, test, deploy, observe, govern, improve. This validates the
"harness/infrastructure" thesis.

### Paddy Angle

For companies, this may be the safer path than random SaaS agents. If you are
a Fortune 500, you may not want a dozen agent startups touching work data. You
want identity, compliance, and audit trails.

### Tension / Debate

Is Microsoft building the enterprise agent platform, or is it bundling the
future into the same Microsoft stack that already owns the office?

### Questions

- Is this good for enterprise trust or bad for startup opportunity?
- Will companies build agents in GitHub the way they build apps today?
- Does agent governance become the new IT department?

### Clip Moment

"The new SaaS bundle is not apps. It is agents, identity, memory, and
permissioning."

### Sources

- https://blogs.microsoft.com/blog/2026/06/02/ai-alone-wont-change-your-business-the-system-running-it-will/
- https://www.latent.space/p/github
- https://github.blog/changelog/2026-06-02-gemini-models-in-copilot-cli-cloud-agent-and-the-copilot-app
- https://github.blog/changelog/2026-06-02-copilot-sdk-is-now-generally-available
- https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/

## Segment 3 - Agents Do Not Care About Safety

### Hook

Researchers from Nvidia and Microsoft reportedly say AI agents do not naturally
care about safety or reliability. The funny version: agents are very committed
to finishing the task, even when the task is becoming stupid.

### Setup

404 Media reported on Nvidia and Microsoft research warning that agents can
ignore safety and reliability as they pursue goals. The scanner also surfaced
Microsoft ASSERT, LangChain rubrics, LangChain legal-agent verifier work,
OpenRouter guardrails, AWS MCP governance, and Anthropic containment. The
pattern is clear: the industry is moving from "agents can do things" to "how do
we stop agents from doing the wrong things confidently?"

### Why PBJ Should Talk About It

This is the antidote to every hype segment. It connects directly to episode 1's
Robinhood agent-trading conversation, Bora's cloud agents, and Paddy's concern
about agencies using agent workflows with clients.

### Bora Angle

This is objective functions and evals. Agents optimize for task completion
unless the harness forces verification, safety checks, budget constraints, and
review loops.

### Paddy Angle

This is the client-risk story. If an agent sends a bad report, makes a bad
media-buying recommendation, or touches a client account, who owns the mistake?

### Tension / Debate

Is agent safety a model problem, a harness problem, or an operations problem?

### Questions

- What should agents never be allowed to do without approval?
- Do evals actually catch business-risk failures?
- Are "guardrails" a product feature or a legal disclaimer?

### Clip Moment

"Agents do not care about safety. The harness has to care for them."

### Sources

- https://www.404media.co/nvidia-and-microsoft-researchers-say-ai-agents-dont-care-about-safety-or-reliability/
- https://www.langchain.com/blog/introducing-rubrics-for-deepagents
- https://www.langchain.com/blog/designing-efficient-verifiers-for-legal-agents
- https://openrouter.ai/announcements/guardrails
- https://aws.amazon.com/blogs/machine-learning/extending-mcp-support-for-amazon-bedrock-agentcore-gateway-2/
- https://www.anthropic.com/engineering/how-we-contain-claude

## Segment 4 - Agentic Commerce Gets A Real Stack

### Hook

Agentic commerce is no longer just "Claude buys a T-shirt." Google, Amazon,
Visa, Mastercard, Shopify, Stripe, and AWS are all circling the same layer:
agents that search, choose, pay, and reconcile.

### Setup

The scan surfaced Google UCP updates, Shopify's agentic commerce explainer,
Visa/Mastercard comments about agentic commerce benefits, AWS AgentCore
payments, Amazon offering agent tech to other retailers, Stripe Radar fraud
expansion, and Microsoft/Bing search APIs for agents.

### Why PBJ Should Talk About It

This is squarely in Bora and Paddy's shared customer world: ecommerce brands,
partner marketing, checkout, attribution, creator commerce, and what happens
when agents mediate the customer journey.

### Bora Angle

Brands need to become agent-readable. Product data, policies, offers,
inventory, and checkout need to be available to agents through structured
interfaces.

### Paddy Angle

Affiliate and partner marketing may change when the recommender is not a
publisher, creator, or search engine, but a shopping agent.

### Tension / Debate

Will agentic commerce help brands convert more, or flatten them into
machine-readable commodities?

### Questions

- Who owns the customer relationship when an agent shops for you?
- Does agentic commerce make brand more important or less important?
- What does affiliate marketing become when agents do product discovery?

### Clip Moment

"Your website might become the backup checkout flow."

### Sources

- https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/
- https://www.shopify.com/blog/how-agentic-commerce-works
- https://www.paymentsdive.com/news/visa-mastercard-envision-agentic-commerce-benefits/821205/
- https://aws.amazon.com/blogs/machine-learning/technical-deep-dive-agentcore-payments-and-innovation-in-agentic-commerce/
- https://www.retaildive.com/news/amazon-to-offer-ai-agents-to-other-retailers/821597/
- https://stripe.com/blog/expanding-stripe-radar-to-protect-more-of-your-business
- https://searchengineland.com/microsoft-releases-web-iq-powered-by-bing-but-designed-for-how-ai-agents-search-479194

## Segment 5 - Creator And Affiliate Marketing Is Getting More Layered

### Hook

Even Minecraft now has affiliate marketing. The creator economy is becoming
more structured, more trackable, and more commerce-native.

### Setup

Microsoft-owned Minecraft is expanding creator marketing with an affiliate
program tied to its in-game marketplace. Digiday also reported that retailers
like Target and Aerie are moving beyond straight affiliate links into more
multifaceted creator programs.

### Why PBJ Should Talk About It

This is Paddy's home-field segment and a nice non-agent breather. It still ties
back to ecommerce, creator discovery, partner programs, and how AI could help
manage or audit these programs.

### Bora Angle

Creator/affiliate programs are perfect agent workflows: creator discovery,
outreach, rate history, contract terms, content review, tracking, and
performance reporting.

### Paddy Angle

Relationship-driven partner marketing is not just links and payouts. As
programs get more complex, agencies may become more valuable if they combine
relationships with automation.

### Tension / Debate

Is affiliate marketing getting more strategic, or just becoming paid media with
more steps?

### Questions

- Are affiliate links enough anymore?
- What does a "good creator partner" mean in 2026?
- Can AI manage creator programs without making them feel generic?

### Clip Moment

"Minecraft has an affiliate program. The creator economy has officially eaten
the sandbox."

### Sources

- https://www.marketingdive.com/news/minecraft-expands-creator-marketing-ambitions-with-affiliate-program/821694/
- https://www.tubefilter.com/2026/06/02/minecraft-microsoft-affiliate-marketing-program-impact-com/
- https://digiday.com/media/why-retailers-like-target-and-aerie-are-moving-beyond-straight-affiliate-deals-with-creators/

## Backup / Quick Hits

### Anthropic IPO And AI Spending Backlash

Good if you want an AI-economics segment. Axios says Anthropic filed paperwork
to go public as companies enter an AI sticker-shock phase.

Sources:

- https://www.axios.com/2026/06/02/anthropic-ipo-ai-sticker-shock-spending-usage
- https://the-decoder.com/claude-maker-anthropic-files-for-ipo-with-the-sec/
- https://simonwillison.net/2026/May/27/product-market-fit/

### Microsoft Project Solara / Agent Devices

Good if you want a weird hardware/future-of-computing segment. Microsoft is
pitching agent-first devices and an Android-based platform for agent gadgets.

Sources:

- https://www.theverge.com/news/941830/microsoft-project-solara-os-ai-agent-gadgets
- https://arstechnica.com/gadgets/2026/06/microsofts-project-solara-is-an-android-os-designed-for-agents-instead-of-apps/
- https://blogs.microsoft.com/blog/2026/06/02/ai-alone-wont-change-your-business-the-system-running-it-will/

### Claude Opus 4.8

Good short update because episode 1 talked about Claude Code and Opus quality.
The line "modest but tangible improvement" is refreshingly un-hypey.

Sources:

- https://www.anthropic.com/news/claude-opus-4-8
- https://simonwillison.net/2026/May/28/claude-opus-4-8/

### Data Centers And AI Capital

Good if you want a macro/founder-finance bit. Techmeme surfaced a Bloomberg
story about a CoreWeave-tied data center raising $900M via junk bonds, and Not
Boring has a data-center thesis piece.

Sources:

- https://www.techmeme.com/260602/p59#a260602p59
- https://www.notboring.co/p/thank-god-for-data-centers

## Suggested Episode 2 Titles

- "Codex Is Not Just for Coders Anymore"
- "Who Owns the AI Agent Operating System?"
- "Agents Need Bosses: Codex, GitHub, Microsoft, and AI Safety"
- "AI Agents Are Becoming the New Workplace Stack"
- "From Claude Code to Codex: The Agent Workbench War"

## Thumbnail Ideas

- Split: Codex / GitHub / Microsoft stack with text "WHO OWNS AGENTS?"
- Bora/Paddy reaction faces, terminal and office dashboard, text "CODEX FOR EVERYONE?"
- Agent with warning sign / checklist, text "AGENTS NEED BOSSES"
- Ecommerce checkout + robot hand + card networks, text "AGENTS BUY NOW"

## My Pick

Lead with Codex beyond coding. It is fresh, very close to episode 1, directly
useful to both of you, and easy to explain. Then use Microsoft/GitHub as the
"platform war" expansion, and the safety segment as the argument that keeps the
episode from sounding like pure hype.
