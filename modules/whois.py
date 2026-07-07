"""
Hack-You Professional WHOIS Lookup
"""

import whois


def lookup(domain):

    data = whois.whois(domain)

    return {
        "domain": domain,
        "registrar": data.registrar,
        "creation_date": str(data.creation_date),
        "expiration_date": str(data.expiration_date),
        "name_servers": data.name_servers,
        "emails": data.emails,
    }