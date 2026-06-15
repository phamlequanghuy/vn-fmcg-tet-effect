"""Generate the LinkedIn Post 3 (white-paper wrap-up) summary chart.

A horizontal bar chart ranking the five FMCG categories by mean peak Tet
uplift %, making the "Tet is not blanket" finding visible at a glance:
the three Tet-sensitive categories are coloured a bold festive red, the two
non-spiking categories a muted grey for contrast.

Numbers are the published six-year (2020-2025) means from the white paper
(Table 3.1): search-implied, expressed as uplift relative to each category's
own within-year non-Tet baseline. This is descriptive of figures already
committed in output/whitepaper/whitepaper.md, not a re-computation.

Output: output/linkedin/summary_ranking.png  (4:5, mobile-friendly)
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "linkedin" / "summary_ranking.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

# (ASCII label, peak uplift %, is_tet_spike) — already sorted descending.
CATS = [
    ("Banh keo (Confectionery)", 130, True),
    ("Bia (Beer)", 129, True),
    ("Nuoc ngot (Soft drinks)", 82, True),
    ("Dau an (Cooking oil)", -9, False),
    ("Sua (Milk / Dairy)", -19, False),
]

SPIKE = "#d62728"    # festive red — strong, repeatable Tet spike
NOSPIKE = "#c2c8d0"  # muted grey — no detected Tet spike
INK = "#1a1a1a"
MUTE = "#5b6470"

labels = [c[0] for c in CATS]
vals = [c[1] for c in CATS]
colors = [SPIKE if c[2] else NOSPIKE for c in CATS]

fig, ax = plt.subplots(figsize=(8.0, 10.0), dpi=135)  # -> 1080 x 1350
fig.subplots_adjust(left=0.33, right=0.95, top=0.70, bottom=0.14)

y = list(range(len(CATS)))
ax.barh(y, vals, color=colors, height=0.60, zorder=3)
ax.invert_yaxis()  # highest-ranked category on top

# Baseline (0% = each category's own non-Tet normal).
ax.axvline(0, color="#444", linewidth=1.1, zorder=2)

# Value labels: positive bars get the % at the bar tip; the two non-spiking
# rows have empty space to the right of 0, so the label sits there instead of
# colliding with the category names on the left.
for yi, v in zip(y, vals):
    if v >= 0:
        ax.text(v + 4, yi, f"+{v}%", va="center", ha="left",
                fontsize=16, fontweight="bold", color=SPIKE, zorder=4)
    else:
        ax.text(6, yi, f"{v}%  ·  no spike", va="center", ha="left",
                fontsize=13.5, fontweight="bold", color=MUTE, zorder=4)

# Note in the open space beside the two non-spiking rows.
ax.text(70, 3.5, "No Tet spike —\npeak season is elsewhere\n(dairy peaks in June)",
        fontsize=12, color=MUTE, va="center", ha="left", style="italic",
        linespacing=1.4)

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=13.5, color=INK)
ax.set_xlim(-40, 168)
ax.xaxis.set_major_formatter(PercentFormatter())
ax.tick_params(axis="x", labelsize=11, colors=MUTE)
ax.set_xlabel("Peak search uplift vs each category's own non-Tet baseline",
              fontsize=11.5, color=MUTE)
for spine in ("top", "right", "left"):
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#999")

# Storytelling title + subtitle (top-anchored so they stack cleanly).
fig.text(0.045, 0.965, "Tet lifts 3 of 5 FMCG categories — not all",
         fontsize=21, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.045, 0.905,
         "Six years of Vietnam search data (2020–2025) vs the planner rule of\n"
         "thumb that \"Tet lifts everything.\" It doesn't — beverages and\n"
         "confectionery carry the spike; cooking oil and dairy don't.",
         fontsize=12.5, color=MUTE, ha="left", va="top", linespacing=1.5)

# Source line + repo link.
fig.text(0.045, 0.055,
         "Source: Google Trends Vietnam (weekly), 2020–2025 — search-implied uplift, "
         "six-year mean per category.\n"
         "Full white paper & code: github.com/phamlequanghuy/vn-fmcg-tet-effect",
         fontsize=9.5, color=MUTE, ha="left", va="top", linespacing=1.5)

fig.savefig(OUT, dpi=135, facecolor="white")
print("Saved:", OUT.relative_to(ROOT), f"({OUT.stat().st_size // 1024} KB)")
