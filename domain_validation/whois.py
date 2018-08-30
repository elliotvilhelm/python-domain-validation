from domain_validation.whois_client import query_whois
from domain_validation.creation_date import get_domain_creation_date
from domain_validation.registrar import get_registrar


class WHOIS:
    def __init__(self, domain):
        self.whois_record = query_whois(domain)

    def creation_date(self):
        return get_domain_creation_date(self.whois_record)

    def registrar(self):
        return get_registrar(self.whois_record)
