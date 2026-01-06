# Portafolio Frank Anconeyra

## Descripción
Este es un portafolio web profesional moderno y atractivo para Frank Anconeyra, desarrollador apasionado por la tecnología y la innovación.

## Características Principales

### 🎨 Diseño Moderno
- Layout responsive que se adapta a todos los dispositivos
- Diseño limpio y profesional con colores coherentes
- Tipografía moderna (Poppins)

### ✨ Animaciones y Efectos
- Animaciones de entrada al cargar la página
- Efectos de hover en tarjetas y botones
- Animaciones al hacer scroll
- Efecto parallax en la sección hero
- Transiciones suaves entre secciones

### 📱 Responsive Design
- Totalmente adaptable a móviles, tablets y desktop
- Menú hamburguesa para dispositivos móviles
- Grid flexible que se ajusta según el tamaño de pantalla

### 🚀 Tecnologías Implementadas
- HTML5 semántico
- CSS3 avanzado con animaciones y efectos
- JavaScript moderno con funcionalidades interactivas
- Uso de CSS Grid y Flexbox
- Tipografía de Google Fonts
- Iconos de Font Awesome

## Configuración de EmailJS

Este proyecto utiliza EmailJS para enviar correos electrónicos desde el formulario de contacto. Para que funcione correctamente, debes configurar tu cuenta de EmailJS:

### 1. Servicio de Correo Electrónico
El proyecto está configurado para usar el servicio `service_u3i5vhf`. Para configurarlo:

1. Inicia sesión en tu cuenta de [EmailJS](https://www.emailjs.com/)
2. Ve a la sección de "Email Services"
3. Asegúrate de que el servicio con ID `service_u3i5vhf` esté configurado y activo
4. Si necesitas crear un nuevo servicio, sigue las instrucciones para conectar tu proveedor de correo (Gmail, Outlook, etc.)

### 2. Plantilla de Correo Electrónico
El proyecto utiliza una plantilla llamada `template_contact_form`. Esta plantilla debe contener los siguientes campos variables:
- `from_name` - Nombre del remitente
- `from_email` - Correo electrónico del remitente
- `to_name` - Nombre del destinatario
- `subject` - Asunto del correo
- `message` - Mensaje del formulario
- `reply_to` - Dirección para responder

### 3. ID de Usuario
El archivo `email.js` está configurado con un ID de usuario de EmailJS. Asegúrate de reemplazarlo con tu propio ID de usuario.

## Estructura del Sitio

### Secciones
1. **Header** - Navegación fija con efecto de transparencia
2. **Hero** - Sección principal con introducción y CTA
3. **Sobre Mí** - Información personal y habilidades
4. **Tecnologías** - Grid con tecnologías y lenguajes de programación
5. **Contacto** - Sección para contactar
6. **Footer** - Información de derechos de autor

## Archivos del Proyecto

- `index.html` - Página principal con la estructura HTML
- `nuevo_estilo.css` - Hoja de estilos con diseño moderno y animaciones
- `nuevo_script.js` - Funcionalidades JavaScript interactivas
- `email.js` - Funcionalidad para enviar correos electrónicos usando EmailJS
- `server.py` - Servidor simple para servir los archivos estáticos
- `images/` - Carpeta con imágenes del portafolio

## Funcionalidades Implementadas

### Interactividad
- Menú hamburguesa para dispositivos móviles
- Scroll suave entre secciones
- Efectos de aparición al hacer scroll
- Hover effects en botones y tarjetas
- Animaciones de carga
- Formulario de contacto funcional que envía correos electrónicos

### Formulario de Contacto
- Campo para nombre, email, asunto y mensaje
- Validación de campos requeridos
- Envío de correos electrónicos usando EmailJS
- Mensajes de confirmación y error

### Animaciones
- Efectos de entrada para elementos
- Animación de texto principal
- Efecto de flotación en imagen de perfil
- Transiciones suaves entre estados

## Personalización

Para personalizar el portafolio:

1. **Información Personal**: Modifica el contenido en `index.html`
2. **Colores**: Cambia las variables de color en `nuevo_estilo.css`
3. **Imágenes**: Reemplaza las imágenes en la carpeta `images/`
4. **Contenido**: Actualiza texto, enlaces y secciones según necesites
5. **Configuración de EmailJS**: Actualiza el ID de usuario y asegúrate de tener configurado el servicio `service_u3i5vhf`

## Compatibilidad

- Navegadores modernos (Chrome, Firefox, Safari, Edge)
- Totalmente responsive
- Optimizado para SEO

## Autor
Frank Anconeyra - Desarrollador apasionado por la tecnología y la innovación