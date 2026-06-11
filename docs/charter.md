# PROJECT CHARTER

## Vietnam FMCG Tet Effect Quantification

**Owner:** Pham Le Quang Huy
**Created:** 1/5/2026
**Target completion:** 30/6/2026 (8 tuần)
**Version:** 1.0

---

## 1. PROBLEM STATEMENT

Tết (Lunar New Year) tạo ra một disruption khổng lồ trong demand FMCG Việt Nam mỗi năm — nhưng **mức độ disruption** thay đổi đáng kể giữa các product categories, và **timing** của uplift/dropoff không trùng với calendar Tết. Demand planners FMCG tại Việt Nam thường dùng heuristic "x2 demand 4 tuần trước Tết, x0.3 demand 2 tuần sau Tết" — nhưng không có baseline quantitative chuẩn cho mỗi category.

Project này quantify Tet Effect across multiple FMCG categories, build framework planners có thể use, và publish public để trở thành reference cho industry Việt Nam.

## 2. RESEARCH QUESTIONS

**Câu hỏi chính:**
> Tet Effect lên demand FMCG Việt Nam cụ thể như thế nào — về magnitude, timing, và variation across categories?

**Sub-questions:**
1. Trung bình demand spike bao nhiêu % so với non-Tet baseline cho mỗi category?
2. Demand bắt đầu spike khi nào (T-X tuần trước Tết) và kéo dài bao lâu?
3. Post-Tet demand drop sâu bao nhiêu và recover khi nào?
4. Categories nào Tet-sensitive nhất? Categories nào ít affected?
5. Pattern này có thay đổi giữa các năm không (COVID 2020-2021 là outlier?)

## 3. SCOPE — IN

- **Categories analyzed:** 5-7 FMCG categories
  - Beverages (beer, soft drinks)
  - Confectionery (mứt Tết, bánh kẹo)
  - Personal care (skincare, haircare)
  - Home care (detergent, dishwash)
  - Food staples (rice, cooking oil, fish sauce)
  - Snacks
  - Gift sets/seasonal SKUs

- **Time period:** 2018-2025 (8 năm Tết, bao gồm COVID outlier để stress-test)

- **Geographic scope:** Vietnam national level (regional breakdown trong v2 nếu thời gian cho phép)

- **Methodology:** Time-series decomposition + comparative baseline analysis

## 4. SCOPE — OUT

Để giữ scope manageable trong 8 tuần:

- Regional breakdown (HCMC vs Hanoi vs Đà Nẵng) — defer to v2
- Forecasting model build (predict next Tet) — defer to v2
- Promotion-corrected analysis (separate Tet effect from promo lift) — defer to v2
- Cross-country comparison (Tet vs Chinese New Year vs Western New Year) — defer to v3
- Real-time data pipeline — out of scope completely

## 5. DELIVERABLES

**Deliverable 1 — GitHub Repository (Public)**
- Clean Python codebase
- Reproducible analysis (anyone can clone và rerun)
- Documented data sources
- README comprehensive
- Repo name: `vn-fmcg-tet-effect`

**Deliverable 2 — Power BI Interactive Dashboard**
- 4 pages: Overview, Category Comparison, Temporal Patterns, Year-over-Year
- Interactive filters: category, year, timeframe
- Hosted as Power BI public report
- Embedded link in GitHub README

**Deliverable 3 — White Paper (PDF)**
- 8-10 pages
- Executive Summary (1 page)
- Context & Background (1.5 pages)
- Methodology (1 page)
- Findings — quantified Tet Effect framework (3-4 pages)
- Implications for Demand Planners (1.5 pages)
- Limitations & Future Work (0.5 pages)
- References

**Deliverable 4 — LinkedIn Content Series (3-4 posts)**
- Post 1 (Week 4): Project announcement + methodology preview
- Post 2 (Week 6): Key finding teaser với 1 chart
- Post 3 (Week 8): White paper release
- Post 4 (Week 10): Lessons learned reflection

## 6. SUCCESS CRITERIA

Project considered successful if:

**Minimum (must achieve):**
- ✓ Repository public với clean code
- ✓ White paper PDF published
- ✓ Quantified Tet Effect cho ít nhất 5 categories
- ✓ LinkedIn announcement post published

**Target (aim for):**
- ✓ Power BI dashboard live và public-accessible
- ✓ 7 categories analyzed
- ✓ 3+ LinkedIn posts với meaningful engagement (50+ reactions each)
- ✓ At least 2 industry professionals comment hoặc DM về project

**Stretch (bonus):**
- ✓ Project được pick up bởi Vietnam Supply Chain Council hoặc industry blog
- ✓ At least 1 Unilever/P&G/Nestlé Vietnam employee engage với content
- ✓ Featured trong Aston coursework / dissertation foundation

## 7. DATA SOURCES

**Primary sources:**
- General Statistics Office Vietnam (gso.gov.vn) — retail trade data monthly
- Nielsen Vietnam public reports (free executive summaries)
- Kantar Worldpanel Vietnam public reports
- Vietnam Ministry of Industry & Trade reports

