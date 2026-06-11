# PROJECT CHARTER

## Vietnam FMCG Tet Effect Quantification

**Owner:** Pham Le Quang Huy
**Created:** 1 May 2026
**Target completion:** 30 June 2026 (8 weeks)
**Version:** 1.0

---

## 1. PROBLEM STATEMENT

Tết (Lunar New Year) creates a massive annual disruption to FMCG demand in Vietnam — but the **magnitude** of the disruption varies materially across product categories, and the **timing** of the uplift / dropoff does not coincide with the Gregorian calendar Tet date. Vietnamese FMCG demand planners typically rely on a heuristic — "x2 demand four weeks before Tet, x0.3 demand two weeks after Tet" — without a quantitative per-category baseline.

This project quantifies the Tet Effect across multiple FMCG categories, builds a framework that planners can use, and publishes it publicly so it can serve as a reference for the Vietnamese industry.

## 2. RESEARCH QUESTIONS

**Primary question:**
> How does the Tet Effect manifest in Vietnamese FMCG demand — in magnitude, in timing, and in variation across categories?

**Sub-questions:**
1. On average, by what percentage does demand spike above the non-Tet baseline, per category?
2. When does demand start spiking (T − X weeks before Tet) and how long does the spike last?
3. How deep is the post-Tet demand drop, and when does it recover?
4. Which categories are the most Tet-sensitive? Which are the least affected?
5. Does the pattern shift between years (is COVID 2020–2021 an outlier)?

## 3. SCOPE — IN

- **Categories analysed:** 5–7 FMCG categories
  - Beverages (beer, soft drinks)
  - Confectionery (mứt Tết — Tet candied fruit; bánh kẹo — confectionery)
  - Personal care (skincare, haircare)
  - Home care (detergent, dishwash)
  - Food staples (rice, cooking oil, fish sauce)
  - Snacks
  - Gift sets / seasonal SKUs

- **Time period:** 2020–2025 (6 Tet cycles, including the COVID-affected 2020 and 2021 Tets for stress-testing)

- **Geographic scope:** Vietnam national level (regional breakdown deferred to v2 if time allows)

- **Methodology:** Time-series decomposition + comparative baseline analysis

## 4. SCOPE — OUT

To keep scope manageable within 8 weeks:

- Regional breakdown (HCMC vs Hanoi vs Đà Nẵng) — defer to v2
- Forecasting model build (predict next Tet) — defer to v2
- Promotion-corrected analysis (separating the Tet effect from promo lift) — defer to v2
- Cross-country comparison (Tet vs Chinese New Year vs Western New Year) — defer to v3
- Real-time data pipeline — out of scope entirely

## 5. DELIVERABLES

**Deliverable 1 — GitHub Repository (Public)**
- Clean Python codebase
- Reproducible analysis (anyone can clone and rerun)
- Documented data sources
- Comprehensive README
- Repository name: `vn-fmcg-tet-effect`

**Deliverable 2 — Power BI Interactive Dashboard**
- 4 pages: Overview, Category Comparison, Temporal Patterns, Year-over-Year
- Interactive filters: category, year, timeframe
- Hosted as a Power BI public report
- Embedded link in the GitHub README

**Deliverable 3 — White Paper (PDF)**
- 8–10 pages
- Executive Summary (1 page)
- Context & Background (1.5 pages)
- Methodology (1 page)
- Findings — quantified Tet Effect framework (3–4 pages)
- Implications for Demand Planners (1.5 pages)
- Limitations & Future Work (0.5 pages)
- References

**Deliverable 4 — LinkedIn Content Series (3–4 posts)**
- Post 1 (Week 4): Project announcement + methodology preview
- Post 2 (Week 6): Key finding teaser with one chart
- Post 3 (Week 8): White paper release
- Post 4 (Week 10): Lessons learned reflection

## 6. SUCCESS CRITERIA

The project is considered successful if:

**Minimum (must achieve):**
- ✓ Repository public with clean code
- ✓ White paper PDF published
- ✓ Tet Effect quantified for at least 5 categories
- ✓ LinkedIn announcement post published

**Target (aim for):**
- ✓ Power BI dashboard live and publicly accessible
- ✓ 7 categories analysed
- ✓ 3+ LinkedIn posts with meaningful engagement (50+ reactions each)
- ✓ At least 2 industry professionals comment or DM about the project

**Stretch (bonus):**
- ✓ Project picked up by the Vietnam Supply Chain Council or an industry blog
- ✓ At least 1 Unilever / P&G / Nestlé Vietnam employee engages with the content
- ✓ Featured in Aston coursework / used as dissertation foundation

## 7. DATA SOURCES

**Primary sources:**
- General Statistics Office Vietnam (gso.gov.vn) — monthly retail trade data
- Nielsen Vietnam public reports (free executive summaries)
- Kantar Worldpanel Vietnam public reports
- Vietnam Ministry of Industry & Trade reports

**Secondary / proxy sources:**
- World Bank Vietnam consumption indicators
- Google Trends Vietnam (proxy for consumer interest)
- Public retail company annual reports (Vingroup, Masan, SaigonCoop)

