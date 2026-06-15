"""Render output/whitepaper/whitepaper.md to whitepaper.pdf.

Engine: Chrome/Edge headless `--print-to-pdf` (Chromium). The previous PDF was
produced by wkhtmltopdf (Qt WebKit), which injected a vertical black-bar render
artifact across page 10. Chromium's print path does not produce that artifact.

Pipeline: markdown -> HTML (mistune, with table support) -> a print-styled HTML
document -> Chromium headless print-to-PDF. Figures are referenced relatively;
the temporary HTML is written next to figures/ so paths resolve, then removed.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

import mistune

ROOT = Path(__file__).resolve().parents[1]
WP_DIR = ROOT / "output" / "whitepaper"
MD = WP_DIR / "whitepaper.md"
PDF = WP_DIR / "whitepaper.pdf"
TMP_HTML = WP_DIR / "_whitepaper_render.html"

CHROME_CANDIDATES = [
    Path(r"C:/Program Files/Google/Chrome/Application/chrome.exe"),
    Path(r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
    Path(r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
    Path(r"C:/Program Files/Microsoft/Edge/Application/msedge.exe"),
]

CSS = """
@page { size: A4; margin: 19mm 17mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
html { font-size: 10.5pt; }
body {
  font-family: Georgia, 'Times New Roman', serif;
  color: #1a1a1a; line-height: 1.5; margin: 0;
}
h1, h2, h3, h4 {
  font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
  color: #11253f; line-height: 1.25; page-break-after: avoid;
}
h1 { font-size: 22pt; margin: 0 0 4px; }
h2 { font-size: 15pt; margin: 22px 0 8px; padding-bottom: 4px; border-bottom: 1px solid #d7dde5; }
h3 { font-size: 12pt; margin: 16px 0 6px; color: #1d3a5f; }
p { margin: 0 0 9px; }
a { color: #11457e; text-decoration: none; }
strong { color: #11253f; }
hr { border: none; border-top: 1px solid #ccd3db; margin: 16px 0; }
ul, ol { margin: 0 0 9px; padding-left: 22px; }
li { margin: 0 0 4px; }
img { max-width: 100%; height: auto; display: block; margin: 12px auto 4px; page-break-inside: avoid; }
table { border-collapse: collapse; width: 100%; margin: 10px 0 12px; font-size: 9.4pt;
        font-family: 'Segoe UI', Arial, sans-serif; page-break-inside: avoid; }
th, td { border: 1px solid #c4ccd6; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #eef2f7; color: #11253f; }
tr:nth-child(even) td { background: #f8fafc; }
blockquote { border-left: 3px solid #11457e; margin: 10px 0; padding: 6px 14px;
             background: #f6f8fb; color: #243245; font-style: italic; page-break-inside: avoid; }
code { font-family: Consolas, 'Courier New', monospace; background: #eef0f3;
       padding: 1px 4px; border-radius: 3px; font-size: 0.9em; }
em { color: #243245; }
/* Figure/table caption paragraphs (a paragraph that is wholly italic). */
p > em:only-child { display: block; text-align: center; font-size: 9pt; color: #5b6470; }
"""

HTML_TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Quantifying the Tet Effect in Vietnamese FMCG Demand</title>
<style>{css}</style></head>
<body>{body}</body></html>"""


def find_browser():
    for p in CHROME_CANDIDATES:
        if p.exists():
            return p
    sys.exit("No Chrome/Edge found for printing.")


def main():
    md_text = MD.read_text(encoding="utf-8")
    render_md = mistune.create_markdown(plugins=["table", "strikethrough", "url"])
    body = render_md(md_text)
    html = HTML_TEMPLATE.format(css=CSS, body=body)
    TMP_HTML.write_text(html, encoding="utf-8")

    browser = find_browser()
    file_url = TMP_HTML.resolve().as_uri()
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            str(browser),
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=20000",
            f"--user-data-dir={profile}",
            f"--print-to-pdf={PDF}",
            file_url,
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if res.stdout.strip():
        print("stdout:", res.stdout.strip()[:500])
    if res.stderr.strip():
        print("stderr:", res.stderr.strip()[:500])

    TMP_HTML.unlink(missing_ok=True)
    if not PDF.exists():
        sys.exit("PDF was not produced.")
    print(f"Rendered: {PDF.relative_to(ROOT)} ({PDF.stat().st_size // 1024} KB) via {browser.name}")


if __name__ == "__main__":
    main()
