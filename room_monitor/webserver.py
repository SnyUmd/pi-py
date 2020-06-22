import http.server
import socketserver
'''
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
#test
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
'''

server_address = ("", 8000)
handler_class = http.server.CGIHTTPRequestHandler
server = http.server.HTTPServer(server_address, handler_class)
server.serve_forever()