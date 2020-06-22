import http.server
import socketserver

def mWebServerRun():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    #test
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()