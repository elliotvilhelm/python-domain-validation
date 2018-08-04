import socket

WHOIS_PORT = 43
WHOIS_RESPONSE_LEN_LIMIT = 10000
WHOIS_PORTION_SIZE = 100
SERVERS = {
    "ac": "whois.nic.ac",
    "ae": "whois.aeda.net.ae",
    "aero": "whois.aero",
    "af": "whois.nic.af",
    "ag": "whois.nic.ag",
    "al": "whois.ripe.net",
    "am": "whois.amnic.net",
    "as": "whois.nic.as",
    "asia": "whois.nic.asia",
    "at": "whois.nic.at",
    "au": "whois.aunic.net",
    "az": "whois.ripe.net",
    "ba": "whois.ripe.net",
    "be": "whois.dns.be",
    "bg": "whois.register.bg",
    "bi": "whois.nic.bi",
    "biz": "whois.neulevel.biz",
    "bj": "www.nic.bj",
    "br": "whois.nic.br",
    "bt": "whois.netnames.net",
    "by": "whois.ripe.net",
    "bz": "whois.belizenic.bz",
    "ca": "whois.cira.ca",
    "cat": "whois.cat",
    "cc": "whois.nic.cc",
    "cd": "whois.nic.cd",
    "ch": "whois.nic.ch ",
    "ck": "whois.nic.ck",
    "cl": "nic.cl",
    "cn": "whois.cnnic.net.cn",
    "co": "whois.nic.co",
    "co.nl": "whois.co.nl",
    "com": "whois.verisign-grs.com",
    "coop": "whois.nic.coop",
    "cx": "whois.nic.cx",
    "cy": "whois.ripe.net",
    "cz": "whois.nic.cz",
    "de": "whois.denic.de",
    "dk": "whois.dk-hostmaster.dk",
    "dm": "whois.nic.cx",
    "dz": "whois.nic.dz",
    "edu": "whois.educause.net",
    "ee": "whois.tld.ee",
    "eg": "whois.ripe.net",
    "es": "whois.ripe.net",
    "eu": "whois.eu",
    "fi": "whois.ficora.fi",
    "fo": "whois.nic.fo",
    "fr": "whois.nic.fr",
    "gb": "whois.ripe.net",
    "ge": "whois.ripe.net",
    "gl": "whois.nic.gl",
    "gm": "whois.ripe.net",
    "gov": "whois.nic.gov",
    "gr": "whois.ripe.net",
    "gs": "whois.nic.gs",
    "hk": "whois.hknic.net.hk",
    "hm": "whois.registry.hm",
    "hn": "whois2.afilias-grs.net",
    "hr": "whois.ripe.net",
    "hu": "whois.nic.hu",
    "ie": "whois.domainregistry.ie",
    "il": "whois.isoc.org.il",
    "in": "whois.inregistry.net",
    "info": "whois.afilias.info",
    "int": "whois.isi.edu",
    "iq": "vrx.net",
    "ir": "whois.nic.ir",
    "is": "whois.isnic.is",
    "it": "whois.nic.it",
    "je": "whois.je",
    "jobs": "jobswhois.verisign-grs.com",
    "jp": "whois.jprs.jp",
    "kg": "whois.domain.kg",
    "kr": "whois.nic.or.kr",
    "la": "whois2.afilias-grs.net",
    "li": "whois.nic.li",
    "lt": "whois.domreg.lt",
    "lu": "whois.restena.lu",
    "lv": "whois.nic.lv",
    "ly": "whois.lydomains.com",
    "ma": "whois.iam.net.ma",
    "mc": "whois.ripe.net",
    "md": "whois.nic.md",
    "me": "whois.nic.me",
    "mil": "whois.nic.mil",
    "mk": "whois.ripe.net",
    "mobi": "whois.dotmobiregistry.net",
    "ms": "whois.nic.ms",
    "mt": "whois.ripe.net",
    "mu": "whois.nic.mu",
    "mx": "whois.nic.mx",
    "my": "whois.mynic.net.my",
    "name": "whois.nic.name",
    "net": "whois.verisign-grs.com",
    "nf": "whois.nic.cx",
    "ng": "whois.nic.net.ng",
    "nl": "whois.domain-registry.nl",
    "no": "whois.norid.no",
    "nu": "whois.nic.nu",
    "nz": "whois.srs.net.nz",
    "org": "whois.pir.org",
    "pl": "whois.dns.pl",
    "pr": "whois.nic.pr",
    "pro": "whois.registrypro.pro",
    "pt": "whois.dns.pt",
    "ro": "whois.rotld.ro",
    "ru": "whois.ripn.ru",
    "sa": "saudinic.net.sa",
    "sb": "whois.nic.net.sb",
    "sc": "whois2.afilias-grs.net",
    "se": "whois.nic-se.se",
    "sg": "whois.nic.net.sg",
    "sh": "whois.nic.sh",
    "si": "whois.arnes.si",
    "sk": "whois.sk-nic.sk",
    "sm": "whois.nic.sm",
    "st": "whois.nic.st",
    "su": "whois.ripn.net",
    "tc": "whois.adamsnames.tc",
    "tel": "whois.nic.tel",
    "tf": "whois.nic.tf",
    "th": "whois.thnic.net",
    "tj": "whois.nic.tj",
    "tk": "whois.nic.tk",
    "tl": "whois.domains.tl",
    "tm": "whois.nic.tm",
    "tn": "whois.ripe.net",
    "to": "whois.tonic.to",
    "tp": "whois.domains.tl",
    "tr": "whois.nic.tr",
    "travel": "whois.nic.travel",
    "tw": "whois.twnic.net.tw",
    "tv": "whois.nic.tv",
    "tz": "whois.tznic.or.tz",
    "ua": "whois.ua",
    "uk": "whois.nic.uk",
    "gov.uk": "uk whois.ja.net",
    "us": "whois.nic.us",
    "uy": "nic.uy",
    "uz": "whois.cctld.uz",
    "va": "whois.ripe.net",
    "vc": "whois2.afilias-grs.net",
    "ve": "whois.nic.ve",
    "vg": "whois.adamsnames.tc",
    "ws": "www.nic.ws",
    "xxx": "whois.nic.xxx",
    "yu": "whois.ripe.net"}


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


def test_whois_com():
    print(query_whois("google.com"))


def test_whois_org():
    print(query_whois("npr.org"))


def test_whois_de():
    print(query_whois("hello.de"))


def test_whois_net():
    print(query_whois("hey.net"))


def test_whois_mx():
    print(query_whois("hey.mx"))


def test_whois_ru():
    print(query_whois("hey.ru"))


def test_whois_br():
    print(query_whois("hey.br"))


def test_whois_it():
    print(query_whois("hey.it"))


def test_whois_us():
    print(query_whois("hey.us"))


def test_whois_la():
    print(query_whois("hey.la"))


def test_whois_gq():
    print(query_whois("hey.gq"))


def test_whois_gt():
    print(query_whois("hey.gt"))

# test_whois_org()  # P
# test_whois_de()   # F
# test_whois_net()  # P
# test_whois_mx()   # P
# test_whois_ru()   # P
# test_whois_br()   # F
# test_whois_it()   # P
# test_whois_us()   # P
# test_whois_la()   # P
# test_whois_gq()   # F
# test_whois_gt()   # P
