from http.server import BaseHTTPRequestHandler, HTTPServer
import win32gui
import win32con
import pyautogui
import subprocess
import time

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        focusFirefoxWindow()
        if self.path == "/":
            path = "index.html"
        elif self.path == "/togglePlayback?" or self.path == "/togglePlayback":
            pyautogui.press("playpause")
            path = "index.html"
        elif self.path == "/prevTab?" or self.path == "/prevTab":
            pyautogui.hotkey("ctrl", "shift", "tab")
            path = "index.html"
        elif self.path == "/nextTab?" or self.path == "/nextTab":
            pyautogui.hotkey("ctrl", "tab")
            path = "index.html"
        elif self.path == "/hotkey1?" or self.path == "/hotkey1":
            pyautogui.hotkey("ctrl", "t")
            path = "index.html"
            pyautogui.hotkey("alt", "1")
        elif self.path == "/hotkey2?" or self.path == "/hotkey2":
            path = "index.html"
            pyautogui.hotkey("ctrl", "t")
            pyautogui.hotkey("alt", "2")
        elif self.path == "/hotkey3?" or self.path == "/hotkey3":
            path = "index.html"
            pyautogui.hotkey("ctrl", "t")
            pyautogui.hotkey("alt", "3")
        elif self.path == "/hotkey4?" or self.path == "/hotkey4":
            path = "index.html"
            pyautogui.hotkey("ctrl", "t")
            pyautogui.hotkey("alt", "4")
        elif self.path == "/hotkey5?" or self.path == "/hotkey5":
            path = "index.html"
            pyautogui.hotkey("ctrl", "t")
            pyautogui.hotkey("alt", "5")
        elif self.path == "/hotkey6?" or self.path == "/hotkey6":
            path = "index.html"
            pyautogui.hotkey("ctrl", "t")
            pyautogui.hotkey("alt", "6")
        elif self.path == "/hotkey7?" or self.path == "/hotkey7":
            path = "index.html"
            pyautogui.hotkey("ctrl", "t")
            pyautogui.hotkey("alt", "7")
        elif self.path == "/hotkey8?" or self.path == "/hotkey8":
            path = "index.html"
            pyautogui.hotkey("ctrl", "t")
            pyautogui.hotkey("alt", "8")
        else:
            path = self.path.lstrip("/")

        self.send_response(200)
        self.send_header("Contest-type", "text/html")
        self.end_headers()

        with open(path, "rb") as file:
            contents = file.read()
            self.wfile.write(contents)

def focusFirefoxWindow():
    FIREFOX_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"

    def find_firefox_windows():
        result = []

        def enum_handler(hwnd, _):
            if win32gui.IsWindowVisible(hwnd):
                if win32gui.GetClassName(hwnd) == "MozillaWindowClass":
                    result.append(hwnd)

        win32gui.EnumWindows(enum_handler, None)
        return result

    windows = find_firefox_windows()

    if not windows:
        subprocess.Popen([FIREFOX_PATH])
        for _ in range(20):
            time.sleep(0.5)
            windows = find_firefox_windows()
            if windows:
                break

    if windows:
        hwnd = windows[0]
        if win32gui.GetForegroundWindow() == hwnd:
            placement = win32gui.GetWindowPlacement(hwnd)
            if placement[1] == win32con.SW_SHOWMAXIMIZED:
                return

        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

focusFirefoxWindow()

server = HTTPServer(("", 8000), Handler)
server.serve_forever()
