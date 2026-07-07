import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from rich.console import Console

console = Console()

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "hackyou.log"

logger = logging.getLogger("HackYou")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s | %(message)s",
    "%Y-%m-%d %H:%M:%S",
)

file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=5 * 1024 * 1024,
    backupCount=5,
    encoding="utf-8",
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def info(msg):
    logger.info(msg)
    console.print(f"[cyan][INFO][/cyan] {msg}")


def success(msg):
    logger.info(msg)
    console.print(f"[green][SUCCESS][/green] {msg}")


def warning(msg):
    logger.warning(msg)
    console.print(f"[yellow][WARNING][/yellow] {msg}")


def error(msg):
    logger.error(msg)
    console.print(f"[red][ERROR][/red] {msg}")


def debug(msg):
    logger.debug(msg)