from pathlib import Path
import os

REPORTS = Path("reports")


def menu():

    REPORTS.mkdir(exist_ok=True)

    while True:

        print("\n========== REPORTS ==========")

        files = list(REPORTS.glob("*"))

        if not files:

            print("No Reports Found")

        else:

            for i, file in enumerate(files, 1):

                print(f"{i}. {file.name}")

        print("\n0. Back")

        choice = input("Select : ")

        if choice == "0":

            break