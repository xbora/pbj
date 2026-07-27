# Episode 9 Topics

## Topic: The Self-Driving Company (by Amjad Masad)
**Original Article**: [LinkedIn Post](https://www.linkedin.com/pulse/self-driving-company-amjad-masad-uyu5c/)

### Summary
In "The Self-Driving Company", Replit CEO Amjad Masad explains how Replit has successfully woven AI agents into its day-to-day operations over the last six months. Instead of agents just acting as side-tools, they are integrated across the entire organization, performing complex tasks and empowering employees to act more as "directors" rather than just "doers."

### Key Highlights:
- **Engineering Supercharged:** Code output has nearly tripled per engineer while keeping review times flat. Agents are reviewing pull requests (saving 30% of human review time) and investigating bugs (dropping the Mean Time to Mitigation). "Loop engineering" allows swarms of agents to tackle long-stalled migrations.
- **Build vs. Buy Shift:** Replit’s internal agents have surpassed commercial SaaS solutions. The company even canceled a seven-figure SaaS contract because their internally built Replit agent proved more effective for tasks like alert triage and penetration testing.
- **Data Access:** A semantic layer on top of their data warehouse means anyone can self-serve and ask complex business intelligence questions.
- **Sales and Marketing:** Agents enrich leads with internal data context, prep AEs for customer calls with tailored slides, and draft product specs from scratch.
- **Support:** Agents can follow playbooks to investigate tickets, resulting in a 60% faster resolution for escalated issues.

**Takeaway:** Replit is offering a preview of what's to come for the modern enterprise. Using AI for internal company operations isn't just a cost-saver—it completely multiplies the output and strategic leverage of human employees.

## Topic: 12-Factor Companies (by Jeff Huber)
**Original Article**: [LinkedIn Post](https://www.linkedin.com/pulse/12-factor-companies-jeff-huber-udxae/)

### Summary
In the spirit of 12-factor apps and 12-factor agents, Jeff Huber proposes "12-factor companies." As AI evolves, the firm of the future will be designed around the bottleneck of human taste and judgment rather than human execution. The new firm bundles context and authority.

### The 12 Factors:

**Data vs compute**
1. **Own your context:** Avoid tools that hoard context to create a moat. You must have complete and unlimited access to your data.
2. **Rent your intelligence:** Intelligence will become a commodity. Make it easy to swap intelligence and don't let context vampires in.

**Build vs buy**
3. **Build your tools:** Owning your unique tooling stack is another way to defend your unique context. 
4. **Buy your infrastructure:** You shouldn't build everything (like databases or training infra). Buying primitives allows you to move faster.

**Hiring**
5. **Hire agents before people:** For a new task, first try teaching an agent to do it before hiring someone.
6. **Build small and extremely high taste teams:** When the bottleneck moves from execution to taste, you must optimize for small, high-quality teams.

**Learning**
7. **Maximize internal information openness:** Silos are catastrophic for agents. Default to open for your teams.
8. **Design a compounding learning machine:** The winning organizations will learn faster and reduce their cycle time.

**Process design**
9. **Develop rubrics:** Provide agents with ample instructions and a scorecard to check their work, iterating over time.
10. **Reactive + Proactive:** Look for ways to build background agents with organizational context that can proactively propose improvements.

**Task learning**
11. **Store and learn from production traces:** Use real execution of agents to help them improve, moving toward recursive self-improvement.
12. **Encode your expertise:** Employ agents to identify patterns of issues and correct them by interviewing you to fix them.

**(13, bonus!):** Think before you AI! Your thought and taste is, and will continue to be, your advantage.

## Topic: Claude Cowork Adds Screen-Recording to Teach AI Skills
*Note: This relates to something we talked about in the past, and now Claude has made it easier natively.*

### Summary
**Claude Cowork Adds Screen-Recording to Teach AI Skills**
*Last updated 2 hours ago*

The 'Record a skill' tool in Claude Cowork lets Pro, Max, and Team users capture workflows like filing expenses, with Claude analyzing the recording to automate them later. Launched Tuesday, it builds on Claude's abilities to edit files, organize folders, and interact with apps in a shared workspace that runs on Anthropic's servers. Users are testing it for trading alerts, LinkedIn tasks, and email replies, though some noted a phased rollout and privacy questions linger as skills may help improve models.

## The New Rules of Context Engineering for Claude 5
*Source: [Claude Blog](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)*

Anthropic recently shared how context engineering has drastically changed for the newest generation of models (like Claude Opus 5 and Fable 5). They removed over 80% of Claude Code's system prompt with no measurable loss in performance. 

Key takeaways for working with Claude 5:
- **Let Claude Use Judgment Over Strict Rules:** Previous strict guardrails (e.g., "DO NOT add comments") are no longer necessary and can actually confuse the model when they clash with user prompts. Claude 5 can adapt to surrounding context.
- **Design Interfaces Over Examples:** Providing strict examples limits the model's exploration space. Instead, design better tools and parameters (like specific Enum values) to guide behavior.
- **Progressive Disclosure Over Huge Prompts:** Rather than putting all instructions and context in the initial system prompt or a giant `CLAUDE.md` file, use tools, memory, and artifacts to allow Claude to load context and tools precisely when needed.
- **Simple Descriptions Over Repetition:** Claude no longer needs repeated instructions at both the start and end of context windows. Clear, singular instructions in tool descriptions are enough.