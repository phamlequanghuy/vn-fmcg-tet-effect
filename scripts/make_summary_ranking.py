"""Generate the LinkedIn Post 3 (white-paper wrap-up) summary chart.

This is the project's hero chart: it must carry the full story with no caption.
A horizontal bar chart ranks the five FMCG categories by mean peak Tet uplift %,
with the three Tet-sensitive categories in bold red and the two non-spiking
categories in muted grey. The key insights (peak timing, beer's holiday-week
consumption, the two no-spike categories) are annotated directly on the chart.

Numbers are the published six-year (2020-2025) means from the white paper
(Table 3.1): search-implied, expressed as uplift relative to each category's
own within-year non-Tet baseline. This is descriptive of figures already
committed in output/whitepaper/whitepaper.md, not a re-computation.

Text style: no em/en dashes (they read as AI); short, natural phrasing; key
numbers highlighted in colour so the eye catches them immediately.

Output: output/linkedin/summary_ranking.png  (4:5, mobile-friendly)
"""
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "linkedin" / "summary_ranking.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

# (ASCII label, peak uplift %, is_tet_spike) -- already sorted descending.
CATS = [
    ("Banh keo (Confectionery)", 130, True),
    ("Bia (Beer)", 129, True),
    ("Nuoc ngot (Soft drinks)", 82, True),
    ("Dau an (Cooking oil)", -9, False),
    ("Sua (Milk / Dairy)", -19, False),
]

SPIKE = "#d62728"     # festive red  -> strong, repeatable Tet spike
NOSPIKE = "#c2c8d0"   # muted grey   -> no detected Tet spike
HILITE = "#ffd34d"    # warm yellow  -> highlighted number on a red bar
INK = "#1a1a1a"
MUTE = "#5b6470"
WHITE = "#ffffff"

labels = [c[0] for c in CATS]
vals = [c[1] for c in CATS]
colors = [SPIKE if c[2] else NOSPIKE for c in CATS]

fig, ax = plt.subplots(figsize=(8.4, 10.5), dpi=130)  # -> 1092 x 1365 (4:5)
fig.subplots_adjust(left=0.30, right=0.97, top=0.80, bottom=0.135)

y = list(range(len(CATS)))
ax.barh(y, vals, color=colors, height=0.66, zorder=3)
ax.set_ylim(4.75, -0.85)            # inverted: highest-ranked on top
ax.set_xlim(-52, 172)
ax.axvline(0, color="#444", linewidth=1.1, zorder=2)   # baseline = own normal

# Strip the quantitative axis -- value labels carry the numbers (social-first).
ax.set_xticks([])
for spine in ("top", "right", "left", "bottom"):
    ax.spines[spine].set_visible(False)
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=13.5, color=INK)
ax.tick_params(axis="y", length=0)

# Value labels at each bar tip.
ax.text(133, 0, "+130%", va="center", ha="left", fontsize=16, fontweight="bold", color=SPIKE)
ax.text(132, 1, "+129%", va="center", ha="left", fontsize=16, fontweight="bold", color=SPIKE)
ax.text(85, 2, "+82%", va="center", ha="left", fontsize=16, fontweight="bold", color=SPIKE)
ax.text(-12, 3, "-9%", va="center", ha="right", fontsize=14, fontweight="bold", color=MUTE)
ax.text(-22, 4, "-19%", va="center", ha="right", fontsize=14, fontweight="bold", color=MUTE)

# Insight annotations, white-on-red, inside the wide bars.
ax.text(7, -0.14, "Peaks 1 to 2 weeks before Tet,", va="center", ha="left",
        fontsize=11, fontweight="bold", color=WHITE, zorder=5)
ax.text(7, 0.16, "not the 4 weeks planners assume.", va="center", ha="left",
        fontsize=11, fontweight="bold", color=WHITE, zorder=5)

# Beer: lines 2-3 plain; line 1 has a highlighted +51% (drawn after render below).
ax.text(6, 1.02, "holiday week itself.", va="center", ha="left",
        fontsize=11.5, fontweight="bold", color=WHITE, zorder=5)
ax.text(6, 1.26, "Consumption, not just stocking.", va="center", ha="left",
        fontsize=11.5, fontweight="bold", color=WHITE, zorder=5)

# No-spike group note, in the open space to the right of the two grey bars.
ax.text(14, 3.30, "No Tet spike.", va="center", ha="left",
        fontsize=13, fontweight="bold", color=MUTE)
ax.text(14, 3.62, "Their peak season is elsewhere", va="center", ha="left",
        fontsize=12, color=MUTE, style="italic")
ax.text(14, 3.90, "(dairy peaks in June).", va="center", ha="left",
        fontsize=12, color=MUTE, style="italic")

# --- Coloured, width-aware text (title + the +51% inline highlight) ---
fig.canvas.draw()
R = fig.canvas.get_renderer()


def chain(add_text, inv, start_x, y, segments):
    """Draw left-to-right segments [(text, color), ...], advancing by rendered width."""
    xx = start_x
    for text, color in segments:
        t = add_text(xx, y, text, color)
        bb = t.get_window_extent(renderer=R)
        xx += inv.transform((bb.x1, 0))[0] - inv.transform((bb.x0, 0))[0]


# Title: "Tet does NOT lift all of FMCG", with NOT in red.
chain(
    lambda x, yy, txt, col: fig.text(x, yy, txt, fontsize=23, fontweight="bold",
                                     color=col, ha="left", va="top"),
    fig.transFigure.inverted(), 0.045, 0.965,
    [("Tet does ", INK), ("NOT", SPIKE), (" lift all of FMCG", INK)],
)

# Beer line 1, inside the bar: "Beer stays +51% through the" with +51% in yellow.
chain(
    lambda x, yy, txt, col: ax.text(x, yy, txt, fontsize=11.5, fontweight="bold",
                                    color=col, ha="left", va="center", zorder=5),
    ax.transData.inverted(), 6, 0.78,
    [("Beer stays ", WHITE), ("+51%", HILITE), (" through the", WHITE)],
)

# Sub-line under the title and the baseline clarifier.
fig.text(0.045, 0.905, "Search-implied. 6 Tet cycles, 2020 to 2025.",
         fontsize=13, color=MUTE, ha="left", va="top")
fig.text(0.045, 0.105,
         "Bars show peak search uplift vs each category's own normal (non-Tet) week.",
         fontsize=10.5, color=MUTE, ha="left", va="top")

# Source line + repo link.
fig.text(0.045, 0.055,
         "Source: Google Trends Vietnam (weekly), 2020 to 2025. "
         "Search-implied uplift, six-year mean per category.\n"
         "Full white paper and code: github.com/phamlequanghuy/vn-fmcg-tet-effect",
         fontsize=9.5, color=MUTE, ha="left", va="top", linespacing=1.5)

fig.savefig(OUT, dpi=130, facecolor="white")
print("Saved:", OUT.relative_to(ROOT), f"({OUT.stat().st_size // 1024} KB)")
