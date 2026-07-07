from core.banner import show
from core.engine import ScanEngine
from modules.network.port_scan import scan


def main():

    show()

    targets = ["scanme.nmap.org", "google.com"]

    engine = ScanEngine()

    results = engine.run(scan, targets)

    for result in results:

        print(result)


if __name__ == "__main__":
    main()
