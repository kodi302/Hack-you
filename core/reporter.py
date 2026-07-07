"""
Hack-You Professional Report Generator
Version : 2.0
"""

import json
from datetime import datetime
from pathlib import Path

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


def generate_report(
    target,
    dns_data,
    subdomains,
    open_ports,
    directories,
):
    """
    Generate JSON + HTML Report
    """

    report = {
        "target": target,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dns": dns_data,
        "subdomains": subdomains,
        "ports": open_ports,
        "directories": directories,
        "summary": {
            "subdomains": len(subdomains),
            "open_ports": len(open_ports),
            "directories": len(directories)
        }
    }

    # JSON Report
    json_file = REPORT_DIR / f"{target}_report.json"

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    # HTML Report
    html_file = REPORT_DIR / f"{target}_report.html"

    html = f"""
<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<title>Hack-You Report</title>

<style>

body{{
font-family:Arial;
background:#111;
color:#eee;
padding:30px;
}}

table{{
border-collapse:collapse;
width:100%;
}}

td,th{{
border:1px solid #444;
padding:8px;
}}

th{{
background:#00b894;
}}

h1,h2{{
color:#00cec9;
}}

pre{{
background:#222;
padding:10px;
}}

</style>

</head>

<body>

<h1>Hack-You Professional Report</h1>

<h2>Target</h2>

<p>{target}</p>

<h2>Summary</h2>

<table>

<tr>
<th>Open Ports</th>
<th>Subdomains</th>
<th>Directories</th>
</tr>

<tr>

<td>{len(open_ports)}</td>

<td>{len(subdomains)}</td>

<td>{len(directories)}</td>

</tr>

</table>

<h2>Full Result</h2>

<pre>

{json.dumps(report,indent=4)}

</pre>

</body>

</html>
"""

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n[+] JSON Report : {json_file}")
    print(f"[+] HTML Report : {html_file}")

    return report