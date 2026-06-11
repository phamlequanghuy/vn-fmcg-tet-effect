# Methodology — Vietnam FMCG Tet Effect Quantification

This document defines the analytical approach used in this project: the data we work with, the core assumption that makes the analysis meaningful, how we operationalize "the Tet effect," and the limitations the reader must keep in mind when interpreting results.

It is intended to be read alongside `docs/charter.md` (scope, deliverables, timeline) and `docs/data_collection.md` (the exact protocol used to pull the underlying data).

---

## 1. Data source

This study uses **Google Trends search volume for Vietnam** as a proxy for consumer demand in selected FMCG categories.

Charter §7 originally listed Google Trends as a "secondary / proxy" source alongside GSO retail trade data, Nielsen Vietnam, and Kantar Worldpanel reports. In practice, category-level Vietnamese FMCG sales data at weekly granularity is not available in public sources: GSO retail trade series are monthly and aggregated above the FMCG-category level, and Nielsen / Kantar category reports are paywalled. We therefore **elevate Google Trends to the primary data source** for this project and treat its limitations openly (see §5).

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

### 4.6 Cross-year normalization

The Google Trends index drifts as Vietnamese internet penetration grows over 2018–2025. We control for this by computing each year's Tet metrics **relative to that year's own baseline**, never against a cross-year absolute index value. This means we measure *the seasonal pattern* within each year and then compare patterns across years — not raw search levels.

### 4.7 Cross-category comparability

Cross-category magnitude comparisons (e.g. "beer spikes more than soft drinks") are only valid for categories that were pulled within a **single Google Trends query**, because Google Trends normalizes the 0–100 index within the query. See `docs/data_collection.md` for the batching strategy.

### 4.8 Below-threshold handling

For category × year cells where the search index is flat at very low values (Google Trends returns `<1` for some weeks), we mark the cell as "below detection threshold" and exclude it from quantitative comparison rather than report unreliable estimates.

---

## 5. Limitations

We commit to publishing every limitation up front. Readers — and the LinkedIn audience of this project — should weight findings accordingly.

**L1. Search is not purchase.**
Search volume captures interest, not transactions. Many searches are informational (recipes, news, brand reputation checks, gift-receiver curiosity) and do not translate to a purchase. Some purchases happen with zero prior search (in-store impulse, repeat buying). The proxy strength varies by category — high-deliberation categories (premium goods, gift sets) likely have stronger search–sales correlation than impulse-buy categories (snacks, point-of-sale soft drinks).

**L2. Within-query normalization, not across-query.**
Google Trends returns values normalized 0–100 against the maximum within the queried region × keyword set × time range. Two consequences:
- Magnitudes from separate downloads are **not** directly comparable.
- Cross-category magnitude comparisons require pulling the categories together in one query (max 5 terms).

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
