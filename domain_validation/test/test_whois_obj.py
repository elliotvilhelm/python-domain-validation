# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from domain_validation.whois import WHOIS
from time import sleep


def test_WHOIS_com():
    sleep(.1)
    whois = WHOIS("google.com")
    assert str(whois.creation_date()) == "1997-09-15"
    assert whois.registrar() == "MarkMonitor Inc."


def test_WHOIS_com2():
    sleep(.1)
    whois = WHOIS("yahoo.com")
    assert str(whois.creation_date()) == "1995-01-18"
    assert whois.registrar() == "MarkMonitor Inc."

def test_WHOIS_org():
    sleep(.1)
    whois = WHOIS("npr.org")
    assert str(whois.creation_date()) == "1993-12-13"
    assert whois.registrar() == "Network Solutions, LLC"

def test_WHOIS_uk():
    sleep(.1)
    whois = WHOIS("wow.uk")
    assert str(whois.creation_date()) == "2014-06-11"
    assert whois.registrar() == "Planet Hippo Internet Ltd t/a EUKHOST [Tag = PLANETHIPPO]"

def test_WHOIS_com_silo():
    sleep(.1)
    whois = WHOIS("1shivom.com")
    assert str(whois.creation_date()) == "2018-07-30"
    assert whois.registrar() == "NameSilo, LLC"

def test_WHOIS_cn():
    sleep(.1)
    whois = WHOIS("yo.cn")
    assert str(whois.creation_date()) == '2003-03-17'
    assert whois.registrar() == '浙江贰贰网络有限公司'
