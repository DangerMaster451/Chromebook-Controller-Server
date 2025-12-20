from http.server import BaseHTTPRequestHandler, HTTPServer
import pyautogui

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/togglePlayback?":
            pyautogui.press("playpause")

        elif self.path == "/prevTab?":
            pyautogui.hotkey("ctrl", "shift", "tab")

        elif self.path == "/nextTab?":
            pyautogui.hotkey("ctrl", "tab")

        self.send_response(200)
        self.send_header("Contest-type", "text/html")
        self.end_headers()

        with open("index.html", "rb") as file:
            contents = file.read()
            self.wfile.write(contents)

server = HTTPServer(("", 8000), Handler)
server.serve_forever()