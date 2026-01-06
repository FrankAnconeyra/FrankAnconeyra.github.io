# Configuración de Envío de Correos Electrónicos

## Instrucciones para Configurar el Formulario de Contacto

Para que el formulario de contacto funcione y envíe correos electrónicos a `frank.anconeyra@tecsup.edu.pe`, debes configurar tus credenciales de correo electrónico.

### 1. Configuración Requerida en server.py

Actualiza las siguientes líneas en el archivo `/workspace/server.py`:

#### Línea 51 - Correo del remitente:
```python
sender_email = "tu_correo@gmail.com"  # Reemplaza con tu correo (por ejemplo, una cuenta de Gmail)
```

#### Línea 52 - Contraseña del correo:
```python
sender_password = "tu_contraseña"     # Reemplaza con tu contraseña o app password
```

#### Línea 53 - Correo del destinatario (ya está configurado correctamente):
```python
recipient_email = "frank.anconeyra@tecsup.edu.pe"  # Tu correo de recepción
```

### 2. Configuración de Gmail (recomendado)

Si usas una cuenta de Gmail, necesitarás:

1. Habilitar "Acceso menos seguro de apps" o preferiblemente:
2. Crear una "App Password" en tu cuenta de Google
3. Usar esa App Password en lugar de tu contraseña normal

Para crear una App Password:
1. Ve a Mi Cuenta de Google
2. Navega a Seguridad
3. En "Acceso a la cuenta de Google", selecciona "Contraseñas de aplicaciones"
4. Genera una nueva contraseña de aplicación para "Correo"
5. Usa esta contraseña en lugar de tu contraseña normal

### 3. Configuración para otros proveedores de correo

Si no usas Gmail, necesitarás ajustar:

1. El servidor SMTP (línea 79): Por ejemplo, para Outlook sería `smtp-mail.outlook.com`
2. El puerto SMTP (línea 79): Gmail usa 587 para TLS
3. Posiblemente el tipo de cifrado (línea 80): Algunos proveedores usan SSL en lugar de TLS

### 4. Importante

- El formulario de contacto enviará los mensajes a tu correo electrónico cuando alguien lo complete
- Asegúrate de probar la funcionalidad antes de publicar tu sitio
- Considera usar servicios de terceros como EmailJS para implementaciones en producción si no deseas manejar directamente el envío de correos

### 5. Iniciar el servidor

Para probar la funcionalidad:

```bash
python3 server.py
```

Luego visita `http://localhost:8000` en tu navegador.