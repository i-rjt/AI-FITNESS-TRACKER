import socketserver
import http.server
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware



PORT=5555
Handler=http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT),Handler) as httpd:
    print(f"server started successfully")
    httpd.serve_forever()


