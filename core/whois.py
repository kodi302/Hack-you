"""
Hack-You Professional WHOIS Lookup
Version : 2.0
"""

import whois


def lookup(domain):
    """
    Perform WHOIS lookup on a domain.
    """

    try:

        data = whois.whois(domain)

        return {
            "domain": domain,
            "registrar": str(data.registrar),
            "creation_date": str(data.creation_date),
            "expiration_date": str(data.expiration_date),
            "updated_date": str(data.updated_date),
            "name_servers": data.name_servers,
            "emails": data.emails,
            "status": data.status,
        }

    except Exception as e:

        return {
            "domain": domain,
            "error": str(e)
        }