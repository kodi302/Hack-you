import json
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

CONFIG_FILE = ROOT_DIR / "config.json"

DEFAULT_CONFIG = {
    "app_name": "Hack-You",
    "version": "2.0.0",

    "threads": 50,
    "timeout": 5,

    "theme": "dark",
    "debug": False,

    "proxy": "",

    "user_agent": "Hack-You Scanner v2.0",

    "save_reports": True,
    "report_format": "html",

    "database": "database/hackyou.db",

    "logging": True,

    "plugins": True,

    "auto_update": True,

    "api": {
        "openai": "",
        "gemini": "",
        "claude": "",
        "virustotal": "",
        "shodan": ""
    }
}


class ConfigManager:

    def __init__(self):

        self.create()

    def create(self):

        if not CONFIG_FILE.exists():

            with open(CONFIG_FILE, "w", encoding="utf-8") as f:

                json.dump(
                    DEFAULT_CONFIG,
                    f,
                    indent=4
                )

    def load(self):

        with open(CONFIG_FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    def save(self, config):

        with open(CONFIG_FILE, "w", encoding="utf-8") as f:

            json.dump(
                config,
                f,
                indent=4
            )

    def get(self, key, default=None):

        cfg = self.load()

        return cfg.get(key, default)

    def set(self, key, value):

        cfg = self.load()

        cfg[key] = value

        self.save(cfg)


config = ConfigManager()