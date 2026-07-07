"""
Hack-You Report Generator
Version 3.0
"""

import json
from pathlib import Path
from datetime import datetime

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


class ReportGenerator:

    def __init__(self):
        self.time = datetime.now().strftime("%Y%m%d_%H%M%S")

    def save_json(self, module, data):

        filename = REPORT_DIR / f"{module}_{self.time}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return filename

    def save_text(self, module, data):

        filename = REPORT_DIR / f"{module}_{self.time}.txt"

        with open(filename, "w", encoding="utf-8") as f:

            f.write("=" * 60 + "\n")
            f.write("Hack-You Professional Report\n")
            f.write("=" * 60 + "\n\n")

            f.write(json.dumps(data, indent=4))

        return filename


report = ReportGenerator()