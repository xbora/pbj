## Uber's Agentic Pods (Praveen Neppalli Naga, CTO @ Uber)

**Source:** [LinkedIn Post](https://www.linkedin.com/posts/pneppalli_agentic-ai-adoption-is-on-fire-at-uber-and-share-7480367288781746176-Ji7t/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAAjp7gBDXMHmugat-dSDnIfIxLMaRXNfeg)

Uber is massively scaling Agentic AI beyond software engineering (where 99% of engineers use AI tools and 70%+ of PRs are AI-attributed) to business functions like Finance, Legal, and HR. 

To do this, they created **Agentic Pods**:
* **Team Structure:** Paired ~30 AI-proficient engineers with business domain experts.
* **2-Week Sprints:**
  * Days 1 – 2: Shadow the expert. Observe every step. Document workflows. Ask questions. Build intuition.
  * Day 3: Prioritize opportunities based on scale, repetition, business impact, and data availability.
  * Days 4 – 5: Build a working agent alongside the person doing the job.
  * Days 6 – 9: Validate with several others performing the same work. Does it generalize? Does it actually make their job better?
  * Day 10: Ship.
* **Results:** 16 pods deployed across 16 functions in 2 months. Achieved drastic time savings (e.g., Marketing web QA reduced from 2 weeks to 50 minutes; Financial pacing reports from 2 days to 10 minutes).

**Key Takeaways:**
1. **The Workflow is the Unit of Automation:** The biggest wins come from redesigning the *entire* workflow around AI, which naturally eliminates handoffs, unnecessary approvals, and legacy tools.
2. **Cross-functional Impact:** The most powerful agents cut across multiple tools, teams, and systems.
3. **Co-creation is Crucial:** The best AI opportunities are hidden from the outside. Engineers must sit next to the people doing the work and build *with* them to truly understand the friction points.

## Key Discussion Questions
1. "When you actually try to make the company more productive with AI, what's the real bottleneck?"
2. "Why is content the thing you're putting your energy into now?"

## Overall Theme: The Pitfall of Poorly Structured Data
* **The Core Issue:** How convincing bad data structures can look even when they're quietly leading you to the wrong conclusions.
* **Talking Points:** 
  * Bring direct examples of what can go wrong when relying on poorly structured data.
  * **The Payoff:** Transition naturally into introducing the **data architect agent**.

## AI News Topics
* **Multi-agent swarms for brand operations:** Moving beyond single models to orchestrating multi-agent teams. A "boss" agent routing tasks to cheaper "worker" agents to run complex projects autonomously.
* **From agent prompter to agent manager:** Leaders shifting from manually prompting models to *managing* fleets of autonomous agents in the cloud via state machines and Kanban boards.
* **Anthropic's "global workspace" research:** Their new paper found an emergent internal workspace in Claude that mirrors theories of human conscious access. *Note: Be precise here - it doesn't claim Claude is conscious or has feelings, but it's a fascinating window into what these models are "thinking" but not saying.*
* **Obliterate, don't automate:** Using AI to completely reinvent and replace broken legacy business models, rather than just bolting automation onto existing flawed processes.

## Article Summary: 20 Questions for the Agentic Enterprise
**Source:** [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/20-questions-for-the-agentic-enterprise)

This article outlines Google Cloud's "build-to-govern" framework, designed to help IT leaders evaluate and deploy autonomous AI agents effectively across their organizations. It presents 20 essential questions categorized into four key phases of AI agent adoption using enterprise platforms:

1. **The Build Phase (Establishing the foundation):** Creating the core groundwork, selecting models, and providing the right base tools for agent development.
2. **The Scale Phase (Connectivity and orchestration):** Connecting agents to existing business data/systems and orchestrating multiple agents to work together.
3. **The Optimize Phase (Trust and efficiency):** Evaluating agent performance, ensuring reliability, and building organizational trust in autonomous decisions.
4. **The Govern Phase (Security and oversight):** Managing compliance, enforcing access controls, and maintaining human oversight to mitigate the risks of autonomous actions.

*Relevance to Episode 7:* This directly ties into our news topic on shifting from "agent prompter to agent manager," offering a concrete look at how enterprise IT is tackling the governance, scale, and orchestration of multi-agent operations.