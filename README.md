### Whois Client and Parser
This is a simple Whois domain registry client that is only focused on parsing domain creation date. The age of a domain can have many applications in abuse prevention and fraud detection. 
The motivation for writing this was that many of the whois clients available were spawning child processes calling the debian whois package. 
This is a security vulnerability when working at an enterprise level, e.g. testing a domain such as `rm -rf /*` with a unix child proccess can allow a spammer to delete your entire system. 
By using a direct socket connection to the proper whois server based on the domain extension this package is able to
achieve greater security than other availible clients. 

#### Installation
###### Python 2.x
`pip install --index-url https://test.pypi.org/simple/ whois_python`
###### Python 3.x
`pip3 install --index-url https://test.pypi.org/simple/ whois_python`

#### Usage
The expected use case is for finding the creation date of a domain:
```
from whois_python.creation_date import get_creation_date
get_creation_date("google.com")
```
Output: `datetime.date(1997, 9, 15)`


#### Notes
##### What makes this different than the other whois clients availible?
This engine does not rely on whois.iana.org server redirect, rather it maintains it's own domain extension to server
mapping which makes query time faster. Also it does not rely on the the debian whois package, it uses a direct socket
connection making it more secure for enterprise usage.
