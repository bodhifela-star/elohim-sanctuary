import os
import http.server
from http.server import ThreadingHTTPServer

PORT = int(os.environ.get("PORT", 8000))
server_address = ("0.0.0.0", PORT)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # If visiting the root or main page, redirect to the static folder
        if path == "/" or path == "":
            path = "/static/index.html"
        else:
            # Check if the requested file is inside static/
            static_path = os.path.join("static", path.lstrip("/"))
            if os.path.exists(static_path):
                path = f"/static/{path.lstrip('/')}"
        return super().translate_path(path)

if __name__ == "__main__":
    server = ThreadingHTTPServer(server_address, CustomHandler)
    print(f"✨ Elohim's Sanctuary server running on port {PORT}")
    server.serve_forever()
