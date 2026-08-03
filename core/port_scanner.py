"""
Hack-You Professional Port Scanner Wrapper
Version : 3.1
"""

from modules.network.port_scan import scan
from core.banner_grabber import grab_banner


def run_port_scan(target, mode="fast", custom_ports=None):
    """
    mode:
        fast   -> Common Ports
        full   -> 1-65535
        custom -> User Ports
    """

    if mode == "fast":

        result = scan(target)

    elif mode == "full":

        result = scan(
            target,
            ports=range(1, 65536)
        )

    elif mode == "custom":

        result = scan(
            target,
            ports=custom_ports
        )

    else:

        result = scan(target)

    ports = result.get("ports", [])

    for item in ports:

        try:

            item["banner"] = grab_banner(
                target,
                item["port"]
            )

        except Exception:

            item["banner"] = "Unknown"

    return ports