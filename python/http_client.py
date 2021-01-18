from http.client import HTTPSConnection
import os
import ssl

WEBSITE_HOST = os.environ["WEBSITE_HOST"] if "WEBSITE_HOST" in os.environ else "localhost" 
WEBSITE_PORT = os.environ["WEBSITE_PORT"] if "WEBSITE_PORT" in os.environ else 4443 

print("HTTPS client will query web server {} on tcp port {}".format(WEBSITE_HOST, WEBSITE_PORT))

ssl._create_default_https_context = ssl._create_unverified_context

i = 0
r1 = None

while i != 4999:
    i += 1
    client = HTTPSConnection(host=WEBSITE_HOST, 
        check_hostname=False, port=WEBSITE_PORT)
    client.request("GET", "/")
    r1 = client.getresponse()
print(r1.status, r1.code)