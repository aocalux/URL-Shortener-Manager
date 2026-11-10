from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        # http ok reply senden (status 200)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"<h1>404 - Not Found</h1>")


def run_server(PORT, folder_path):
    server_address = ("", PORT)

    httpd = HTTPServer(server_address, Handler)

    httpd.serve_forever()