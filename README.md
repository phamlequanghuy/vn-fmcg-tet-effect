# Vietnam FMCG Tet Effect

> A public framework for quantifying Lunar New Year (Tết) demand patterns in Vietnamese FMCG categories — built for demand planners, accessible to industry researchers.

[![Status](https://img.shields.io/badge/status-white_paper_v1_published-brightgreen)](output/whitepaper/whitepaper.pdf)
[![Methodology](https://img.shields.io/badge/methodology-v1_locked-brightgreen)](docs/methodology.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

📄 **[Read the white paper (PDF)](output/whitepaper/whitepaper.pdf)** &nbsp;·&nbsp; 🧮 [Methodology](docs/methodology.md) &nbsp;·&nbsp; 📝 [Author's plain-language notes](docs/my-understanding.md)

---

## Overview

Tết (Lunar New Year) is the single largest annual demand event in Vietnamese FMCG. Yet planners commonly rely on a heuristic — *"x2 demand four weeks before Tết, x0.3 demand two weeks after"* — without any public, per-category, quantitative baseline.

This project quantifies the **Tết Effect** — magnitude, timing, recovery shape — across five Vietnamese FMCG categories over six consecutive Tết cycles (2020–2025), using Google Trends Vietnam as a search-implied demand proxy.

The framework is intentionally **public and reproducible**: all raw data, code, methodology, and limitations are committed to this repository so any demand planner or researcher can clone, rerun, and extend it. Every figure is **search-implied** — a directional benchmark to validate against internal sales, not a replacement for it.

## Key findings

The twenty-year planner heuristic is right in spirit but wrong in three specific, plannable ways. Full evidence, tables, and figures in the **[white paper](output/whitepaper/whitepaper.pdf)**.

1. **The Tết effect is not blanket — it concentrates in three of five categories.** Confectionery (`bánh kẹo`, **+130%** peak uplift), beer (`bia`, **+129%**), and soft drinks (`nước ngọt`, **+82%**) show a strong, repeatable Tết spike. Cooking oil (`dầu ăn`, −9%) and dairy (`sữa`, −19%) show **no spike** — their real peak season lies elsewhere (dairy peaks in June).

2. **The spike peaks one to two weeks before Tết, not four.** The weekly peak lands at **T − 1.4 weeks** (confectionery), **T − 1.0 week** (soft drinks), and **T − 0.7 weeks** (beer). The familiar four-week mark is when elevated demand *begins*; the true crest is in the final fortnight.

3. **Categories behave differently *during* the holiday week — beer is the outlier.** Confectionery dips once the holiday arrives (**−2%**, a pre-stock category), while beer stays **+51% above baseline through the holiday week itself** (a consumption category). They need different replenishment logic.

4. **Confectionery has a second annual season.** A robust September search spike points to Tết Trung Thu (Mid-Autumn / mooncake) — confectionery is a two-season category, not a Tết-only one.

**Central implication for planners:** replace the single uniform Tết rule with a *per-category, shape-aware* plan — category-specific lead times, a later replenishment crest, segmentation by pre-stock vs in-holiday consumption, and year-by-year stress-testing rather than blended averages.

## Research questions

(Detailed in [`docs/charter.md`](docs/charter.md) §2.)

1. By what percentage does demand spike above the non-Tết baseline, per category?
2. When does demand start spiking (T − X weeks before Tết) and how long does the spike last?
3. How deep is the post-Tết drop, and when does it recover?
4. Which categories are most / least Tết-sensitive?
5. Does the pattern shift across years — is COVID (2020 – 2021) an outlier?

## Categories analysed

| # | Category | Vietnamese keyword | English label |
|---|----------|--------------------|---------------|
| 1 | Beer | `bia` | Beer |
| 2 | Confectionery | `bánh kẹo` | Confectionery |
| 3 | Soft drinks | `nước ngọt` | Soft drinks |
| 4 | Cooking oil | `dầu ăn` | Cooking oil |
| 5 | Milk / Dairy | `sữa` | Milk / Dairy |

Time coverage: weekly granularity, 2020 – 2025 inclusive (6 Tết cycles).

## Methodology summary

Full treatment with every assumption and limitation in [`docs/methodology.md`](docs/methodology.md). Headlines:

- **Data source.** Google Trends Vietnam search volume, used as a *proxy for consumer interest*. All findings are framed as **search-implied Tết effect**, not as sales.
- **Tết windowing.** Pre-Tết build-up = `T − 6 weeks` to `T − 1 day`; Tết holiday = `T` to `T + 7 days`; recovery window = `T + 8 days` to `T + 4 weeks`. `T` is the Gregorian date of Mùng 1 Tết (Lunar Jan 1) for each year.
- **Core metrics.** Build-up uplift %, holiday dip %, recovery time in weeks, peak timing relative to T. All four are within-year ratios over that year's own baseline.
- **Normalization handling.** Google Trends returns 0 – 100 normalized per file. Every metric is a within-file ratio, which is scale-invariant under the per-file normalization — so the constraint does not invalidate the framework. Absolute cross-file comparisons (e.g. "beer 2024 was X% bigger than beer 2020 in absolute search volume") are explicitly off the table.

The methodology document lists the limitations in full: search ≠ purchase, per-file normalization, demographic skew toward urban search users, keyword choice sensitivity, temporal aggregation forced by Trends, COVID confounding entangled with lunar-calendar drift in 2020 – 2021, and no SKU / brand resolution.

## Repository structure

```
vn-fmcg-tet-effect/
├── data/
│   ├── raw/                          30 Google Trends CSVs (5 keywords × 6 years)
│   └── processed/                    trends_long.csv (combined long-format dataset)
├── src/
│   └── load_data.py                  load + validate + emit processed dataset
├── notebooks/
│   ├── 01_eda.ipynb                  exploratory analysis + Tết-effect visualization
│   ├── 02_stl_decomposition.ipynb    STL decomposition (Mid-Autumn discovery)
│   ├── 03_publication_figures.ipynb  white-paper figure generation
│   └── figures/                      notebook-generated charts
├── output/
│   └── whitepaper/
│       ├── whitepaper.pdf            ← the deliverable (figures embedded)
│       ├── whitepaper.md             white paper source (Markdown)
│       └── figures/                  figures embedded in the paper
├── dashboards/                       Power BI artifacts (planned, Week 5)
├── scripts/
│   └── build_all_code.py             regenerates docs/ALL_CODE.md
├── docs/
│   ├── charter.md                    project charter (scope contract)
│   ├── methodology.md                methodology + assumptions + limitations
│   ├── data_collection.md            Google Trends export protocol
│   ├── my-understanding.md           author's plain-language notes
│   ├── linkedin-posts.md             public-content drafts
│   └── ALL_CODE.md                   single-file code aggregation for reviewers
├── requirements.txt                  Python dependencies (pinned via pip freeze)
├── README.md
└── LICENSE                           MIT
```

## Project status

**Analysis complete — white paper v1 published. Power BI dashboard in progress.**

| Phase | Status |
|-------|--------|
| Repo scaffolding, `.gitignore`, virtual environment | ✅ |
| Charter, methodology, data-collection protocol | ✅ |
| Google Trends data export (30 weekly CSVs, 2020 – 2025) | ✅ |
| Data loader + processed long-format dataset | ✅ |
| EDA notebook + data dictionary | ✅ |
| Time-series (STL) decomposition + Tết uplift calculation | ✅ |
| Publication figures | ✅ |
| White paper PDF (v1) | ✅ |
| Power BI dashboard | ⏭ in progress |
| LinkedIn content series | ⏭ drafts ready |
| Publish + distribute | ⏭ Week 8 |

**Target ship date:** 30 June 2026.

## Deliverables

(Per [`docs/charter.md`](docs/charter.md) §5.)

1. **This GitHub repository** — public, reproducible, MIT-licensed.
2. **White paper PDF** — [`output/whitepaper/whitepaper.pdf`](output/whitepaper/whitepaper.pdf) ✅ (v1 published, figures embedded).
3. **Power BI interactive dashboard** — 4 pages; embedded link will appear here when published.
4. **LinkedIn content series** — 3 – 4 posts; working drafts in [`docs/linkedin-posts.md`](docs/linkedin-posts.md).

## Reproducing the analysis

```bash
git clone https://github.com/phamlequanghuy/vn-fmcg-tet-effect.git
cd vn-fmcg-tet-effect

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
# source .venv/bin/activate

pip install -r requirements.txt
python src/load_data.py
```

Notes:

- The 30 raw Google Trends CSVs are committed under `data/raw/`. Google Trends values drift slightly over time as the index is reprocessed, so the committed CSVs are the canonical snapshot used for every finding in this project.
- `load_data.py` will print a validation summary (rows per `keyword × year`, max-per-file sanity check, duplicate-week detection) and emit `data/processed/trends_long.csv`.
- The notebooks (`notebooks/01–03`) reproduce the EDA, STL decomposition, and every figure embedded in the white paper.

## For reviewers

If you want to read every line of code in one place rather than navigating the repo, see [`docs/ALL_CODE.md`](docs/ALL_CODE.md). It is auto-generated from `src/`, `notebooks/`, and `scripts/` by running:

```bash
python scripts/build_all_code.py
```

## About the author

**Pham Le Quang Huy**

- MSc Supply Chain Management, Aston Business School (UK) — September 2026 intake
- Target post-graduation programme: **Unilever Future Leaders Programme (UFLP) UK**
- This project is the portfolio centrepiece supporting the UFLP application and serves as the foundation for MSc dissertation work at Aston.

For project context: see [`docs/charter.md`](docs/charter.md).
For methodology depth: see [`docs/methodology.md`](docs/methodology.md).
For the author's plain-language reasoning: see [`docs/my-understanding.md`](docs/my-understanding.md).

## License

MIT — see [`LICENSE`](LICENSE). Use, fork, adapt, criticise. Attribution appreciated when this framework is reused in industry or academic work.
