from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.console import Console
import traceback

console = Console()


class ScanEngine:
    """
    Professional Scan Engine
    ------------------------
    Features:
    - Multi-threading
    - Progress Bar
    - Error Handling
    - Callback Support
    - Logging Ready
    """

    def __init__(self, threads=50):
        self.threads = threads

    def run(
        self,
        function,
        targets,
        callback=None,
        ignore_errors=True,
    ):
        """
        Run a scan function against multiple targets.

        Parameters
        ----------
        function : callable
            Function to execute.

        targets : list
            List of targets.

        callback : callable
            Optional callback after every result.

        ignore_errors : bool
            Continue scanning even if one target fails.
        """

        results = []

        if not targets:
            console.print("[yellow]No targets supplied.[/yellow]")
            return results

        with Progress(
            SpinnerColumn(),
            TextColumn("[bold cyan]{task.description}"),
            BarColumn(),
            TextColumn("{task.completed}/{task.total}"),
            TimeElapsedColumn(),
        ) as progress:

            task = progress.add_task(
                "Scanning",
                total=len(targets),
            )

            with ThreadPoolExecutor(
                max_workers=self.threads
            ) as executor:

                futures = {
                    executor.submit(function, target): target
                    for target in targets
                }

                for future in as_completed(futures):

                    target = futures[future]

                    try:

                        result = future.result()

                        results.append(result)

                        if callback:
                            callback(result)

                    except Exception as e:

                        console.print(
                            f"[red]Error scanning {target}: {e}[/red]"
                        )

                        if not ignore_errors:
                            raise

                        results.append(
                            {
                                "target": target,
                                "error": str(e),
                                "traceback": traceback.format_exc(),
                            }
                        )

                    progress.update(task, advance=1)

        return results