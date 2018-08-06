# -*- coding: utf-8 -*- 
import socket
import sys
import re
from datetime import datetime
from constants import WHOIS_PORTION_SIZE, WHOIS_PORT, WHOIS_RESPONSE_LEN_LIMIT, SERVERS, SERVER_NOT_FOUND, CREATION_DATE_NOT_FOUND, MONTHS


def query_whois(domain):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = fetch_server(domain)
    if not server:
        return SERVER_NOT_FOUND
    try:
        sock.connect((server, WHOIS_PORT))
        sock.send(domain + "\r\n")
        whois_response = ''
        while len(whois_response) < WHOIS_RESPONSE_LEN_LIMIT:
            response_portion = sock.recv(WHOIS_PORTION_SIZE)
            if response_portion == '':
                break
            whois_response += response_portion
        sock.close()
    except:
        print("Failed on " + domain)
        return SERVER_NOT_FOUND
    return whois_response


def fetch_server(domain):
    domain_extension = domain.split(".")[-1]
    if domain_extension in SERVERS:
        return SERVERS[domain_extension]
    else:
        return None


def parse_date(date):
    pattern = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
    res = re.search(pattern, date, re.I)
    if res:                              # 14 Apr 2018
        day = int(date[0:2])
        month = MONTHS[date[res.start():res.start() + 3]]
        year = int(date[res.end() + 1: res.end() + 5])
    elif '/' in date and date[2] == '/':    # DD/MM/YYY
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
    elif '/' in date:                     # YYYY/MM/DD
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
    elif '-' in date and date[2] == '-':  # DD-MM-YYYY
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
    elif '-' in date:                     # YYYY-MM-DD
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
    elif '.' in date and date[2] == '.':                     # YYYY.MM.DD
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
    elif '.' in date:                     # YYYY.MM.DD
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
    else:                                 # YYYYMMDD
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
    date = datetime(year, month, day)
    return date.date()


def get_creation_date(domain):
    whois_response = query_whois(domain)
    if whois_response == SERVER_NOT_FOUND:
        return CREATION_DATE_NOT_FOUND
    pattern = r"Creation Date|created|Created On|Creation date|Created|Domain Name Commencement Date|登録年月日"
    res = re.search(pattern, whois_response, re.I)
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


if __name__ == "__main__":
    print(get_creation_date(sys.argv[1]))
