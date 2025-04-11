Característica: Registro de Usuarios
Como nuevo usuario
quiero registrarme proporcionando mis datos (correo, contraseña, unidad académica y área de conocimiento)
para obtener una cuenta en el sistema

Escenario: Registro exitoso con datos correctos
Dado que ingreso a la plataforma en la URL "http://127.0.0.1:8000/registro"
Y visualizo el formulario de registro
Y ingreso mi correo "nuevo.usuario@example.com"
Y ingreso una contraseña "ContrasenaSegura123"
Y confirmo la contraseña "ContrasenaSegura123"
Y selecciono la unidad académica "Unidad Académica de Ingeniería Eléctrica"
Y selecciono el área de conocimiento correspondiente
Cuando presiono el botón "Registrarse"
Entonces el sistema valida que los datos sean correctos
Y crea mi cuenta asignándome el rol de autor automáticamente
Y me redirige a la pantalla de inicio de sesión

Escenario: Registro fallido por correo ya registrado
Dado que ingreso a la plataforma en la URL "http://127.0.0.1:8000/registro"
Y visualizo el formulario de registro
Y ingreso mi correo "usuario@example.com" (ya registrado)
Cuando presiono el botón "Registrarse"
Entonces debo ver un mensaje de error "Ya existe una cuenta con ese correo"
Y permanezco en la pantalla de registro