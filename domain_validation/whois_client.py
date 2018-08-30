# -*- coding: utf-8 -*- 
import socket
from domain_validation.constants import WHOIS_PORTION_SIZE, WHOIS_PORT, WHOIS_RESPONSE_LEN_LIMIT, SERVERS, SERVER_NOT_FOUND


def query_whois(domain):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server = fetch_server(domain)
        if not server:
            return SERVER_NOT_FOUND
        sock.connect((server, WHOIS_PORT))
        sock.send((domain + "\r\n").encode('utf-8'))
        whois_response = ''
        while len(whois_response) < WHOIS_RESPONSE_LEN_LIMIT:
            response_portion = sock.recv(WHOIS_PORTION_SIZE).decode('utf-8')
            if response_portion == '':
                break
            whois_response += response_portion
        sock.close()
    except Exception as e:
        print(e)
        return SERVER_NOT_FOUND
    return whois_response


def fetch_server(domain):
    domain_extension = domain.split(".")[-1]
    if domain_extension in SERVERS:
        return SERVERS[domain_extension]
    else:
        return None

