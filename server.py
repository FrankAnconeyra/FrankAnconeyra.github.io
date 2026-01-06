#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
import json
from urllib.parse import urlparse

PORT = 8000
DIRECTORY = "/workspace"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_POST(self):
        if self.path == '/send-email':
            # Ahora que usamos EmailJS, este endpoint simplemente devuelve un mensaje
            # indicando que se debe usar EmailJS en lugar del backend
            self.send_response(405)  # Método no permitido
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({
                "error": "El envío de correo electrónico ahora se maneja a través de EmailJS en el cliente. Este endpoint ya no está en uso."
            })
            self.wfile.write(response.encode('utf-8'))
        else:
            super().do_POST()
    
    def end_headers(self):
        # Agregar encabezados CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    

def start_server():
    print(f"Sirviendo en el directorio: {DIRECTORY}")
    print(f"Abre tu navegador en: http://localhost:{PORT}")
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Servidor iniciado en el puerto {PORT}")
        print("Presiona Ctrl+C para detener el servidor")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")

if __name__ == "__main__":
    start_server()