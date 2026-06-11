# My Understanding — Author's Notes

This file is a working notebook where I explain the project's analytical choices **in my own words, in plain language**, as I learn them. It complements the formal documents (`charter.md`, `methodology.md`, `data_collection.md`) — those are the canonical specs; this file is where I make sure I actually understand them.

Write in English (per the project's English-only policy for committed artifacts).

Treat this file as if you were explaining the project to a fellow demand planner over coffee. If you cannot explain a section without falling back on jargon or hand-waving, that's a signal to revisit the formal docs and come back to this file.

---

## 1. Data approach

> _What data are we using? Why this particular data source? What does the data physically look like (granularity, span, format)? If a planner asked "where do these numbers come from?", what would you say?_

[ write your notes here ]

**Related canonical docs:** `docs/methodology.md` §1, `docs/data_collection.md`.

---

## 2. Normalization logic

> _Google Trends returns values on a 0 – 100 scale per file. Why does that matter? What does "scale-invariant ratio" actually mean for our metrics? Which comparisons does the per-file normalization allow, and which does it block? When someone asks "why can't I just say beer was 30% more popular in 2024 than 2020," what's the answer?_

[ write your notes here ]

**Related canonical docs:** `docs/methodology.md` §4.6, §5 (limitation L2).

---

## 3. Tet windowing

> _How do we define the "Tet window" each year? Why 6 weeks pre-Tet and 4 weeks post-Tet? What is `T` exactly, and why does it shift on the Gregorian calendar? How would the analysis change if we used a 4-week pre-window instead — would the framework still answer the same question?_

[ write your notes here ]

**Related canonical docs:** `docs/methodology.md` §3.

---

## 4. Metrics calculation

> _Walk through each of the four core metrics in plain language:_
> - _Build-up uplift % — what does it answer? how is it computed? what value is "high" vs "low"?_
> - _Holiday dip % — same questions._
> - _Recovery time (weeks) — same._
> - _Peak timing (weeks before T) — same._
>
> _For a Tet-sensitive category (e.g. confectionery), what pattern across the four metrics would you expect to see? What about a Tet-neutral category?_

[ write your notes here ]

**Related canonical docs:** `docs/methodology.md` §4.1 – §4.4.

---

## Open questions for myself

> _Things I think I understand but want to verify. Things I do not yet understand and want to revisit. Things that are genuinely fuzzy and need an outside check._

[ write your notes here ]

---

**Last updated:** [update this each time you edit the file]
