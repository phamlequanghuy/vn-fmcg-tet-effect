# Data Collection Protocol — Google Trends Vietnam

This document defines the exact procedure used to pull the raw data that this project analyses. It is the canonical reference for reproducing the dataset.

Read alongside `docs/methodology.md` (analytical approach and assumptions) and `docs/charter.md` (scope and timeline).

---

## 1. Goal

Export Google Trends search-volume time series for selected Vietnamese FMCG categories, in a form that:

1. **Allows valid cross-category comparison** — categories intended for comparison share a single normalization, achieved by pulling them in one query.
2. **Spans the charter window 2018–2025** — covers the 8 Tet cycles required by charter §3.
3. **Has granularity fine enough to do `T − 6w` to `T + 4w` windowing** — weekly resolution for the recent years.

These goals dictate the two-pull strategy in §3.

---

## 2. Category and keyword selection

Per charter §3, we analyze 5–7 FMCG categories. Google Trends allows a maximum of **5 terms per query**, and only terms in the same query share a normalization — so we organize categories into 5-term batches.

### Batch 1 — Core FMCG (the first export)

These five categories are the foundation. All five must be pulled together in **one query** so their Tet-effect magnitudes are directly comparable.

| # | Category | Vietnamese keyword | Rationale |
|---|----------|--------------------|-----------|
| 1 | Beer | `bia` | Highest-volume FMCG search term; iconic Tet gift and gathering staple |
| 2 | Confectionery | `bánh kẹo` | "Cake-candy" — catch-all for confectionery; very strong Tet signal expected |
| 3 | Soft drinks | `nước ngọt` | Generic soft drinks |
| 4 | Cooking oil | `dầu ăn` | Cooking-oil; Tet meal-prep surge expected |
| 5 | Milk / dairy | `sữa` | Broad term covering liquid milk, infant formula, condensed milk |

### Batch 2+ — additional categories (later pulls)

After Batch 1 is collected and validated, additional 5-term batches can be added to cover the remaining charter categories — personal care (`sữa rửa mặt`, `dầu gội`), home care (`nước rửa chén`, `nước giặt`), snacks (`snack`, `bim bim`), gift sets (`giỏ quà Tết`, `hộp quà Tết`).

**Important:** magnitudes from Batch 2 are **not** directly comparable to magnitudes from Batch 1 — only timing patterns can be compared across batches. This is a hard constraint of Google Trends' normalization behavior (`docs/methodology.md` §5 L2).

---

## 3. The two-pull strategy

Google Trends serves different temporal granularities depending on the queried date range:

| Date-range length | Granularity returned |
|-------------------|----------------------|
| ≤ 8 days | hourly |
| 9 days – 90 days | daily |
| 91 days – 5 years | **weekly** |
| > 5 years | **monthly** |

To get both the full charter span (8 years) and the weekly granularity needed for windowing analysis, we run two separate pulls per batch.

### Pull A — Long view (monthly, 8 years)

- **Purpose:** Cover the full 2018–2025 charter window (charter §3); enables multi-year Tet pattern analysis and stress-tests against the COVID-affected 2020 and 2021 Tets
- **Region:** Vietnam
- **Time range:** Custom, **2018-01-01 to 2025-12-31**
- **Search type:** Web Search
- **Category filter:** All categories
- **Granularity returned:** Monthly
- **Output file:** `data/raw/gtrends_VN_monthly_2018-2025_batch1.csv`
- **Expected row count:** ~96 (one per month)

### Pull B — Short view (weekly, 5 years)

- **Purpose:** Fine-grained timing analysis (peak timing within build-up, recovery curve shape) for the 5 most recent Tets (2021–2025)
- **Region:** Vietnam
- **Time range:** Custom, **2020-12-01 to 2025-12-31** (just under 5 years to force weekly granularity)
- **Search type:** Web Search
- **Category filter:** All categories
- **Granularity returned:** Weekly
- **Output file:** `data/raw/gtrends_VN_weekly_2020-2025_batch1.csv`
- **Expected row count:** ~261 (one per week)

