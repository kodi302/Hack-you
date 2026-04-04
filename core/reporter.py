import os
from datetime import datetime

def generate_report(target, dns, subs, ports, dirs):
    folder = f"output/{target}"
    os.makedirs(folder, exist_ok=True)

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    path = os.path.join(folder, filename)

    with open(path, "w") as f:
        f.write(f"Target: {target}\n\n")

        f.write("DNS:\n")
        f.write(str(dns) + "\n\n")

        f.write("Subdomains:\n")
        for s in subs:
            f.write(s + "\n")

        f.write("\nPorts:\n")
        for p in ports:
            f.write(str(p) + "\n")

        f.write("\nDirectories:\n")
        for d in dirs:
            f.write(d + "\n")

    print(f"[INFO] Report saved: {path}")