from domain_age.whois_client import query_whois
from domain_age.creation_date import get_domain_creation_date


class WHOIS:
    def __init__(self, domain):
        self.whois_record = query_whois(domain)

    def creation_date(self):
        return get_domain_creation_date(self.whois_record)

    def registrar_name(self):
        return ""
