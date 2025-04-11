Característica: Alertas de Datos Incorrectos en Login
Como usuario
quiero recibir alertas cuando ingreso datos incorrectos en el inicio de sesión
para poder corregirlos y acceder al sistema

Escenario: Alerta por datos incorrectos al iniciar sesión
Dado que ingreso a la plataforma en la URL "http://127.0.0.1:8000/login"
Y visualizo el formulario de inicio de sesión
Y ingreso mi correo "usuario@example.com"
Y ingreso una contraseña incorrecta "errorpass"
Cuando presiono el botón "Iniciar sesión"
Entonces el sistema valida las credenciales
Y muestra un mensaje "El correo o la contraseña son incorrectos"
Y permanezco en la pantalla de inicio de sesión