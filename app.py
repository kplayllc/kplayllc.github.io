"""Local preview server for the Kplay LLC homepage.

Run with Python / PyCharm: python app.py
This is a static website; no Python server is needed on GitHub Pages.
"""

import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


SITE_DIRECTORY = Path(__file__).resolve().parent


def main() -> None:
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8000"))
    handler = partial(SimpleHTTPRequestHandler, directory=str(SITE_DIRECTORY))
    server = ThreadingHTTPServer((host, port), handler)
    print(f"Kplay homepage running at http://{host}:{port}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
