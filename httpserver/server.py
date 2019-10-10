import http.server
import socketserver
import sys

logfile = open("server.log", "a+")

PORT = 8000

class myHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
      self.send_response(200)

    def log_message(self, format, *args):
        msg = "%s - - [%s] %s\n" % (self.address_string(),
                          self.log_date_time_string(),
                          format%args)
        logfile.write(msg)
        logfile.flush()
        sys.stdout.write(msg)

Handler = myHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

