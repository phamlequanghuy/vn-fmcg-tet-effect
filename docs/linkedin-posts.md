# LinkedIn Content Series — Drafts

Working drafts for the 4-post LinkedIn series defined in charter §5 deliverable 4. Drafts are filled in incrementally as the project progresses; placeholders marked `[INSERT: …]` are intentional.

---

## Series strategy

**Goal of the series (from charter §6):**
- Establish the Vietnam FMCG Tet Effect framework as a public reference
- Reach industry professionals at Unilever / P&G / Nestlé Vietnam (stretch: get one to engage)
- Build portfolio narrative for UFLP application and Aston coursework

**Target audience:**
- Primary: Vietnam-based FMCG demand planners, supply-chain managers, S&OP leads
- Secondary: international supply-chain practitioners interested in Lunar New Year markets
- Tertiary: recruiters / mentors who will read the profile

**Language decision:**
Drafts are in English by default. For posts targeted at Vietnam-based practitioners specifically (Posts 2 and 4 in particular), consider Vietnamese or a VI hook + EN body format. Decide per post; do not blanket-translate without intent.

**Format conventions (LinkedIn best practice):**
- Hook on lines 1–2; LinkedIn cuts off the rest behind "…see more"
- Short paragraphs (1–3 lines each), generous whitespace
- Aim for 1,200–1,500 characters total; under 1,300 is the engagement sweet spot
- One visual per post, embedded as native image (not link)
- 3–5 hashtags at the very bottom
- Always end with an open question or CTA to invite comments

**Visualization standard (per project memory):**
Every chart attached to a post must carry: descriptive title, both axes labelled with units, and an inline annotation that surfaces the insight. Screenshots of "raw" exploratory plots are not acceptable.

**Framing standard (per `docs/methodology.md` §6):**
Every claim must be communicated as a **search-implied Tet effect**, never as a sales Tet effect. The proxy caveat must appear in every post body, not buried in a comment reply.

---

## Post 1 — Project Announcement

- **Target week:** Week 4 (per charter §5; charter §9 timeline shows it earlier at Week 3 — pick once Week 3 work is on track)
- **Theme:** Why I'm quantifying Vietnam's Tet effect in public
- **Status:** Skeleton ready; finalise after methodology peer-review

### Hook (first 2 lines)

> Vietnamese demand planners size Tet uplift with a 20-year-old heuristic: "x2 demand four weeks before Tet, x0.3 two weeks after." Nobody publishes the actual number per category.
>
> So I'm building one. In public.

### Body draft

Tet is the single biggest demand event in Vietnamese FMCG. Beer, confectionery, cooking oil, dairy — all of it swings hard for ~10 weeks around Lunar New Year.

Planners I've spoken with rely on instinct plus last year's actuals. Magnitude varies by category, peak timing varies by year (because Tet drifts on the Gregorian calendar), and post-Tet recovery shape is barely talked about.

For the next 8 weeks I'm building a **public framework** that quantifies, for [INSERT: 5–7] FMCG categories:

→ Pre-Tet build-up uplift (% above baseline)
→ Tet holiday dip magnitude
→ When the peak actually lands (T-1w? T-2w? T-3w?)
→ How long demand takes to recover

**One honest caveat upfront:** I'm using Google Trends Vietnam as a demand proxy because public granular sales data does not exist at this resolution. Search is not sales — it's *interest* — so findings should be read as "search-implied Tet effect" and treated as hypotheses for planners to validate against internal data.

Everything is going into a public GitHub repo + a 10-page white paper + a Power BI dashboard. I'll share methodology choices, code, mistakes, and final numbers as I go.

**Question for planners:** what's the single Tet-related question you've never been able to get a clean answer to? Drop it below — I'll prioritize it in the analysis if I can.

### CTA

Follow along for weekly updates as the framework comes together.

### Companion visualization

- **Type:** Conceptual diagram, not a data chart yet
- **Content:** A timeline showing Tet date drift across 2018–2025 with the T−6w to T+4w analysis window shaded
- **Title:** "Why Tet planning is hard: the analysis window drifts 26 days across years"
- **X-axis:** Calendar date (Jan – Mar)
- **Y-axis:** Year (2018 → 2025)
- **Annotation:** Arrow + text — "Mùng 1 Tết (T) shifts by up to 26 days between years; static calendar baselines fail here"

### Hashtags

`#SupplyChain #DemandPlanning #FMCG #Vietnam #LunarNewYear`

### Pre-publish checklist

- [ ] Methodology peer-reviewed (at least 1 person)
- [ ] Repo public and README presentable
- [ ] Companion diagram has title + axis labels + annotation
- [ ] Proxy caveat present in body
- [ ] CTA question phrased to invite specific replies, not generic agreement

---

## Post 2 — Key Finding Teaser

- **Target week:** Week 5–6 (per charter §5 / §9)
- **Theme:** One striking finding from the analysis with a single chart
- **Status:** Awaiting analysis output from Weeks 3–4

