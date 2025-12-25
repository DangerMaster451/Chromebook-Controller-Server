from http.server import BaseHTTPRequestHandler, HTTPServer
import win32gui
import win32con
import pyautogui
import subprocess
import time

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        __focusFirefoxWindow()
        if self.path == "/togglePlayback?" or self.path == "/togglePlayback":
            pyautogui.press("playpause")

        elif self.path == "/prevTab?" or self.path == "/prevTab":
            pyautogui.hotkey("ctrl", "shift", "tab")

        elif self.path == "/nextTab?" or self.path == "/nextTab":
            pyautogui.hotkey("ctrl", "tab")

        elif self.path == "/hotkey1?" or self.path == "/hotkey1":
            pyautogui.hotkey("alt", "1")
        elif self.path == "/hotkey2?" or self.path == "/hotkey2":
            pyautogui.hotkey("alt", "2")
        elif self.path == "/hotkey3?" or self.path == "/hotkey3":
            pyautogui.hotkey("alt", "3")
        elif self.path == "/hotkey4?" or self.path == "/hotkey4":
            pyautogui.hotkey("alt", "4")
        elif self.path == "/hotkey5?" or self.path == "/hotkey5":
            pyautogui.hotkey("alt", "5")
        elif self.path == "/hotkey6?" or self.path == "/hotkey6":
            pyautogui.hotkey("alt", "6")
        elif self.path == "/hotkey7?" or self.path == "/hotkey7":
            pyautogui.hotkey("alt", "7")
        elif self.path == "/hotkey8?" or self.path == "/hotkey8":
            pyautogui.hotkey("alt", "8")

        self.send_response(200)
        self.send_header("Contest-type", "text/html")
        self.end_headers()

        with open("index.html", "rb") as file:
            contents = file.read()
            self.wfile.write(contents)

def __focusFirefoxWindow():
    def find_window():
        result = []

        def enum_handler(hwnd, _):
            if win32gui.IsWindowVisible(hwnd):
                if "Firefox" in win32gui.GetWindowText(hwnd):
                    result.append(hwnd)

        win32gui.EnumWindows(enum_handler, None)
        return result

    windows = find_window()

    if not windows:
        subprocess.Popen(["C:\\Program Files\\Mozilla Firefox\\firefox.exe"])

        # wait for Firefox window to appear
        for _ in range(20):
            time.sleep(0.5)
            windows = find_window()
            if windows:
                break

    if windows:
        hwnd = windows[0]
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)

__focusFirefoxWindow()

server = HTTPServer(("", 8000), Handler)
server.serve_forever()