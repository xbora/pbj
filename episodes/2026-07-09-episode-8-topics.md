# Episode 8 Topics

## Opportunity cost of wasting time with mediocre models
- Jason Lemkin rant in the July 9th 20VC podcast about wasting a whole day using a mediocre model to solve a problem which Fable and Opus together solved in 20 minutes.
### Context: Jason Lemkin's Rant (20VC)
*From the July 9th 20VC episode:*
> "I'm trying to build this project right now... and it's got a sufficiently complex algorithm that I can't understand it. I'm using the mix of the models in Replit which there's it's Sonnet plus open source... Can't quite get it right. So... I'm passing it to Fable and Opus and then I'm running both side by side... after spending about 10 hours in Replit I couldn't solve this big algo problem I solved in about 20 minutes in Fable and Opus... there's going to be this grade of problems where I lost so much time and money using the n-minus-one step down model. I lost a day, endless cycles... I got stuff to do... By using Fable plus Opus... I was able to get to the heart of the problem in an algorithm I could not understand... As the problems we solve get bigger and more complicated, I'm not sure I want to waste a day on a mediocre answer that doesn't work."
## Topic: The Reverse Information Paradox
*Source: [snscratchpad.com/posts/reverse-information-paradox](https://snscratchpad.com/posts/reverse-information-paradox/)*

*Note: The concept of "The Reverse Information Paradox" was written by Satya Nadella, Microsoft CEO.*

**Core Concept:** 
In the AI era, the traditional "Information Paradox" (where a seller risks giving away knowledge to sell it) is reversed. Now, buyers of AI services risk giving away their proprietary knowledge just to use the intelligence they purchased. 

**The Problem:** 
AI models learn from user "exhaust"—prompts, corrections, traces, and evals. This creates an asymmetry where model providers continuously extract institutional know-how from users. Economic value thus shifts to the owners of the learning infrastructure rather than the creators of the knowledge.

**The Solution:** 
Enterprises must establish a strict "trust boundary" to protect their learning mechanisms and retain the rights to use model outputs for fine-tuning their own models.

**5 Imperatives for Enterprises:**
1. **Control:** Own your private evals, organizational memory, traces, and feedback.
2. **Capability:** Build proprietary, in-house learning environments where models learn without exposing company knowledge.
3. **Choice:** Decouple orchestration from single models to avoid lock-in and retain veteran capabilities even if a specific model is removed.
4. **Cost:** Optimize context, models, and tasks efficiently by decoupling the orchestration layer.
5. **Compound:** Combine the above to create a continuous, proprietary learning loop (a "hill climbing machine") that compounds the firm's AI investments.
## Topic: The loudest warning about AI and jobs yet

**Core Takeaways:**
- Over 200 economists, AI leaders, and Nobel laureates (including Daron Acemoglu and Simon Johnson) signed a statement warning that AI could drive economic transformation larger than the Industrial Revolution, risking large-scale job displacement in a condensed timeframe.
- While there is no massive AI jobs crisis yet, warning signs are appearing: early-career, entry-level jobs most exposed to AI are starting to shrink (down 2.7% this year) as employers use AI for junior-level tasks and focus hiring on senior roles.
- The statement, organized by Stanford economist Erik Brynjolfsson, urges proactive measures before the "tsunami" hits. Proposed solutions include AI-funded sovereign wealth funds, overhauled unemployment insurance, and wage insurance.

## Topic: Meta's AI Ads Push Causing Chaos for Brands
*Source: [Business Insider](https://www.businessinsider.com/metas-ai-ads-push-causes-chaos-for-brands-2026-7)*

- **The Issue:** Meta's push for advertisers to use its AI tools is causing bizarre ad errors, such as strangely twisted limbs, gibberish text, and entirely altered products (e.g., REI's ad featuring a bicycle with two handlebars).
- **Advertiser Frustration:** Meta has reportedly auto-enrolled brands in some AI features or had them enabled via bugs. This creates extra work for advertisers who must constantly double-check campaigns and ensure AI enhancements are toggled off to prevent brand damage.
- **Meta's Stance:** Meta claims that AI can make mistakes and places the responsibility squarely on advertisers to review AI outputs.
- **Why Brands Stay:** Despite the headaches, advertisers admit it is difficult to quit Meta due to its massive reach (3.5 billion daily active users) and highly sophisticated targeting data, making it essential for customer acquisition.

## Thinking Machines - Inkling
*Source: [thinkingmachines.ai/news/introducing-inkling](https://thinkingmachines.ai/news/introducing-inkling/)*

- **Model**: 975B parameter (41B active) Mixture-of-Experts transformer with a 1M token context window.
- **Features**: Native multimodal capabilities (text, image, audio) and controllable thinking effort to balance performance with latency/cost.
- **Capabilities**: Strong agentic coding abilities.
- **Fine-tuning**: Heavily optimized to be an excellent base model for fine-tuning via their Tinker platform (they demonstrated this by having the model autonomously fine-tune itself to stop using the letter 'e').


## Questions

**Bora asks Paddy:**
1. You have important news to share about a massive new partnership. Let's hear it.
2. There has been incredible drama in the past week about Bill Gates' daughter's company. And you had a front row seat. Tell us about it.

**Paddy asks Bora:**
1. Should brands be using OpenClaw or Hermes for their agentic operations?
2. Should brands be vibe coding internal web apps or building agents instead?
3. What is the _Reverse Information Paradox" was written by Satya Nadella, Microsoft CEO._ And is this relevant for how brands are building their agentic operations?