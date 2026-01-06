# Configuración del Formulario de Contacto

Este portafolio incluye un formulario de contacto que permite a los visitantes enviar correos electrónicos directamente al propietario del sitio.

## Configuración Requerida

Para que el formulario de contacto funcione correctamente, debes configurar los siguientes parámetros en el archivo `server.py`:

1. **Correo del remitente** (línea 51):
   ```python
   sender_email = "tu_correo@gmail.com"  # Reemplaza con tu correo
   ```

2. **Contraseña del correo** (línea 52):
   ```python
   sender_password = "tu_contraseña"     # Reemplaza con tu contraseña o app password
   ```

3. **Correo del destinatario** (línea 53):
   ```python
   recipient_email = "frank.anconeyra@example.com"  # Reemplaza con tu correo de recepción
   ```

## Configuración de Gmail (recomendado)

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

## Configuración para otros proveedores de correo

Si no usas Gmail, necesitarás ajustar:

1. El servidor SMTP (línea 79): Por ejemplo, para Outlook sería `smtp-mail.outlook.com`
2. El puerto SMTP (línea 79): Gmail usa 587 para TLS
3. Posiblemente el tipo de cifrado (línea 80): Algunos proveedores usan SSL en lugar de TLS

## Importante

- El formulario de contacto enviará los mensajes a tu correo electrónico cuando alguien lo complete
- Asegúrate de probar la funcionalidad antes de publicar tu sitio
- Considera usar servicios de terceros como EmailJS para implementaciones en producción si no deseas manejar directamente el envío de correos

## Iniciar el servidor

Para probar la funcionalidad:

```bash
python3 server.py
```

Luego visita `http://localhost:8000` en tu navegador.