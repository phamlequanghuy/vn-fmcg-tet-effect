"""Load Google Trends weekly CSVs from data/raw/ into one long-format dataset.

Input: 30 CSVs in data/raw/ named <keyword>_<year>.csv, each holding
one keyword's weekly search-interest series for one year (Google Trends
"multiTimeline" export, region=Vietnam, granularity=weekly).

Output:
    data/processed/trends_long.csv

Output schema (long format, one row per keyword-week):
    keyword         normalized slug, e.g. "bia", "banh_keo", "sua"
    keyword_label   bilingual display label, e.g. "Bia (Beer)"
    year            year per filename (NOTE: not always == week_start.year;
                    Google Trends weeks straddle Sun-Sat so a 2024 file
                    starts with the week of 2023-12-31)
    week_start      Sunday of the Google Trends week (datetime)
    search_index    float 0-100; "<1" sentinel from Trends mapped to 0.5
    below_threshold bool flag for rows that came in as "<1"
    source_file     original filename, kept for traceability

Limitation handled here — per-file 0-100 normalization
----------------------------------------------------------------
Each Google Trends export is normalized independently to 0-100 against
its own max. As a result the raw `search_index` values are NOT
comparable across files (i.e. not comparable across years for a single
keyword, and not comparable across keywords for a single year).

All within-year Tet-effect metrics in docs/methodology.md section 4 are
ratios over the within-year baseline mean, so they remain scale-invariant
under this normalization. Absolute cross-file comparisons are off the
table; see docs/methodology.md section 5 limitation L2 for the full
treatment.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"

FNAME_RE = re.compile(r"^(?P<keyword>.+?)_(?P<year>\d{4})\.csv$", re.IGNORECASE)

KEYWORD_LABELS = {
    "bia": "Bia (Beer)",
    "banh_keo": "Bánh kẹo (Confectionery)",
    "nuoc_ngot": "Nước ngọt (Soft drinks)",
    "dau_an": "Dầu ăn (Cooking oil)",
    "sua": "Sữa (Milk / Dairy)",
}


def parse_filename(path: Path) -> tuple[str, int]:
    m = FNAME_RE.match(path.name)
    if not m:
        raise ValueError(f"Filename does not match <keyword>_<year>.csv: {path.name}")
    return m["keyword"].lower(), int(m["year"])


def load_one(path: Path) -> pd.DataFrame:
    keyword, year = parse_filename(path)

    df = pd.read_csv(path, skiprows=2, encoding="utf-8")
    if df.shape[1] != 2:
        raise ValueError(
            f"{path.name}: expected 2 columns (Week, <keyword>: (Vietnam)), got {df.shape[1]}"
        )
    df.columns = ["week_start", "search_index_raw"]

    df["week_start"] = pd.to_datetime(df["week_start"], errors="raise")

    raw = df["search_index_raw"].astype(str).str.strip()
    df["below_threshold"] = raw.str.startswith("<")
    df["search_index"] = raw.replace({"<1": "0.5"}, regex=False).astype(float)

    if keyword not in KEYWORD_LABELS:
        raise ValueError(
            f"{path.name}: keyword '{keyword}' is not in KEYWORD_LABELS — "
            "update the mapping if a new keyword was added."
        )

    df["keyword"] = keyword
    df["keyword_label"] = KEYWORD_LABELS[keyword]
    df["year"] = year
    df["source_file"] = path.name

    return df[
        [
            "keyword",
            "keyword_label",
            "year",
            "week_start",
            "search_index",
            "below_threshold",
            "source_file",
        ]
    ]


def validate(df: pd.DataFrame, n_files: int) -> list[str]:
    """Return a list of human-readable validation findings; empty list = clean."""
    warnings: list[str] = []

    expected_files = 5 * 6
    if n_files != expected_files:
        warnings.append(
            f"Expected {expected_files} files (5 keywords x 6 years 2020-2025); found {n_files}."
        )

    pivot = df.groupby(["keyword", "year"]).size().unstack(fill_value=0)
    missing = (pivot == 0)
    if missing.any().any():
        gaps = [(k, y) for k in pivot.index for y in pivot.columns if pivot.loc[k, y] == 0]
        warnings.append(f"Missing (keyword, year) cells: {gaps}")

    max_per_file = df.groupby("source_file")["search_index"].max()
    not_100 = max_per_file[max_per_file != 100]
    if len(not_100) > 0:
        warnings.append(
            "Files whose max != 100 (per-file normalization should always peak at 100):\n"
            + not_100.to_string()
        )

    duplicate_keys = df.duplicated(subset=["keyword", "week_start"]).sum()
    if duplicate_keys > 0:
        warnings.append(
            f"{duplicate_keys} duplicate (keyword, week_start) rows — adjacent yearly "
            "files overlap on the Dec-31 / Jan-1 boundary week. Decide on a "
            "deduplication rule downstream."
        )

    return warnings


def print_summary(df: pd.DataFrame, out_path: Path, warnings: list[str]) -> None:
    print(f"\nLoaded {len(df):,} weekly rows from {df['source_file'].nunique()} files.")
    print(f"Keywords: {sorted(df['keyword'].unique())}")
    print(f"Years:    {sorted(df['year'].unique())}")
    print(
        f"Date span: {df['week_start'].min().date()} -> {df['week_start'].max().date()}"
    )

    print("\nRows per (keyword, year):")
    print(df.groupby(["keyword", "year"]).size().unstack(fill_value=0).to_string())

    bt = int(df["below_threshold"].sum())
    print(f"\nBelow-threshold weeks ('<1' in raw): {bt} of {len(df)}")

    print("\nMax search_index per source_file (should be 100 for every file):")
    print(df.groupby("source_file")["search_index"].max().to_string())

    if warnings:
        print("\n!! Validation warnings:")
        for w in warnings:
            print(f"  - {w}")
    else:
        print("\nValidation: clean (no warnings).")

    print(f"\nSaved long-format dataset to: {out_path.relative_to(ROOT)}")


def main() -> int:
    raw_files = sorted(RAW_DIR.glob("*.csv"))
    if not raw_files:
        print(f"No CSVs found in {RAW_DIR}", file=sys.stderr)
        return 1

    frames = [load_one(p) for p in raw_files]
    combined = pd.concat(frames, ignore_index=True).sort_values(
        ["keyword", "week_start"]
    ).reset_index(drop=True)

    warnings = validate(combined, n_files=len(raw_files))

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    out_path = PROCESSED_DIR / "trends_long.csv"
    combined.to_csv(out_path, index=False, encoding="utf-8")

    print_summary(combined, out_path, warnings)
    return 0


if __name__ == "__main__":
    sys.exit(main())
