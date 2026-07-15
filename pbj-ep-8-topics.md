## Thinking Machines: Introducing Inkling

- **What it is**: Inkling is a 975B parameter (41B active) open-weights Mixture-of-Experts transformer model by Thinking Machines. It features a 1M token context window and was pretrained on 45 trillion tokens of text, images, audio, and video. They also previewed a lighter Inkling-Small (12B active parameters).
- **Key Features**: 
  - **Native Multimodal:** Built with an encoder-free architecture to process text, audio, and vision seamlessly. 
  - **Controllable Thinking Effort:** Allows developers to scale thinking effort to balance cost and latency with reasoning performance.
  - **Agentic Coding & Tool Use:** Excels at complex, multi-step agentic workflows and tool usage.
- **Customization Focus**: It’s engineered specifically as a broad, flexible base for fine-tuning via their Tinker platform. To demonstrate this, Inkling successfully executed an autonomous fine-tuning job on itself to become a "lipogram" model (refusing to use the letter 'e').