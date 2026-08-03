"""
Hack-You Port Parser
"""

def parse_ports(text):

    ports = []

    text = text.replace(" ", "")

    for part in text.split(","):

        if "-" in part:

            start, end = part.split("-")

            ports.extend(
                range(
                    int(start),
                    int(end) + 1
                )
            )

        else:

            ports.append(int(part))

    return sorted(list(set(ports)))