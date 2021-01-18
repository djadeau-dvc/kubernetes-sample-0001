from http.client import HTTPConnection
import os
import ssl

WEBSITE_HOST = os.environ["WEBSITE_HOST"] if "WEBSITE_HOST" in os.environ else "nginx-service" 
WEBSITE_PORT = os.environ["WEBSITE_PORT"] if "WEBSITE_PORT" in os.environ else 80 

print("HTTPS client will query web server {} on tcp port {}".format(WEBSITE_HOST, WEBSITE_PORT))

i = 0
r1 = None
while i != 4999:
    i += 1
    client = HTTPConnection(host=WEBSITE_HOST,  port=WEBSITE_PORT)
    client.request("GET", "/")
    r1 = client.getresponse()
print(r1.status, r1.code)