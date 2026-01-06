#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.parse import urlparse
import cgi

PORT = 8000
DIRECTORY = "/workspace"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_POST(self):
        if self.path == '/send-email':
            self.send_email()
        else:
            super().do_POST()
    
    def send_email(self):
        # Obtener la longitud del contenido
        content_length = int(self.headers['Content-Length'])
        # Leer el cuerpo de la solicitud
        post_data = self.rfile.read(content_length)
        # Parsear el JSON
        try:
            data = json.loads(post_data.decode('utf-8'))
        except json.JSONDecodeError:
            self.send_error(400, "JSON inválido")
            return
        
        # Extraer los datos del formulario
        name = data.get('name', '')
        email = data.get('email', '')
        subject = data.get('subject', '')
        message = data.get('message', '')
        
        # Validar que todos los campos estén presentes
        if not all([name, email, subject, message]):
            self.send_error(400, "Todos los campos son requeridos")
            return
        
        # Configurar los detalles del correo
        # Aquí debes reemplazar con tus propios detalles de correo
        sender_email = "tu_correo@gmail.com"  # Reemplaza con tu correo
        sender_password = "tu_contraseña"     # Reemplaza con tu contraseña o app password
        recipient_email = "frank.anconeyra@example.com"  # Reemplaza con tu correo de recepción
        
        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"[Contacto Web] {subject}"
        
        # Cuerpo del mensaje
        body = f"""
        Nuevo mensaje de contacto recibido:
        
        Nombre: {name}
        Email: {email}
        Asunto: {subject}
        Mensaje: {message}
        
        --
        Enviado desde el formulario de contacto de tu portafolio web.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Enviar el correo
        try:
            # Configurar el servidor SMTP (ajusta según tu proveedor de correo)
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP
            server.starttls()  # Iniciar TLS
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()
            
            # Enviar respuesta exitosa
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"message": "Correo enviado exitosamente"})
            self.wfile.write(response.encode('utf-8'))
            
        except Exception as e:
            print(f"Error al enviar correo: {str(e)}")
            self.send_error(500, f"Error al enviar el correo: {str(e)}")

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