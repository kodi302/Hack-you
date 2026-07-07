import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080, 3389]


def scan(target):

    result = []

    for port in COMMON_PORTS:

        sock = socket.socket()

        sock.settimeout(0.5)

        try:

            sock.connect((target, port))

            result.append(port)

        except:

            pass

        sock.close()

    return {"target": target, "ports": result}
