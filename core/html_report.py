from pathlib import Path
import json

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


def create(module, data):

    file = REPORT_DIR / f"{module}.html"

    html = f"""
<html>

<head>

<title>Hack-You Report</title>

</head>

<body>

<h1>Hack-You Professional Report</h1>

<pre>

{json.dumps(data,indent=4)}

</pre>

</body>

</html>
"""

    with open(file, "w", encoding="utf-8") as f:
        f.write(html)

    return file