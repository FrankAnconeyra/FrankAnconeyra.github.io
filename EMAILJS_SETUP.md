# Configuración de EmailJS

Esta guía explica cómo configurar correctamente EmailJS para que funcione con el servicio `service_u3i5vhf` en este proyecto.

## Paso 1: Crear una cuenta en EmailJS

1. Visita [https://www.emailjs.com/](https://www.emailjs.com/)
2. Haz clic en "Sign Up" para crear una cuenta gratuita
3. Verifica tu correo electrónico y completa el proceso de registro

## Paso 2: Conectar un servicio de correo electrónico

Para usar el servicio `service_u3i5vhf`, necesitas conectar un proveedor de correo electrónico:

1. Inicia sesión en tu cuenta de EmailJS
2. Ve a la sección "Email Services"
3. Haz clic en "Add New Service"
4. Selecciona tu proveedor de correo (Gmail, Outlook, etc.)
5. Sigue las instrucciones para autenticar tu cuenta de correo

## Paso 3: Crear la plantilla `template_contact_form`

El código JavaScript espera una plantilla con ID `template_contact_form`. Para crearla:

1. Ve a la sección "Email Templates"
2. Haz clic en "Create New Template"
3. Establece el ID como `template_contact_form`
4. Configura los campos variables como se indica a continuación:

### Campos Variables Disponibles:

- `from_name` - Nombre del remitente (del formulario de contacto)
- `from_email` - Correo electrónico del remitente
- `to_name` - Nombre del destinatario (en este caso, "Frank Anconeyra")
- `subject` - Asunto del mensaje
- `message` - Contenido del mensaje
- `reply_to` - Dirección de correo para responder

### Ejemplo de Plantilla:

**Asunto:**
```
[Contacto Web] {{subject}}
```

**Cuerpo (HTML):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mensaje de Contacto</title>
</head>
<body>
    <h2>Nuevo mensaje de contacto recibido</h2>
    <p><strong>De:</strong> {{from_name}} ({{from_email}})</p>
    <p><strong>Asunto:</strong> {{subject}}</p>
    <p><strong>Mensaje:</strong></p>
    <p>{{message}}</p>
    <hr>
    <p>Enviado desde el formulario de contacto del portafolio web.</p>
</body>
</html>
```

## Paso 4: Obtener tu ID de usuario

1. Ve a la sección "Account" o "Dashboard"
2. Copia tu "User ID"
3. Reemplaza el valor en la línea de inicialización en `email.js`:
   ```javascript
   emailjs.init("TU_USER_ID_AQUI");
   ```

## Paso 5: Probar la configuración

Después de completar todos los pasos:

1. Asegúrate de que el servicio tenga el ID `service_u3i5vhf`
2. Verifica que la plantilla se llame `template_contact_form`
3. Confirma que tu User ID esté correctamente configurado
4. Prueba el formulario de contacto en tu sitio web

## Solución de Problemas

### Error: "Service not found"
- Verifica que el ID del servicio en `email.js` coincida exactamente con el servicio configurado en EmailJS

### Error: "Template not found"
- Asegúrate de que la plantilla `template_contact_form` exista y esté activa

### Error: "Access denied"
- Verifica que tu cuenta de EmailJS esté verificada
- Confirma que tu proveedor de correo esté correctamente conectado