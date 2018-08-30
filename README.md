[![Build Status](https://travis-ci.org/ElliotVilhelm/python-domain-validation.svg?branch=master)](https://travis-ci.org/ElliotVilhelm/python-domain-validation)
## WHOIS Client and Domain Creation Date Parser
![spam](assets/hacker.png)

This is a simple `WHOIS` domain registry client focused around parsing a domain's `Creation Date` and `Registrar` from `WHOIS` domain records.
This package is geared towards preventing fraud and abuse. The age of a domain has many applications in __abuse prevention__ and __fraud detection__.
Spammers often register on sites using newly created domains. Being able to quickly identify the age of a domain has 
numerous applications in fighting fraudulent activity. Similarly, the Registrar name of a domain can be very useful in fighting fraud by
allowing an organization to implement blacklisting functionality of known fraudulent `Registrars`.

This package maintains a list of domain extension to `WHOIS` server mappings. Using these servers and a 
rule based parsing schema this package will provide you with the domain creation date of nearly any website.

#### Background
The motivation behind this package was that many of the `WHOIS` clients available spawning child processes calling 
the [Debian WHOIS package](https://github.com/rfc1036/WHOIS). 
This is a security vulnerability when working at an enterprise level.
 Suppose a spammer decides to register with an email address such as, `elliot@;rm -rf /*` testing a domain such as 
 `rm -rf /*` with a Unix child process can allow a hacker to delete your entire system or *worse*.

By using a direct socket connection to the proper WHOIS server based on the domain extension this package is able to
achieve greater security than other available clients.  

This package does not rely on `WHOIS.iana.org` redirection as many other WHOIS packages do. 
Rather, this package maintains a direct mapping of domain extensions to servers allowing you to query for `domain creation age` through a single request.
This is a major improvement of runtime in relation to other WHOIS packages. 

#### Installation
###### Python 2.x
`pip install --index-url https://test.pypi.org/simple/ domain_validation`
###### Python 3.x
`pip3 install --index-url https://test.pypi.org/simple/ domain_validation`

![pypi](assets/pypi.svg)

#### Usage
The expected use case is for finding the creation date of a domain:
```python
from domain_validation.whois import WHOIS

whois = WHOIS("google.com")
assert str(whois.creation_date()) == "1997-09-15"
assert whois.registrar() == "MarkMonitor Inc."

whois = WHOIS("aa.中国")
assert str(whois.creation_date()) == '2013-12-29'
assert whois.registrar() == '张洪泉'

```

#### Notes
##### What makes this different from other WHOIS clients?
This engine does not rely on `WHOIS.iana.org` server redirect, rather it maintains it's own domain extension to server
mapping which makes query time faster. Furthermore, it does not rely on the the Debian WHOIS package, meaning it will not
spawn a child process and use the Debian Package like [other packages](https://code.google.com/archive/p/python-WHOIS/). 
Rather it uses a direct socket connection to the exact WHOIS server for the given domain extension making it __secure__ and __fast__.

##### Why would I use this?
Perhaps you are a small business or an enterprise organization facing fraudulent activity through spammy account sign-ups.
One signal representing the validity of an email domain is the age of the domain. This package will allow you to query for the
age of nearly any domain from and domain extension, securely and rapidly within the safety of a Python environment (no child proccess).
Furthermore, if you are using a rule based fraud system, this package provides you with `Registrar` information allowing you to maintain a
blacklist of Registrars which you have found to be fraudulent.
