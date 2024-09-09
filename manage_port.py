import http.server
import socketserver
import urllib.parse
import subprocess

PORT = 8080  # Port for the HTTP server to listen on
HANDLER = http.server.SimpleHTTPRequestHandler

# List of IP addresses allowed to access the server
ALLOWED_IPS = ['192.168.1.204']

class CustomHandler(HANDLER):
    def do_GET(self):
        # Get the client's IP address
        client_ip = self.client_address[0]

        # Check if the client's IP address is allowed
        if client_ip not in ALLOWED_IPS:
            self.send_response(403)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"403 Forbidden: You are not allowed to access this server.")
            return

        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        action = query.get('action', [None])[0]

        if action == "open":
            result = self.manage_port(1111, "open")
        elif action == "close":
            result = self.manage_port(1111, "close")
        else:
            result = "Invalid action. Please specify 'open' or 'close'."

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(result.encode())

    def manage_port(self, port, action):
        if action == "open":
            command = f'netsh advfirewall firewall add rule name="Open Port {port}" dir=in action=allow protocol=TCP localport={port}'
        elif action == "close":
            command = f'netsh advfirewall firewall delete rule name="Open Port {port}" protocol=TCP localport={port}'
        else:
            return "Invalid action."

        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return f"Port {port} has been successfully {action}ed."
        else:
            return f"Failed to {action} port {port}. Error: {result.stderr}"

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