### Hook (first 2 lines)

> Conventional wisdom: "stock everything 4 weeks before Tet."
>
> The data says different categories peak at different times — and the spread is [INSERT: X] weeks wide.

> _Alternative hook if magnitude is the headline:_
> Of [INSERT: N] FMCG categories I analysed, the Tet build-up uplift ranged from [INSERT: low]% to [INSERT: high]%. The category planners most under-stock for is [INSERT: category].

### Body draft

For the past few weeks I've been quantifying Tet effect across [INSERT: N] Vietnamese FMCG categories, using Google Trends Vietnam as a search-implied demand proxy (full methodology + repo linked in comments).

Here's the headline pattern from the data so far:

[INSERT 1–3 sentence finding. Examples:
- "Confectionery peaks at T−[X] weeks, but beer peaks at T−[Y] weeks. Planners using a uniform 4-week lead time will systematically [over/under]-stock one of them."
- "The post-Tet recovery is not symmetric. [Category] returns to baseline in [X] weeks; [Category] takes [Y] weeks. The drop is the *easy* half of the Tet effect — the recovery is where the working-capital bleed happens."
- "2020 and 2021 (COVID-affected) look fundamentally different from 2022–2025. Anyone using 5-year averages for Tet 2026 forecasts is folding in a structural break."]

The chart below shows [INSERT: brief description of what the chart shows].

**Caveat (same one as last post):** this is search-implied, not sales-confirmed. The shape is the signal here, not the absolute %. Numbers should be treated as hypotheses to validate against internal sales data.

**Question for planners:** does [INSERT: the specific finding] match what you see in your own data? Public confirmation or pushback is more useful than I can say.

### CTA

Full methodology + dataset + code in the repo (link in comments). White paper drops in [INSERT: ~2 weeks].

### Companion visualization

- **Type:** [Pick at Week 4 — likely either bar chart of uplift % by category, or line chart of T-windowed pattern for top 3 categories]
- **Title (template):** "[Specific finding] — Vietnam FMCG search interest, [years covered]"
- **X-axis:** Category name OR weeks-from-Tet (with units)
- **Y-axis:** % uplift over baseline OR search index value (with units)
- **Annotation:** Arrow / textbox pointing to the surprising point in the chart, stating the insight in one sentence
- **Source line on chart:** "Source: Google Trends Vietnam, [pull date]. Search-implied; see methodology."

### Hashtags

`#SupplyChain #DemandPlanning #FMCG #Vietnam #DataAnalytics`

### Pre-publish checklist

- [ ] Finding has been gut-checked against at least one other view of the same data
- [ ] Chart has title, both axes labelled with units, annotation, source line
- [ ] Search-implied caveat in body (not just comments)
- [ ] Repo link works and points to the analysis file underlying the chart
- [ ] CTA question is specific enough to invite expert pushback

---

## Post 3 — White Paper Release

- **Target week:** Week 8 (per charter §5 §9)
- **Theme:** The framework is published. Here's the headline + how to use it.
- **Status:** Awaiting white paper completion

### Hook (first 2 lines)

> 8 weeks ago I said I'd quantify the Vietnam FMCG Tet effect in public.
>
> The white paper is live. Headline finding: [INSERT: one-sentence summary of the biggest finding].

### Body draft

The framework covers [INSERT: N] FMCG categories across [INSERT: 8] Tet cycles (2018–2025). For each category it quantifies:

→ Build-up uplift: [INSERT: range]% above baseline
→ Holiday dip: [INSERT: range]% below baseline
→ Peak timing: [INSERT: range] weeks before Mùng 1
→ Recovery: [INSERT: range] weeks to return to baseline

The category Tet-sensitivity ranking is in the paper; the top 3 results [INSERT: confirm / contradict] industry intuition.

**What planners can do with this:**
1. Use the per-category lead-time pattern instead of a uniform 4-week heuristic
2. Stress-test current Tet forecasts against the COVID years (2020, 2021) as a worst-case structural break
3. Validate the search-implied magnitudes against internal sales data — and tell me where it breaks

**The honest stuff:**
- Search-implied is not sales. Magnitudes will not match your data exactly.
- 5 categories share normalization; cross-batch comparisons are timing-only.
- Demographic skew toward urban search users under-represents rural Tet consumption.
- Full limitations section in the paper is 7 items long. Read it.

Repo + white paper + Power BI dashboard — all links in comments.

