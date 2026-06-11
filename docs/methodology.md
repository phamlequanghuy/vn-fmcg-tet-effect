# Methodology — Vietnam FMCG Tet Effect Quantification

This document defines the analytical approach used in this project: the data we work with, the core assumption that makes the analysis meaningful, how we operationalize "the Tet effect," and the limitations the reader must keep in mind when interpreting results.

It is intended to be read alongside `docs/charter.md` (scope, deliverables, timeline) and `docs/data_collection.md` (the exact protocol used to pull the underlying data).

---

## 1. Data source

This study uses **Google Trends search volume for Vietnam** as a proxy for consumer demand in selected FMCG categories.

Charter §7 originally listed Google Trends as a "secondary / proxy" source alongside GSO retail trade data, Nielsen Vietnam, and Kantar Worldpanel reports. In practice, category-level Vietnamese FMCG sales data at weekly granularity is not available in public sources: GSO retail trade series are monthly and aggregated above the FMCG-category level, and Nielsen / Kantar category reports are paywalled. We therefore **elevate Google Trends to the primary data source** for this project and treat its limitations openly (see §5).

### 1.1 Actual collection scope

Collected data covers **5 keywords × 6 years (2020–2025)**, weekly granularity, 30 separate CSV files — one per `(keyword, year)` combination. Keywords: `bia` (beer), `bánh kẹo` (confectionery), `nước ngọt` (soft drinks), `dầu ăn` (cooking oil), `sữa` (milk / dairy).

The actual collection deviates from the protocol described in `docs/data_collection.md` (which recommended a single 5-keyword × multi-year pull per granularity). Two consequences flow from this deviation, both addressed below:

1. **Year coverage shortened from charter §3.** Charter requested 2018–2025 (8 Tet cycles); we have 2020–2025 (6 Tet cycles). Years 2018 and 2019 are not in the dataset and are out of scope for this analysis cycle. The 6-year span still includes the COVID-affected 2020 and 2021 Tets needed for the structural-break check in charter §1.
2. **Per-file 0–100 normalization** (rather than a single shared 0–100 scale across all 5 keywords and 6 years). Each of the 30 CSVs is independently normalized to its own internal max. This is a real constraint that shapes which comparisons are valid; see §4.6 for how it affects the metrics, and §5 limitation L2 for the full treatment.

---

## 2. Core assumption

> **Relative consumer interest in an FMCG category, as measured by Google search volume in Vietnam, is correlated with relative purchase intent for that category over the same period.**

This assumption rests on three sub-claims:

1. **Search behavior precedes or accompanies purchase.** Vietnamese consumers searching for `bia` (beer), `bánh kẹo` (confectionery), `sữa` (milk/dairy), etc. are predominantly evaluating products, comparing brands, checking prices, or looking up recipes — all activities adjacent to a purchase decision.
2. **Search seasonality reflects demand seasonality.** Even if the absolute Google Trends index does not equal absolute sales volume, the *shape* of search interest over time (peaks, troughs, year-over-year change) should reasonably mirror the shape of demand. The Tet effect is a *relative* measurement (uplift over baseline), so a faithful shape is what we need — not a calibrated absolute level.
3. **Vietnam's internet penetration is sufficient for the signal to be representative-ish.** As of 2024, roughly 78% of the Vietnamese population is online and Google is the dominant search engine in Vietnam. The signal therefore reflects a meaningful slice of the urban and suburban consumer base, while under-representing rural and older demographics (see §5).

We are explicitly **not** claiming `Google Trends index = sales volume`. We are claiming `Google Trends shape ≈ demand shape`. Concretely:

> If category X shows a Y% spike in search index above its baseline during the Tet build-up window, then category X demand likely also spikes by a comparable order of magnitude during the same window — though not necessarily by exactly Y%.

Every finding in this project must be framed accordingly: a *search-implied* Tet effect, not a sales Tet effect.

---

## 3. Defining the Tet period

Tet (Tết Nguyên Đán, Lunar New Year) falls on the first day of the lunar calendar, which translates to a different Gregorian date each year. Let `T` denote the Gregorian date of Lunar Jan 1 (Mùng 1 Tết) for each year in scope:

| Year | T (Gregorian date of Mùng 1) |
|------|------------------------------|
| 2018 | 2018-02-16 |
| 2019 | 2019-02-05 |
| 2020 | 2020-01-25 |
| 2021 | 2021-02-12 |
| 2022 | 2022-02-01 |
| 2023 | 2023-01-22 |
| 2024 | 2024-02-10 |
| 2025 | 2025-01-29 |

