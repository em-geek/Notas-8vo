Característica: Login de usuarios
Como usuario registrado
quiero iniciar sesión ingresando mi correo y contraseña
para acceder al sistema

Escenario: Login con credenciales válidas
Dado que ingreso a la plataforma en la URL "http://127.0.0.1:8000/login"
Y visualizo el formulario de inicio de sesión
Y escribo mi correo "usuario@example.com"
Y escribo mi contraseña "ContrasenaSegura123"
Cuando presiono el botón "Iniciar sesión"
Entonces debo ser redirigido a la pantalla principal del sistema
Y debo ver mi nombre de usuario en la cabecera

Escenario: Login con credenciales inválidas
Dado que ingreso a la plataforma en la URL "http://127.0.0.1:8000/login"
Y visualizo el formulario de inicio de sesión
Y escribo mi correo "usuario@example.com"
Y escribo una contraseña incorrecta "12345"
Cuando presiono el botón "Iniciar sesión"
Entonces debo ver un mensaje de alerta "El correo o la contraseña son incorrectos"
Y permanezco en la pantalla de inicio de sesión

Escenario: Error en el servidor durante el login
Dado que ingreso a la plataforma en la URL "http://127.0.0.1:8000/login"
Y visualizo el formulario de inicio de sesión
Y escribo mi correo "usuario@example.com"
Y escribo mi contraseña "ContrasenaSegura123"
Cuando presiono el botón "Iniciar sesión"
Y se produce un fallo de conexión o error del servidor
Entonces debo ver un mensaje "Ocurrió un error. Intente nuevamente más tarde."
Y permanezco en la pantalla de inicio de sesión