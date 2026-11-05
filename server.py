import http.server
import os

PORT = 8000
DIRECTORY = "static"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

def run():
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY, exist_ok=True)
        print(f"⚠️ Warning: '{DIRECTORY}' directory was missing and has been created.")

    server_address = ("", PORT)
    httpd = http.server.ThreadingHTTPServer(server_address, CustomHandler)

    print(f"✨ Elohim's Sanctuary server running at: http://127.0.0.1:{PORT}/")
    print(f"Press Ctrl+C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server gracefully...")
        httpd.server_close()

if __name__ == "__main__":
    run()
