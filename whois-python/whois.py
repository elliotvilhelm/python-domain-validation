import socket
from constants import WHOIS_PORTION_SIZE, WHOIS_PORT, WHOIS_RESPONSE_LEN_LIMIT, SERVERS


def query_whois(domain):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = fetch_server(domain)
    sock.connect((server, WHOIS_PORT))
    sock.send(domain + "\r\n")
    whois_response = ''
    while len(whois_response) < WHOIS_RESPONSE_LEN_LIMIT:
        response_portion = sock.recv(WHOIS_PORTION_SIZE)
        if response_portion == '':
            break
        whois_response += response_portion
    sock.close()
    return whois_response


def fetch_server(domain):
    return SERVERS[domain.split(".")[-1]]
