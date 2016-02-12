import http.server
import socketserver

PORT = 8000

print("k")
Handler = http.server.SimpleHTTPRequestHandler
print("k1")
httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
