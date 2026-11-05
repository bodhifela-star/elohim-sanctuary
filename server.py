import os
import http.server
from http.server import ThreadingHTTPServer

# Read port from cloud environment (like Render), default to 8000 locally
PORT = int(os.environ.get("PORT", 8000))

# Bind to 0.0.0.0 so external traffic and cloud platforms can access it
server_address = ("0.0.0.0", PORT)

if __name__ == "__main__":
    server = ThreadingHTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    print(f"✨ Elohim's Sanctuary server running at http://0.0.0.0:{PORT}")
    server.serve_forever()