We define three windows around `T`:

- **Pre-Tet build-up window — `T − 6 weeks` to `T − 1 day`.**
  This is where stocking-up purchases concentrate: gift sets, beer, confectionery, cooking ingredients, dairy.
- **Tet holiday window — `T` to `T + 7 days`.**
  Most retail operates at low intensity; consumer purchasing collapses.
- **Post-Tet recovery window — `T + 8 days` to `T + 4 weeks`.**
  Demand patterns gradually return to baseline.

The **baseline period** for any given year is defined as that year's weeks falling outside `T − 6w` to `T + 4w`, with major non-Tet public holiday weeks (Reunification Day / Labour Day around April 30 – May 1, National Day around September 2) flagged for sensitivity checks.

**Window choice rationale.** The 6-weeks-pre / 4-weeks-post window is consistent with industry heuristics in Vietnamese supply chain practice (charter §1 references the "x2 demand 4 weeks before Tet, x0.3 demand 2 weeks after Tet" planner heuristic). We adopt 6 / 4 as the default and will validate empirically during EDA — if data show the build-up starts earlier (e.g. T − 8w) or recovery takes longer (T + 6w), windows will be widened and the change documented in this file.

---

## 4. Measuring the Tet effect — logic

For each `category × year` cell we compute the following metrics:

### 4.1 Tet build-up uplift (%)

```
uplift_y,c = mean(search_index[c, weeks in T-6w..T-1d of year y])
           / mean(search_index[c, baseline weeks of year y])
           - 1
```

Interpretation: "by how much does category `c`'s search interest exceed its own baseline during the Tet build-up of year `y`."

### 4.2 Tet holiday dip (%)

```
dip_y,c = mean(search_index[c, weeks in T..T+7d of year y])
        / mean(search_index[c, baseline weeks of year y])
        - 1
```

Typically negative; the magnitude captures how completely the category goes quiet during the holiday itself.

### 4.3 Recovery time (weeks)

The smallest integer `k ≥ 1` such that the rolling 2-week mean of `search_index` from `T + k weeks` is at least 90% of that year's baseline mean. Captures how quickly normal patterns resume.

### 4.4 Peak timing (weeks before T)

Within the build-up window, the week (relative to `T`) in which `search_index` is maximised. Answers the planner question: "when *exactly* does the spike land — T − 1, T − 2, T − 3, or T − 4 weeks?"

### 4.5 Aggregation across years

For each category we report:
- The 8-year mean and 8-year range of build-up uplift, holiday dip, recovery time, and peak timing.
- 2020 and 2021 reported separately as "COVID-affected" before being optionally included in the mean — see §5 limitation 6.

### 4.6 Per-file normalization and the scale-invariance of these metrics

The collected data has per-file 0–100 normalization: each CSV is independently rescaled to its own internal max (§1.1). Two natural questions follow.

**Are the metrics defined in §4.1–§4.4 still valid under per-file normalization?** Yes — because they are all ratios computed within the same file:

> Per-file normalization is equivalent to multiplying every value in that file by an unknown constant `k_file > 0`. The metrics `(Tet window mean) / (baseline mean) - 1`, the comparison `rolling_mean ≥ 0.9 × baseline_mean`, and the `argmax` operation that defines peak timing are all scale-invariant under multiplication by a positive constant. The `k_file` cancels.

In plain terms: even though we cannot say "search interest in beer was 30% higher in 2024 than in 2020 in absolute terms," we *can* say "in 2024 beer search jumped 87% above its 2024 baseline, while in 2020 it jumped 75% above its 2020 baseline." That second statement is what the methodology asks for.

**What does break under per-file normalization?**

- Cross-year absolute comparisons of the raw search index (e.g. "the 2024 peak is higher than the 2020 peak in absolute terms"). Out of scope; never claimed.
- Cross-keyword absolute comparisons of the raw search index (e.g. "more people search for beer than for soft drinks"). Out of scope; never claimed.
- Direct cross-keyword comparison of the search-index *level* itself.

**What still works under per-file normalization?**

- Within-(keyword, year) Tet uplift, dip, recovery, peak timing — all four metrics in §4.1–§4.4.
- Cross-year comparison of uplift % for the same keyword (e.g. "beer Tet uplift was 87% in 2024 vs 75% in 2020").
- Cross-keyword ranking by uplift % (e.g. "confectionery has stronger Tet seasonality than soft drinks") — because each side of the ranking uses its own within-file baseline as the denominator, scale-invariance applies independently to each keyword.

