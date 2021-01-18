from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from random import random
import os
import ssl


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _nothing(self,a,b,c):
        pass

    def do_GET(self):
        elem = None
        
        for i in range(2000):
            a = i + 3.0 * 12.0 - random()
            b = random()
            c = float(a) * b
            self._nothing(a,b,c)
            elem = c
        phrase = 'Hello world! This is our web page!!! {}'.format(elem)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str.encode(phrase))

WEBSITE_PORT = os.environ["WEBSITE_PORT"] if "WEBSITE_PORT" in os.environ else 4443

redpath = os.path.realpath('..')

httpd = ThreadingHTTPServer(('', WEBSITE_PORT), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, 
        certfile=os.path.join(redpath, "certificates\\localhost.pem"), server_side=True)
#"C:\Program Files\OpenSSL-Win64\bin\openssl.exe" req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes
httpd.serve_forever()
