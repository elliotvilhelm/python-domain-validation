### Whois Client and Parser
This is a simple client that is only focused on parsing creation date. The motivation for writing this was that many of the whois clients available were spawning child processes calling the debian
whois package. This is a security vulnerability when working at an enterprise level, e.g. testing a domain such as `rm -rf /*`. It is much safer to directly connect through a socket.

#### Installation
`pip install --index-url https://test.pypi.org/simple/ whois_python`

#### Usage
The expected use case is for finding the creation date of a domain:
```
from whois_python.creation_date import get_creation_date
get_creation_date("google.com")
```
Output: `datetime.date(1997, 9, 15)`


#### Notes
What makes this different than the other whois clients availible?
This engine does not rely on whois.iana.org server redirect, rather it maintains it's own domain extension to server
mapping which makes query time faster. Also it does not rely on the the debian whois package, it uses a direct socket
connection making it more secure for enterprise usage.
