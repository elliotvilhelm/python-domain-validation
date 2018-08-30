from domain_age.whois import WHOIS


def test_WHOIS():
    whois = WHOIS("google.com")
    print(whois.creation_date())

test_WHOIS()