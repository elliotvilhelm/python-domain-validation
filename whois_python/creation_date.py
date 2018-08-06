# -*- coding: utf-8 -*-
import re
from constants import WHOIS_PORTION_SIZE, WHOIS_PORT, WHOIS_RESPONSE_LEN_LIMIT, SERVERS, SERVER_NOT_FOUND, CREATION_DATE_NOT_FOUND, MONTHS
from whois_client import query_whois
from parse_date import parse_date


def get_creation_date(domain):
    try:
        whois_response = query_whois(domain)
        if whois_response == SERVER_NOT_FOUND:
            return CREATION_DATE_NOT_FOUND
        pattern = r"Creation Date|created|Created On|Creation date|Created|Domain Name Commencement Date|登録年月日|Registration Time|Registered on|registered"
        res = re.search(pattern, whois_response)
        if not res:
            return CREATION_DATE_NOT_FOUND
        creation_date_start = res.start()
        creation_date = whois_response[creation_date_start:creation_date_start + 50]
        date = re.search(r'\d', creation_date)
        if not date:
            return CREATION_DATE_NOT_FOUND
        start_index = date.start()
        date = creation_date[start_index:]
        return parse_date(date)
    except:
        return CREATION_DATE_NOT_FOUND