Both pulls use the **same 5 Batch 1 keywords** so the metrics line up across pulls.

---

## 4. Step-by-step export procedure

1. Open https://trends.google.com/trends/ in a browser (any browser; no login required).
2. In the search box, enter the first keyword: `bia`.
3. On the results page, click **"+ Compare"** and add the next keyword (`bánh kẹo`). Repeat for `nước ngọt`, `dầu ăn`, `sữa` — five terms total.
4. Set **Region** → `Vietnam`.
5. Set **Time** → `Custom time range`, then enter the dates for the pull you are doing (Pull A: 2018-01-01 to 2025-12-31; Pull B: 2020-12-01 to 2025-12-31).
6. Leave **Category** as `All categories` and **Search type** as `Web Search`. Do not switch to YouTube / Image / News / Shopping — each uses a different index and would not be comparable.
7. Wait for the "Interest over time" chart at the top of the page to render fully.
8. Click the **download icon** (↓) at the top-right of the "Interest over time" panel. The browser will download a file named `multiTimeline.csv`.
9. **Immediately rename** the downloaded file to the convention in §3 and move it to `data/raw/`:
   - Pull A → `gtrends_VN_monthly_2018-2025_batch1.csv`
   - Pull B → `gtrends_VN_weekly_2020-2025_batch1.csv`
10. Repeat steps 2–9 for the other pull (you will redo the 5-term entry, but Google Trends preserves the comparison if you only change the time range — verify dates and re-download).

---

## 5. Output file format

The CSV that Google Trends produces has this shape:

```
Category: All categories

Week,bia: (Vietnam),banh keo: (Vietnam),nuoc ngot: (Vietnam),dau an: (Vietnam),sua: (Vietnam)
2020-11-29,47,28,12,9,84
2020-12-06,49,30,13,10,85
2020-12-13,52,33,15,11,87
...
```

Notes:

- **First two lines** are headers Google Trends prepends. The data loader will skip them.
- **Column names** have diacritics stripped (`bánh kẹo` → `banh keo`). We will re-map to clean labels during cleaning.
- **Time column** is named `Week` for Pull B and `Month` for Pull A.
- **`<1` values** mean "below detection threshold" for that period — we handle this explicitly during cleaning, not silently drop or zero.

---

## 6. Verification checklist

Before the data is considered ready to hand off to the loader:

- [ ] Both files saved to `data/raw/` using the exact naming convention in §3
- [ ] Pull A CSV opens and has ~96 data rows (one per month, 2018–2025)
- [ ] Pull B CSV opens and has ~261 data rows (one per week, late 2020 – end 2025)
- [ ] Every column header in both files ends with `(Vietnam)` — confirms region was set correctly
- [ ] Neither file has been opened-and-saved in Excel (Excel rewrites the date column and may corrupt the format — inspect the raw CSV in a plain text editor or VS Code; do **not** double-click into Excel)
- [ ] Record the **date you ran the export** in a brief note (e.g. add a `# pulled YYYY-MM-DD` comment line at the top of each file, or log it in the project notebook). Google Trends results drift over time as the index is reprocessed, so the export date is metadata we want.

---

## 7. Reproducibility note

The exact Google Trends 0–100 index values are computed against a global maximum within each query and **drift slightly over time** as Google reprocesses its index. Reruns of the same query on a later date may produce slightly different absolute values, though shapes and Tet-effect *magnitudes* should be stable to within ±1–2 index points.

This is acceptable for our purposes because every metric in `docs/methodology.md` §4 is computed *within each year's own baseline*, not against an absolute index. Stability of shape is what matters; stability of absolute index value is not required.

If a future re-pull is needed, repeat §4 exactly and overwrite the raw files, noting the new pull date.

---

**Last updated:** 2026-06-11
**Owner:** Pham Le Quang Huy
