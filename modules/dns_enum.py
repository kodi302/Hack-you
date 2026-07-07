"""
Hack-You Professional DNS Enumerator
Version : 3.0
"""

import dns.resolver

RECORDS = [
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT",
    "CNAME",
]


def scan(domain):

    result = {
        "target": domain,
        "records": {}
    }

    for record in RECORDS:

        try:

            answers = dns.resolver.resolve(
                domain,
                record
            )

            result["records"][record] = [
                str(answer)
                for answer in answers
            ]

        except Exception:

            result["records"][record] = []

    return result