**Ask:** if you work in Vietnamese FMCG demand planning, tell me one number in the paper that's wrong relative to your internal data. I'll update v2 with the correction (attributed if you're willing).

### CTA

Sharing welcome. DMs open for collaboration on v2 (regional breakdown + forecasting layer).

### Companion visualization

- **Type:** Summary infographic — likely a small-multiples panel showing each category's T-windowed pattern, OR a single ranked bar chart of build-up uplift % by category
- **Title:** "Vietnam FMCG Tet Effect framework — [N] categories, [8] Tet cycles, [year range]"
- **X-axis / Y-axis:** Per chart subtype
- **Annotation:** Each category's pattern labelled with peak timing and peak magnitude
- **Source line:** "Source: Google Trends Vietnam, [pull date]. Full methodology + code: github.com/phamlequanghuy/vn-fmcg-tet-effect"

### Hashtags

`#SupplyChain #DemandPlanning #FMCG #Vietnam #OpenData #LunarNewYear`

### Pre-publish checklist

- [ ] White paper PDF final, hosted (GitHub release or similar)
- [ ] Power BI dashboard live and accessible without login
- [ ] Repo README updated with white paper + dashboard links at the top
- [ ] All 7 limitations from methodology §5 referenced or summarised in post body
- [ ] Specific names of 5–10 industry contacts to DM with the link prepared (per charter §9 Week 8)

---

## Post 4 — Lessons Learned Reflection

- **Target week:** Week 10 (per charter §5)
- **Theme:** What I learned about doing public, time-boxed analytical work
- **Status:** Awaiting project retrospective

### Hook (first 2 lines)

> Shipping the Vietnam FMCG Tet Effect framework taught me [INSERT: N] things — most of them about the limitations of the work, not the wins.
>
> The most uncomfortable lesson: [INSERT: the most honest single sentence about what the project did and didn't prove].

### Body draft

Two weeks since the white paper dropped. Here's what I'd change if I started over.

**What worked:**
- [INSERT: 1–2 things — e.g. "Charter as scope contract: I refused 3 scope-creep ideas mid-project and shipped on time."]

**What I'd change:**
- [INSERT: 2–3 honest mistakes — e.g. "Underestimated Google Trends normalization gotchas — cost me ~1 week."]
- [INSERT: e.g. "Should have validated 1 category against a planner's internal data in Week 4, not Week 8. The proxy strength varies massively by category and I had no early signal on which categories had weak search–sales correlation."]

**What stays open:**
- Regional breakdown (HCMC vs Hanoi vs Đà Nẵng) — v2 candidate
- Forecasting layer — v2 candidate
- Promotion-corrected analysis — needs internal data partnership

**The meta-lesson:**
Building public meant I couldn't hide the limitations section. That forced me to ship a less impressive but more honest framework. Net I think that was the right trade.

**Open ask:** if you're a Vietnam FMCG planner and want to collaborate on v2 (regional breakdown), or if you have internal data you'd be willing to use for a private validation check, DM me.

### CTA

Project artifacts all stay public at github.com/phamlequanghuy/vn-fmcg-tet-effect. Forks and issue PRs welcome.

### Companion visualization

- **Type:** Optional. If included, a "before/after" of one analytical choice — e.g. results computed with a 4-week window vs the 6-week window we ended up using, to show how the choice changed conclusions
- **Title:** "Why the Tet window definition matters: [category] uplift under two windowing choices"
- **X-axis:** Weeks before Mùng 1
- **Y-axis:** Search index value (or % over baseline)
- **Annotation:** Callout on the divergence point with one sentence on what the choice changes

### Hashtags

`#SupplyChain #DataAnalytics #BuildingInPublic #Vietnam #FMCG`

### Pre-publish checklist

- [ ] At least 2 weeks have passed since Post 3 (let engagement on the launch settle)
- [ ] Project retrospective doc complete (charter §9 Week 8)
- [ ] Lessons named specifically, not generically (no "I learned a lot")
- [ ] Open ask is concrete and actionable

---

## Cross-cutting notes

### When to write vs when to post

Drafts in this file are working notes — write into them whenever you have material, not on a schedule. Publish dates above are the *targets*, but the actual posting decision happens at the pre-publish checklist for each post.

### Vietnamese-language variants

If a post is meant primarily for Vietnam-based practitioners (Post 2 finding teaser, Post 4 reflection asking for collaborators), draft a Vietnamese version alongside the English one. Keep both in this file under the post heading. Do not auto-translate — Vietnamese supply-chain register has specific terminology (`baseline`, `lead time`, `S&OP`) that often stays in English even in Vietnamese-language professional posts.

### Engagement playbook

For each post:
1. Pre-line up 3–5 industry contacts who'll see and engage in the first hour (LinkedIn algorithm weighs early engagement heavily).
2. Reply to every substantive comment within 24 hours.
3. Save comments that introduce useful pushback to a `docs/feedback-log.md` (future) — they become content for v2 or for the white paper update notes.
4. Do not post comments containing the proxy caveat as an afterthought — it has to be in the body of every post.

### Metrics to track

Per charter §6 target criteria — 50+ reactions per post, 2+ industry professionals commenting or DMing. Track in a small notes doc (not committed; private) so you can see if the series is hitting target before Post 3.

---

**Last updated:** 2026-06-11
**Owner:** Pham Le Quang Huy
