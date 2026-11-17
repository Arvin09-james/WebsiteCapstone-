"""Serve the Lyceum of San Pedro website."""

from __future__ import annotations

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


SITE_DIRECTORY = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 5000
PUBLIC_FILES = {"/lyceum.html", "/styles.css", "/background.jpg", "/Logo.png"}


class SchoolWebsiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, directory=str(SITE_DIRECTORY), **kwargs)

    def do_GET(self) -> None:
        request_path = urlsplit(self.path).path
        if request_path == "/":
            self.path = "/lyceum.html"
        elif request_path not in PUBLIC_FILES:
            self.send_error(404, "File not found")
            return
        super().do_GET()

    def do_POST(self) -> None:
        self.send_error(404, "Endpoint not found")


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), SchoolWebsiteHandler)
    print(f"School website running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping school website.")
    finally:
        server.server_close()