**Secondary/proxy sources:**
- World Bank Vietnam consumption indicators
- Google Trends Vietnam (proxy for consumer interest)
- Public retail company annual reports (Vingroup, Masan, SaigonCoop)

**Risk:** Data granularity có thể không đủ chi tiết SKU level cho FMCG.
**Mitigation:** Use category-level aggregated data, supplement với public industry reports để estimate proportions.

## 8. TECHNICAL STACK

- **Python 3.11+** (analysis, data processing)
  - pandas, numpy (data manipulation)
  - statsmodels (time-series decomposition)
  - matplotlib, seaborn, plotly (visualization)
  - jupyter (notebook documentation)
- **Power BI Desktop** (dashboard)
- **Git + GitHub** (version control + hosting)
- **Markdown + LaTeX** (white paper drafting)
- **Notion** (project management, notes)

## 9. TIMELINE — 8 WEEKS

**Week 1 (5/5 - 11/5):** Foundation
- GitHub repo setup
- Project structure scaffolding
- Data sourcing — identify và download
- Read 5 reference papers về seasonality FMCG / Tet effect Vietnam

**Week 2 (12/5 - 18/5):** Data Pipeline
- Build data loader, cleaner, processor scripts
- EDA notebook v1 — understand data shape
- Documentation data dictionary

**Week 3 (19/5 - 25/5):** Core Analysis Phase 1
- Implement time-series decomposition
- Calculate baseline (non-Tet periods average)
- Calculate Tet uplift cho mỗi category
- LinkedIn Post 1 published

**Week 4 (26/5 - 1/6):** Core Analysis Phase 2
- Temporal pattern analysis (T-8 weeks to T+4 weeks around Tet)
- Year-over-year comparison
- Statistical significance testing
- COVID outlier handling

**Week 5 (2/6 - 8/6):** Dashboard Build
- Power BI dashboard layout
- Connect to processed data
- 4 pages with interactivity
- LinkedIn Post 2 published

**Week 6 (9/6 - 15/6):** White Paper Draft
- Outline finalize
- Write Methodology + Findings sections
- Embed charts từ analysis
- First draft complete

**Week 7 (16/6 - 22/6):** Polish & Review
- White paper review by 2 people (mentor, peer)
- Iterate based on feedback
- Dashboard polish — UX improvements
- Repository README comprehensive

**Week 8 (23/6 - 30/6):** Publish & Distribute
- White paper PDF final
- LinkedIn Post 3 (release announcement)
- Reach out to 5-10 industry contacts với link
- Submit to relevant Vietnam SCM communities
- Project retrospective document

## 10. TIME BUDGET

**Total estimated effort:** 150-180 hours
**Per-week average:** 20-22 hours
**Daily average:** 3-3.5 hours/day x 6 days/tuần (1 day rest)

**Buffer:** 20% built-in for unexpected blockers.

## 11. RISKS & MITIGATIONS

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Data sources disaggregated không đủ | High | High | Start với aggregated data, supplement với industry reports, accept limitation |
| Scope creep từ "thêm 1 thứ nữa" | High | High | Charter này là contract — không change scope without explicit decision |
| Technical blocker (Python skill gap) | Medium | Medium | Daily 30 phút Python practice trong Week 1, ask for help fast |
| Burnout từ pace 20-22 hr/tuần | Medium | High | Weekly review check-in, mandatory 1 day rest, downscale nếu signs |
| Overlap với Aston onboarding tháng 9 | Low | Medium | Project completed by 30/6, có buffer 2 tháng trước Aston |
| Quality gap giữa expectation và output | Medium | Low | Ship v1 ở tuần 8, iterate v2 nếu thời gian — không hold for perfect |

## 12. DECISION CHECKPOINTS

**End Week 2:** Data accessibility check
- Decision: Continue as planned, hoặc pivot to different angle nếu data không feasible

**End Week 4:** Analysis quality check
- Decision: Continue to dashboard phase, hoặc spend extra week on analysis

**End Week 6:** Scope check
- Decision: Push to ship v1 ở Week 8, hoặc accept 1-2 tuần slip (max)

**End Week 8:** Ship decision
- Decision: Publish v1 hoặc delay (default: PUBLISH, không delay)

## 13. POST-PROJECT (V2 EXTENSIONS — IF TIME)

If shipped v1 successfully và còn thời gian (July onwards):

**v2 candidates (pick 1):**
- Add regional breakdown (D2 angle)
- Add forecasting model layer (D3 angle)
- Add promotion-corrected analysis
- Translate white paper to English fully

**v2 timeline:** 4-6 tuần (July-mid August)

## 14. PERSONAL COMMITMENT

I commit to:

- Following this charter as scope contract
- Decision checkpoints honestly even if uncomfortable
- Shipping v1 by 30/6/2026 in some form
- Publishing publicly regardless of perfection level
- Documenting honestly — including failures và limitations
- Treating this project as portfolio centerpiece for UFLP application

---

**Charter approved:** [Date when you commit to this]
**Next milestone:** GitHub repository setup + Week 1 data sourcing
