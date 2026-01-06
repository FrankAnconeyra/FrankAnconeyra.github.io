// email.js - Funcionalidad para manejar el envío de correos electrónicos
// Inicializar EmailJS con el ID del usuario
(function() {
    emailjs.init("user_3wR63hmY6xHg8f58A63zP"); // Reemplaza con tu ID de usuario de EmailJS
})();

// Función para enviar un correo electrónico usando EmailJS
async function sendEmail(data) {
    try {
        // Preparar los parámetros para EmailJS
        const templateParams = {
            from_name: data.name,
            from_email: data.email,
            to_name: 'Frank Anconeyra', // Receptor
            subject: data.subject,
            message: data.message,
            reply_to: data.email
        };

        // Enviar correo usando EmailJS
        const result = await emailjs.send(
            'service_u3i5vhf', // ID del servicio
            'template_contact_form', // ID de la plantilla (debe ser creado en EmailJS)
            templateParams
        );

        if (result.status === 200 || result.status === 201) {
            return { success: true, message: 'Correo enviado exitosamente' };
        } else {
            return { success: false, message: 'Error al enviar el correo' };
        }
    } catch (error) {
        console.error('Error en la conexión al enviar el correo con EmailJS:', error);
        return { success: false, message: 'Error de conexión al enviar el correo: ' + error.text || error.message };
    }
}

// Función para validar el formato de un correo electrónico
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Función para validar los campos del formulario de contacto
function validateContactForm(formData) {
    const { name, email, subject, message } = formData;
    
    const errors = [];
    
    if (!name || name.trim().length === 0) {
        errors.push('El nombre es requerido');
    }
    
    if (!email || email.trim().length === 0) {
        errors.push('El correo electrónico es requerido');
    } else if (!validateEmail(email)) {
        errors.push('El formato del correo electrónico no es válido');
    }
    
    if (!subject || subject.trim().length === 0) {
        errors.push('El asunto es requerido');
    }
    
    if (!message || message.trim().length === 0) {
        errors.push('El mensaje es requerido');
    }
    
    return {
        isValid: errors.length === 0,
        errors
    };
}

// Función para inicializar el formulario de contacto
function initializeContactForm() {
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');
    
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(contactForm);
            const data = {
                name: formData.get('name'),
                email: formData.get('email'),
                subject: formData.get('subject'),
                message: formData.get('message')
            };
            
            // Validar los datos del formulario
            const validation = validateContactForm(data);
            
            if (!validation.isValid) {
                formMessage.className = 'form-message error';
                formMessage.innerHTML = validation.errors.join('<br>');
                formMessage.style.display = 'block';
                return;
            }
            
            try {
                // Mostrar mensaje de carga
                formMessage.className = 'form-message';
                formMessage.textContent = 'Enviando mensaje...';
                formMessage.style.display = 'block';
                
                // Enviar el correo electrónico usando la función de email.js
                const result = await sendEmail(data);
                
                if (result.success) {
                    formMessage.className = 'form-message success';
                    formMessage.innerHTML = result.message + '. ¡Mensaje enviado con éxito! Te responderé pronto.';
                    contactForm.reset();
                } else {
                    formMessage.className = 'form-message error';
                    formMessage.textContent = result.message;
                }
            } catch (error) {
                formMessage.className = 'form-message error';
                formMessage.textContent = 'Error de conexión. Por favor, inténtalo de nuevo más tarde.';
            }
        });
    }
}

// Función para formatear el cuerpo del correo electrónico
function formatEmailBody(name, email, subject, message) {
    return `Nuevo mensaje de contacto recibido:

Nombre: ${name}
Email: ${email}
Asunto: ${subject}
Mensaje: ${message}

--
Enviado desde el formulario de contacto de tu portafolio web.`;
}

// Exponer las funciones para que estén disponibles globalmente si es necesario
if (typeof window !== 'undefined') {
    window.EmailService = {
        sendEmail,
        validateEmail,
        validateContactForm,
        initializeContactForm,
        formatEmailBody
    };
}

// Si se está usando en Node.js, exportar las funciones
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        sendEmail,
        validateEmail,
        validateContactForm,
        formatEmailBody
    };
}