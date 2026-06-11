# Vietnam FMCG Tet Effect

> A public framework for quantifying Lunar New Year (Tết) demand patterns in Vietnamese FMCG categories — built for demand planners, accessible to industry researchers.

[![Status](https://img.shields.io/badge/status-Week_1_of_8-orange)](docs/charter.md)
[![Methodology](https://img.shields.io/badge/methodology-v1_locked-brightgreen)](docs/methodology.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

---

## Overview

Tết (Lunar New Year) is the single largest annual demand event in Vietnamese FMCG. Yet planners commonly rely on a heuristic — *"x2 demand four weeks before Tet, x0.3 demand two weeks after"* — without any public, per-category, quantitative baseline.

This project quantifies the **Tet Effect** — magnitude, timing, recovery shape — across five Vietnamese FMCG categories over six consecutive Tet cycles (2020–2025), using Google Trends Vietnam as a search-implied demand proxy.

The framework is intentionally **public and reproducible**: all raw data, code, methodology, and limitations are committed to this repository so any demand planner or researcher can clone, rerun, and extend it.

## Research questions

(Detailed in [`docs/charter.md`](docs/charter.md) §2.)

1. By what percentage does demand spike above the non-Tet baseline, per category?
2. When does demand start spiking (T − X weeks before Tet) and how long does the spike last?
3. How deep is the post-Tet drop, and when does it recover?
4. Which categories are most / least Tet-sensitive?
5. Does the pattern shift across years — is COVID (2020 – 2021) an outlier?

## Categories analysed

| # | Category | Vietnamese keyword | English label |
|---|----------|--------------------|---------------|
| 1 | Beer | `bia` | Beer |
| 2 | Confectionery | `bánh kẹo` | Confectionery |
| 3 | Soft drinks | `nước ngọt` | Soft drinks |
| 4 | Cooking oil | `dầu ăn` | Cooking oil |
| 5 | Milk / Dairy | `sữa` | Milk / Dairy |

Time coverage: weekly granularity, 2020 – 2025 inclusive (6 Tet cycles).

## Methodology summary

Full treatment with every assumption and limitation in [`docs/methodology.md`](docs/methodology.md). Headlines:

- **Data source.** Google Trends Vietnam search volume, used as a *proxy for consumer interest*. All findings are framed as **search-implied Tet effect**, not as sales.
- **Tet windowing.** Pre-Tet build-up = `T − 6 weeks` to `T − 1 day`; Tet holiday = `T` to `T + 7 days`; recovery window = `T + 8 days` to `T + 4 weeks`. `T` is the Gregorian date of Mùng 1 Tết (Lunar Jan 1) for each year.
- **Core metrics.** Build-up uplift %, holiday dip %, recovery time in weeks, peak timing relative to T. All four are within-year ratios over that year's own baseline.
- **Normalization handling.** Google Trends returns 0 – 100 normalized per file. Every metric is a within-file ratio, which is scale-invariant under the per-file normalization — so the constraint does not invalidate the framework. Absolute cross-file comparisons (e.g. "beer 2024 was X% bigger than beer 2020 in absolute search volume") are explicitly off the table.

The methodology document lists seven limitations: search ≠ purchase, per-file normalization, demographic skew toward urban search users, keyword choice sensitivity, temporal aggregation forced by Trends, COVID confounding in 2020 – 2021, and no SKU / brand resolution.

## Repository structure

```
vn-fmcg-tet-effect/
├── data/
│   ├── raw/                 30 Google Trends CSVs (5 keywords × 6 years)
│   └── processed/           trends_long.csv (combined long-format dataset)
├── src/
│   └── load_data.py         load + validate + emit processed dataset
├── notebooks/               EDA + analysis notebooks (in progress)
├── dashboards/              Power BI artifacts (planned, Week 5)
├── scripts/
│   └── build_all_code.py    regenerates docs/ALL_CODE.md
├── docs/
│   ├── charter.md           project charter (scope contract)
│   ├── methodology.md       methodology + assumptions + limitations
│   ├── data_collection.md   Google Trends export protocol
│   ├── linkedin-posts.md    public-content drafts (4 posts)
│   ├── my-understanding.md  author's plain-language notes
│   └── ALL_CODE.md          single-file code aggregation for reviewers
├── output/
│   └── whitepaper/          white paper draft (planned, Week 6 – 8)
├── requirements.txt         Python dependencies (pinned via pip freeze)
├── README.md
└── LICENSE                  MIT
```

## Project status

**Week 1 of 8 — foundation phase complete.**

| Phase | Status |
|-------|--------|
| Repo scaffolding, `.gitignore`, virtual environment | ✅ |
| Charter, methodology, data-collection protocol | ✅ |
| Google Trends data export (30 weekly CSVs, 2020 – 2025) | ✅ |
| Data loader + processed long-format dataset | ✅ |
| EDA notebook v1 + data dictionary | ⏭ Week 2 |
| Time-series decomposition + Tet uplift calculation | ⏭ Week 3 |
| Year-over-year analysis + COVID outlier handling | ⏭ Week 4 |
| Power BI dashboard | ⏭ Week 5 |
| White paper draft | ⏭ Week 6 |
| Review and polish | ⏭ Week 7 |
| Publish + distribute | ⏭ Week 8 |

**Target ship date:** 30 June 2026.

## Deliverables

(Per [`docs/charter.md`](docs/charter.md) §5.)

1. **This GitHub repository** — public, reproducible, MIT-licensed.
2. **Power BI interactive dashboard** — 4 pages; embedded link will appear here at Week 5.
3. **White paper PDF** — 8 – 10 pages; will appear in `output/whitepaper/` at Week 8.
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

## License

MIT — see [`LICENSE`](LICENSE). Use, fork, adapt, criticise. Attribution appreciated when this framework is reused in industry or academic work.
