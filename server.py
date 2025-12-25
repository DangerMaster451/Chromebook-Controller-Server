from http.server import BaseHTTPRequestHandler, HTTPServer
import pyautogui

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/togglePlayback?" or self.path == "/togglePlayback":
            pyautogui.press("playpause")

        elif self.path == "/prevTab?" or self.path == "/prevTab":
            pyautogui.hotkey("ctrl", "shift", "tab")

        elif self.path == "/nextTab?" or self.path == "/nextTab":
            pyautogui.hotkey("ctrl", "tab")

        elif self.path == "/hotkey1?" or self.path == "/hotkey1":
            pyautogui.hotkey("ctrl", "k")
            pyautogui.typewrite("https://youtube.com\n")


        self.send_response(200)
        self.send_header("Contest-type", "text/html")
        self.end_headers()

        with open("index.html", "rb") as file:
            contents = file.read()
            self.wfile.write(contents)

server = HTTPServer(("", 8000), Handler)
server.serve_forever()