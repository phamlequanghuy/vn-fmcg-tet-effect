"""Re-render the white paper's Figure 5 (STL decomposition of banh keo).

Faithful reproduction of notebooks/02_stl_decomposition.ipynb `plot_decomposition`
for the banh_keo series, with ONE addition: an annotation on the residual panel
flagging the large negative point at the start of the series as an STL boundary
(edge) effect, so readers do not misread it as a real demand shock (e.g. COVID).

Everything else (data, STL params period=52 robust, colours, layout, dpi=120,
bbox tight) matches the notebook so the figure is identical except for the new
annotation. Output goes only to the paper's figure path; no other figure changes.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "whitepaper" / "figures" / "02_stl_banh_keo.png"

KEYWORD = "banh_keo"
LABEL = "Banh keo (Confectionery)"

tet_dates = {
    2020: pd.Timestamp("2020-01-25"),
    2021: pd.Timestamp("2021-02-12"),
    2022: pd.Timestamp("2022-02-01"),
    2023: pd.Timestamp("2023-01-22"),
    2024: pd.Timestamp("2024-02-10"),
    2025: pd.Timestamp("2025-01-29"),
}

df = pd.read_csv(ROOT / "data" / "processed" / "trends_long.csv")
df["week_start"] = pd.to_datetime(df["week_start"])
df = df[df["week_start"].dt.year == df["year"]].copy()   # year-boundary dedup (methodology 4.6)

g = df[df["keyword"] == KEYWORD].sort_values("week_start")
series = pd.Series(
    g["search_index"].values,
    index=pd.DatetimeIndex(g["week_start"], freq="W-SUN"),
)
res = STL(series, period=52, robust=True).fit()

panels = [
    ("Observed", res.observed, "#1f77b4", False),
    ("Trend", res.trend, "#ff7f0e", False),
    ("Seasonal", res.seasonal, "#2ca02c", False),
    ("Residual", res.resid, "#7f7f7f", True),
]
fig, axes = plt.subplots(4, 1, figsize=(14, 11), sharex=True)

for ax, (name, s, color, is_resid) in zip(axes, panels):
    if is_resid:
        ax.axhline(0, color="black", linewidth=0.6)
        ax.scatter(s.index, s.values, s=9, color=color, alpha=0.8)
    else:
        ax.plot(s.index, s.values, color=color, linewidth=1.3)
    for year, t in tet_dates.items():
        ax.axvline(t, color="#d62728", linestyle="--", linewidth=0.7, alpha=0.5)
    ax.set_ylabel(name, fontsize=10, fontweight="bold")
    ax.grid(True, alpha=0.2)

# Caveat tag on the trend panel (unchanged from the notebook).
axes[1].text(
    0.005, 0.05,
    "Not real demand growth - artifact of per-file 0-100 normalization (see methodology 4.6)",
    transform=axes[1].transAxes, fontsize=8, style="italic", color="#aa3333",
    va="bottom", ha="left",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#aa3333", alpha=0.85),
)

# NEW: flag the start-of-series residual spike as an STL edge artifact, so it is
# not misread as a real event. Point at the most extreme residual in the first
# few weeks (the boundary region).
edge = res.resid.iloc[:4]
ex = edge.abs().idxmax()
ey = res.resid.loc[ex]
axes[3].annotate(
    "STL edge artifact, not a real event",
    xy=(ex, ey),
    xytext=(48, 20), textcoords="offset points",
    fontsize=8, style="italic", color="#aa3333",
    va="center", ha="left",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#aa3333", alpha=0.9),
    arrowprops=dict(arrowstyle="->", color="#aa3333", linewidth=0.9),
    zorder=6,
)

# Tet-year labels along the top panel.
top = axes[0].get_ylim()[1]
for year, t in tet_dates.items():
    axes[0].text(t, top * 0.99, f"Tet {year}", rotation=90,
                 fontsize=7, ha="center", va="top", color="#d62728")

axes[-1].set_xlabel("Week starting (Sunday)", fontsize=10)
fig.suptitle(
    f"STL decomposition (exploratory) - {LABEL} - Vietnam Google Trends 2020-2025",
    fontsize=13, fontweight="bold", y=0.995,
)
fig.text(
    0.5, 0.004,
    "Source: Google Trends Vietnam, pulled 2026-06-12. Additive STL, period=52, robust. "
    "Qualitative only - official metrics from 01_eda baseline comparison (methodology 4.6).",
    ha="center", fontsize=8, style="italic", color="gray",
)
plt.tight_layout(rect=[0, 0.015, 1, 0.985])

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=120, bbox_inches="tight")
print("Saved:", OUT.relative_to(ROOT), f"({OUT.stat().st_size // 1024} KB)")
print(f"Edge point flagged at {ex.date()} residual={ey:.1f}")