**Risk:** Data granularity may not be sufficient at SKU level for FMCG.
**Mitigation:** Use category-level aggregated data, supplemented with public industry reports to estimate proportions.

> **Note (2026-06-12):** During execution this assumption did not hold — public granular sales data is not available at the category × week resolution needed. Google Trends was elevated from "secondary / proxy" to **primary** data source. See `docs/methodology.md` §1.

## 8. TECHNICAL STACK

- **Python 3.11+** (analysis, data processing)
  - pandas, numpy (data manipulation)
  - statsmodels (time-series decomposition)
  - matplotlib, seaborn, plotly (visualisation)
  - jupyter (notebook documentation)
- **Power BI Desktop** (dashboard)
- **Git + GitHub** (version control + hosting)
- **Markdown + LaTeX** (white paper drafting)
- **Notion** (project management, notes)

## 9. TIMELINE — 8 WEEKS

**Week 1 (5–11 May):** Foundation
- GitHub repo setup
- Project structure scaffolding
- Data sourcing — identify and download
- Read 5 reference papers on FMCG seasonality / Vietnamese Tet effect

**Week 2 (12–18 May):** Data Pipeline
- Build data loader, cleaner, processor scripts
- EDA notebook v1 — understand data shape
- Documentation / data dictionary

**Week 3 (19–25 May):** Core Analysis Phase 1
- Implement time-series decomposition
- Calculate baseline (non-Tet period average)
- Calculate Tet uplift per category
- LinkedIn Post 1 published

**Week 4 (26 May – 1 June):** Core Analysis Phase 2
- Temporal pattern analysis (T − 8 weeks to T + 4 weeks around Tet)
- Year-over-year comparison
- Statistical significance testing
- COVID outlier handling

**Week 5 (2–8 June):** Dashboard Build
- Power BI dashboard layout
- Connect to processed data
- 4 pages with interactivity
- LinkedIn Post 2 published

**Week 6 (9–15 June):** White Paper Draft
- Outline finalised
- Write Methodology + Findings sections
- Embed charts from analysis
- First draft complete

**Week 7 (16–22 June):** Polish & Review
- White paper reviewed by 2 people (mentor, peer)
- Iterate based on feedback
- Dashboard polish — UX improvements
- Repository README comprehensive

**Week 8 (23–30 June):** Publish & Distribute
- White paper PDF finalised
- LinkedIn Post 3 (release announcement)
- Reach out to 5–10 industry contacts with the link
- Submit to relevant Vietnam SCM communities
- Project retrospective document

## 10. TIME BUDGET

**Total estimated effort:** 150–180 hours
**Per-week average:** 20–22 hours
**Daily average:** 3–3.5 hours/day × 6 days/week (1 rest day)

**Buffer:** 20% built-in for unexpected blockers.

## 11. RISKS & MITIGATIONS

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Data sources not disaggregated enough | High | High | Start with aggregated data, supplement with industry reports, accept the limitation |
| Scope creep ("just one more thing") | High | High | This charter is the contract — no scope change without an explicit decision |
| Technical blocker (Python skill gap) | Medium | Medium | 30 minutes of daily Python practice in Week 1; ask for help quickly |
| Burnout at 20–22 hr/week pace | Medium | High | Weekly review check-in; mandatory 1 rest day; downscale if early signs appear |
| Overlap with Aston onboarding in September | Low | Medium | Project completed by 30 June; 2-month buffer before Aston |
| Quality gap between expectation and output | Medium | Low | Ship v1 at Week 8 and iterate v2 if time allows — do not hold for perfect |

## 12. DECISION CHECKPOINTS

**End of Week 2:** Data accessibility check
- Decision: continue as planned, or pivot to a different angle if data is not feasible.

**End of Week 4:** Analysis quality check
- Decision: continue to the dashboard phase, or spend an extra week on analysis.

**End of Week 6:** Scope check
- Decision: push to ship v1 at Week 8, or accept a 1–2 week slip (maximum).

**End of Week 8:** Ship decision
- Decision: publish v1 or delay (default: PUBLISH, do not delay).

## 13. POST-PROJECT (V2 EXTENSIONS — IF TIME)

If v1 ships successfully and time remains (July onwards):

**v2 candidates (pick 1):**
- Add regional breakdown (D2 angle)
- Add forecasting model layer (D3 angle)
- Add promotion-corrected analysis
- Translate the white paper into Vietnamese for the local FMCG practitioner audience

**v2 timeline:** 4–6 weeks (July to mid-August)

## 14. PERSONAL COMMITMENT

I commit to:

- Following this charter as the scope contract
- Honouring the decision checkpoints honestly even when uncomfortable
- Shipping v1 by 30 June 2026 in some form
- Publishing publicly regardless of perfection level
- Documenting honestly — including failures and limitations
- Treating this project as the portfolio centrepiece for my UFLP application

---

**Charter approved:** [Date when commitment is made]
**Next milestone:** GitHub repository setup + Week 1 data sourcing
