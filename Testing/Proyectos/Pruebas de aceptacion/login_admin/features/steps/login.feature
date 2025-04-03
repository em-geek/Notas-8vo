Característica: Iniciar sesíon
Como usuario del sistema de cargas académicas
deseo iniciar sesíon
para realizar mis actividades.

Escenario: Credenciales váidas
Dado que ingreso a la url:"http://10.2.224.136:8000/admin"
Y capturo el usuario: "admin" y la contraseña "admin123"
Cuando presiono el botón Identificarse
Entonces puedo ver el mensaje "BIENVENIDO, ADMIN"

Escenario: Credenciales iniciarváidas
Dado que ingreso a la url:"http://10.2.224.136:8000/admin"
Y capturo el usuario: "admins" y la contraseña "admin123"
Cuando presiono el botón Identificarse
Entonces puedo ver el mensaje de error "Por favor introduza nombre de usuario y contraseña correctos"