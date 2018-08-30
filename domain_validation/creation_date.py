# -*- coding: utf-8 -*-
import re
from domain_validation.constants import SERVER_NOT_FOUND, CREATION_DATE_NOT_FOUND
from domain_validation.parse_date import parse_date


def get_domain_creation_date(whois_record):
    try:
        if whois_record == SERVER_NOT_FOUND:
            return CREATION_DATE_NOT_FOUND
        pattern = r"Creation Date|created|Created On|Creation date|Created|Domain Name Commencement Date|登録年月日|Registration Time|Registered on|registered"
        res = re.search(pattern, whois_record)
        if not res:
            return CREATION_DATE_NOT_FOUND
        creation_date_start = res.start()
        creation_date = whois_record[creation_date_start:creation_date_start + 50]
        date = re.search(r'\d', creation_date)
        if not date:
            return CREATION_DATE_NOT_FOUND
        start_index = date.start()
        date = creation_date[start_index:]
        return parse_date(date)
    except Exception as e:
        print(e)
        return CREATION_DATE_NOT_FOUND