In summary, the per-file normalization is a real constraint but does not invalidate the Tet-effect framework. All findings will be framed as **percentage uplift / dip relative to within-year baseline**, never as raw search-index magnitude. This convention is enforced in all charts and write-ups.

### 4.7 Cross-year trend in internet penetration

Vietnamese internet penetration grows over 2020–2025, which would inflate later years' raw search counts. Per-file normalization happens to neutralize this within-year, so each year's Tet uplift % is measured against that year's own behavior — independent of how many users were searching that year. This is a fortunate side-effect of the constraint discussed in §4.6.

### 4.8 Below-threshold handling

For category × year cells where the search index is flat at very low values (Google Trends returns `<1` for some weeks), we mark the cell as "below detection threshold" and exclude it from quantitative comparison rather than report unreliable estimates.

---

## 5. Limitations

We commit to publishing every limitation up front. Readers — and the LinkedIn audience of this project — should weight findings accordingly.

**L1. Search is not purchase.**
Search volume captures interest, not transactions. Many searches are informational (recipes, news, brand reputation checks, gift-receiver curiosity) and do not translate to a purchase. Some purchases happen with zero prior search (in-store impulse, repeat buying). The proxy strength varies by category — high-deliberation categories (premium goods, gift sets) likely have stronger search–sales correlation than impulse-buy categories (snacks, point-of-sale soft drinks).

**L2. Per-file (per-download) 0–100 normalization.**
Google Trends returns values normalized 0–100 against the maximum within the queried region × keyword set × time range. Because the collected data uses one CSV per `(keyword, year)` (§1.1), normalization here is **per file** — the most granular and most restrictive case. Consequences:
- Raw `search_index` values are **not** directly comparable across keywords or across years.
- Comparisons must be done in ratio form (uplift %, dip %, ranking by uplift %), which is scale-invariant under per-file normalization — see §4.6 for the formal argument and the list of comparisons that are and are not valid.
- A single 5-term, 5-year pull would have allowed cross-keyword and cross-year absolute comparisons, at the cost of weekly granularity for ranges > 5 years. The current collection trades that capability for per-year-per-keyword weekly granularity — a defensible trade because every metric we report is a ratio anyway.

**L3. Demographic skew.**
Google search users skew younger, more urban, and more affluent than the Vietnamese population mean. Rural Tet consumption — which is heavy in confectionery, beer, and cooking oil — is under-represented relative to its share of total FMCG demand. Findings should be read as an "urban-skewed Tet effect."

**L4. Keyword selection sensitivity.**
The choice of Vietnamese keyword per category materially affects the signal. `bia` (generic beer) vs `Tiger beer` (branded) vs `thùng bia` (case of beer, more purchase-loaded) all give different curves. We document keyword choice explicitly (in `docs/data_collection.md`) and run sensitivity checks against alternative keywords where the analytical conclusion is close to a threshold.

**L5. Temporal aggregation forced by Trends.**
Google Trends serves weekly data only when the queried range is ≤ 5 years; longer ranges are returned monthly. To cover charter §3's 2018–2025 window we accept monthly aggregation for the long view, and pull a separate weekly-granularity window (2020–2025) for fine-grained timing analysis. Cross-aggregation comparisons (monthly vs weekly) are made carefully and never numerically combined.

**L6. Confounding events.**
The 2020 and 2021 Tet periods overlap with COVID-19 disruption in Vietnam (border closures, mobility restrictions, retail closures). These years are reported separately, never blended into the multi-year mean without an explicit caveat.

**L7. No SKU or brand resolution.**
Search volume can characterize a category, not a brand share within it. We can claim "beer category interest spikes ~X% pre-Tet," but cannot claim which beer brand captures that lift.

---

## 6. Implications for how findings are communicated

Every finding from this project must be communicated as:

- **"Search-implied Tet uplift"** rather than "Tet sales uplift."
- **Directional and shape-based** (timing patterns, ranking of categories by Tet sensitivity) rather than precise sales-magnitude claims.
- **Hypotheses for demand planners to validate against their own internal sales data**, not replacements for those internal numbers.

This framing applies to the white paper, the LinkedIn content series, the Power BI dashboard tooltips, and any chart screenshots used in external communication.

---

**Last updated:** 2026-06-11
**Status:** Methodology v1 — locked for Week 1–3 execution; revisit at end-Week-4 checkpoint per charter §12.
