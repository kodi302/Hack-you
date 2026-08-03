"""
Hack-You Settings
"""

import json
from pathlib import Path

CONFIG = Path("config.json")

DEFAULT = {
    "threads": 100,
    "timeout": 1,
    "theme": "default"
}


def load():

    if not CONFIG.exists():

        save(DEFAULT)

        return DEFAULT

    with open(CONFIG, "r") as f:

        return json.load(f)


def save(data):

    with open(CONFIG, "w") as f:

        json.dump(data, f, indent=4)


def menu():

    settings = load()

    while True:

        print("\n========== SETTINGS ==========")

        print(f"1. Threads : {settings['threads']}")
        print(f"2. Timeout : {settings['timeout']}")
        print(f"3. Theme   : {settings['theme']}")
        print("0. Back")

        choice = input("\nSelect : ")

        if choice == "1":

            settings["threads"] = int(
                input("Threads : ")
            )

        elif choice == "2":

            settings["timeout"] = float(
                input("Timeout : ")
            )

        elif choice == "3":

            settings["theme"] = input(
                "Theme : "
            )

        elif choice == "0":

            save(settings)

            break

    save(settings)