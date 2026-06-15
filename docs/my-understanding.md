# My Understanding — Author's Notes

This file is a working notebook where I explain the project's analytical choices **in my own words, in plain language**, as I learn them. It complements the formal documents (`charter.md`, `methodology.md`, `data_collection.md`) — those are the canonical specs; this file is where I make sure I actually understand them.

Write in English (per the project's English-only policy for committed artifacts).

Treat this file as if you were explaining the project to a fellow demand planner over coffee. If you cannot explain a section without falling back on jargon or hand-waving, that's a signal to revisit the formal docs and come back to this file.

---

## 1. Data approach

> _What data are we using? Why this particular data source? What does the data physically look like (granularity, span, format)? If a planner asked "where do these numbers come from?", what would you say?_

**My answer:** I use Google Trends data because Google Trends measures search volume by sampling (randomly) the products people look up through Google search on the internet. It is a *relative* report, which is exactly what I need for a baseline analysis. It does not tell me how much was actually bought, but it does tell me what demand is highest, and in which period — and that pattern is what this project needs to figure out. What the data looks like: a set of weekly search points across a year. These numbers come from customers' searches on Google, recorded over time. Importantly, Google measures the *rate* of searching, not the absolute number of searches.

**Related canonical docs:** `docs/methodology.md` §1, `docs/data_collection.md`.

---

## 2. Normalization logic

> _Google Trends returns values on a 0 – 100 scale per file. Why does that matter? What does "scale-invariant ratio" actually mean for our metrics? Which comparisons does the per-file normalization allow, and which does it block? When someone asks "why can't I just say beer was 30% more popular in 2024 than 2020," what's the answer?_

**My answer:** Each year, Google Trends has its own baseline for that year. Suppose that in 2020, one week before Mùng 1 Tết, confectionery searches across Vietnam were 180,000, while the other 51 weeks hovered around 60,000 per week — that means the pre-Tết week was a 3× uplift. In 2024, again the week before Mùng 1, confectionery searches were 240,000 (the highest of the year) while the other 51 weeks were 40,000 — so that pre-Tết week is a 6× uplift RELATIVE TO THE SAME YEAR. What I cannot do is say the 2024 pre-Tết week was 4× a normal week using 2020's baseline, because each year is normalized on its own scale.

**Related canonical docs:** `docs/methodology.md` §4.6, §5 (limitation L2).

---

## 3. Tet windowing

> _How do we define the "Tet window" each year? Why 6 weeks pre-Tet and 4 weeks post-Tet? What is `T` exactly, and why does it shift on the Gregorian calendar? How would the analysis change if we used a 4-week pre-window instead — would the framework still answer the same question?_

**My answer:** Because Tết in Vietnam follows its own (lunar) Eastern calendar, it shifts relative to the shared global (Gregorian) calendar. Each year Tết falls in a different month — or 1–3 weeks off the global calendar — usually in January or February. But overall the pattern still holds: 1 to 2 weeks before Tết, demand peaks for confectionery and soft drinks.
T = the day of Mùng 1 Tết. Every week is measured relative to T (T−1 = one week before Mùng 1, T+2 = two weeks after).
The Tết window starts from the point at which buyers are considered to begin shopping for Tết. The earlier heuristics held that it runs from 6 weeks before Mùng 1 until 4 weeks after Mùng 1.
From my analysis, switching the window to 4 weeks before Tết would still work, because the analysis showed demand starts around T−4.

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

**My answer:**
- Build-up uplift % answers how much demand rises compared with normal weeks, so you can prepare to stock up. Whether a value is high or low depends on that year's baseline.
- Holiday dip % is how the product's search rate behaves during Tết, measured from Mùng 1 to T+7. It tells me whether the product falls off after the stocking-up (confectionery drops back to normal, beer does not).
- Recovery time is the number of weeks it takes for search to return to the baseline level. For example, before Tết searches are 20,000 and people buy; during Tết they are consuming, no one searches anymore, so it drops over that period. Once the stock is used up, people start searching and buying again, and it rises back.
- Peak timing is the week with the highest search count before Mùng 1 Tết.
- The pattern I'd expect to see is a strong rise in the 2 weeks before Tết. For a Tết-neutral category (cooking oil, dairy), the pattern is the OPPOSITE — no spike, and pre-Tết even sits below baseline.

**Related canonical docs:** `docs/methodology.md` §4.1 – §4.4.

---

## Open questions for myself

> _Things I think I understand but want to verify. Things I do not yet understand and want to revisit. Things that are genuinely fuzzy and need an outside check._

[ write your notes here ]

---

**Last updated:** 2026-06-15
