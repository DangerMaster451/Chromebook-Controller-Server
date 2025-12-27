from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            path = "index.html"
        else:
            path = self.path.lstrip("/")

        self.send_response(200)
        self.send_header("Content-type", "text.html")
        self.end_headers()

        with open(path, "rb") as file:
            self.wfile.write(file.read())
# Run server
server = HTTPServer(("", 8000), Handler)
server.serve_forever()