import os
from datetime import datetime

def generate_report(target, ports):
    os.makedirs("output", exist_ok=True)

    filename = f"output/{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write(f"Target: {target}\n\n")
        f.write("Open Ports:\n")

        for port in ports:
            f.write(f"- {port}\n")

    print(f"[INFO] Report saved: {filename}")