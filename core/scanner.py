"""
Hack-You Professional Scanner Manager
Version : 3.0
"""

from core.engine import ScanEngine
from core.logger import info, error
from core.database import db


class Scanner:

    def __init__(self, threads=50):
        self.engine = ScanEngine(threads)

    def run(self, module_name, scan_function, targets):
        """
        Run any scanner module.
        """

        info(f"Starting {module_name}")

        try:

            results = self.engine.run(
                scan_function,
                targets
            )

            for result in results:

                try:

                    db.add_scan(
                        module_name,
                        result.get("target", ""),
                        str(result)
                    )

                except Exception:
                    pass

            info(f"{module_name} completed")

            return results

        except Exception as e:

            error(str(e))

            return []

    def run_single(self, module_name, scan_function, target):

        return self.run(
            module_name,
            scan_function,
            [target]
        )