from pathlib import Path

import markdown


BASE_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = BASE_DIR / "reports"

MD_PATH = REPORTS_DIR / "final_report.md"
HTML_PATH = REPORTS_DIR / "final_report.html"


markdown_text = MD_PATH.read_text(encoding="utf-8")

html_body = markdown.markdown(
    markdown_text,
    extensions=[
        "extra",
        "tables",
        "toc",
        "sane_lists",
    ],
)

css = """
@page {
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    color: #222222;
    font-size: 11pt;
    line-height: 1.5;
    max-width: 900px;
    margin: 32px auto;
    padding: 0 28px;
}

h1 {
    font-size: 34px;
    line-height: 1.15;
    margin-bottom: 8px;
    color: #17324d;
}

h2 {
    font-size: 24px;
    margin-top: 36px;
    margin-bottom: 14px;
    color: #17324d;
    border-bottom: 1px solid #d9e2ec;
    padding-bottom: 8px;
}

h3 {
    font-size: 19px;
    margin-top: 28px;
    margin-bottom: 10px;
    color: #24496b;
}

h4 {
    font-size: 16px;
    margin-top: 22px;
    margin-bottom: 8px;
    color: #24496b;
}

p {
    margin-top: 0;
    margin-bottom: 13px;
}

ul, ol {
    margin-top: 4px;
    margin-bottom: 14px;
}

li {
    margin-bottom: 4px;
}

blockquote {
    border-left: 4px solid #9fbad1;
    margin: 18px 0;
    padding: 10px 18px;
    background: #f5f8fb;
    color: #263849;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 14px;
    margin-bottom: 22px;
    font-size: 10pt;
}

th {
    background: #17324d;
    color: white;
    font-weight: 600;
    padding: 8px 9px;
    text-align: left;
}

td {
    border-bottom: 1px solid #d8dee6;
    padding: 8px 9px;
    vertical-align: top;
}

tr:nth-child(even) td {
    background: #f7f9fb;
}

img {
    display: block;
    max-width: 92%;
    margin: 18px auto 12px auto;
}

hr {
    border: 0;
    border-top: 1px solid #d9e2ec;
    margin: 26px 0;
}

strong {
    color: #17324d;
}

a {
    color: #1f5f99;
    text-decoration: none;
}

code {
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 9pt;
    background: #f2f4f7;
    padding: 1px 3px;
    border-radius: 3px;
}

@media print {
    body {
        max-width: none;
        margin: 0;
        padding: 0;
        font-size: 10.5pt;
    }

    h1, h2, h3, h4 {
        break-after: avoid;
    }

    table, img {
        break-inside: avoid;
    }

    a {
        color: #1f5f99;
    }
}
"""

html_document = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>What Makes a Society Healthy?</title>
    <style>
    {css}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""

HTML_PATH.write_text(html_document, encoding="utf-8")

print(f"HTML created: {HTML_PATH}")
