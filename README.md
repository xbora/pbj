# Paddy and Bora Jam (PBJ) Prep

PBJ is a weekly, conversational AI and tech news show with a pub-table energy:
smart enough for builders, loose enough to be fun, and especially sharp around
agents, ecommerce, creator/affiliate marketing, and operator workflows.

## Weekly Workflow

1. Run the news radar:

   ```sh
   python3 scripts/news_scan.py --days 10 --limit 50
   ```

2. Read the generated file in `research/`.
3. Promote 4 main segments and 1-2 backups into the next file in `episodes/`.
4. Use the segment shape from `templates/episode.md`:
   - emotional hook
   - why now
   - setup
   - talking points
   - tension/debate angle
   - Paddy angle
   - Bora angle
   - questions to bounce
   - clip moments and visual anchors

## Source Strategy

The scanner is intentionally boring and reliable: it pulls RSS/Atom feeds from
official company blogs and high-signal tech publications, then scores items
against PBJ keywords. It is a radar, not a replacement for judgement.

For final show prep, verify each story from the original source and add one
outside source if the story is controversial, numbers-heavy, or likely to be
PR-shaped.

See `docs/research-system.md` for the repeatable weekly research process and
`docs/show-playbook.md` for the YouTube/show-format rules.

## References

Original source docs are kept in `references/`:

- `paddy-episode-1-prep.mhtml`: Paddy's original Episode 1 prep sheet.
- `ai_pub_chat_youtube_playbook.md`: Bora's YouTube show strategy notes.

## Cadence

Suggested rhythm for a Friday recording:

- Monday: loose scan, collect weird/funny candidates.
- Wednesday: serious scan, pick the probable four.
- Thursday: tighten angles and questions.
- Friday: record.

## Selection Criteria

Rank stories by show value, not just importance:

- emotional reaction
- disagreement potential
- audience impact
- visual potential
- clip potential
- relevance to agents, ecommerce, creators, operators, or AI tooling

The weekly goal is not to summarize AI news. The weekly goal is to make
complicated tech feel emotionally understandable and socially entertaining.
