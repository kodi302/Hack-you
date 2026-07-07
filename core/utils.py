import socket
import validators


def is_ip(ip):

    try:

        socket.inet_aton(ip)

        return True

    except:

        return False


def is_domain(domain):

    return validators.domain(domain)
