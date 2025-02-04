- Fallas quinquemilenarias
	- El software mas depurado y considerado de alta fiabilidad contiene defectos remanentes.
	- Edward N, Adams de IBM analizo los "tamaños" de las faltas en una BD de cobertura mundial que suponia el equivalente de miles de años de uso de un sistema informatico particular. El descubrimiento mas extraordinario consistio en que alrededor de la tercera parte de las faltas contenidas en un programa son quinquemilenarias (producirian un fallo una vez cada 5000 años)
- ¿Cuántos errores son lo "normal" por Sistema de software?
	- SEI, un programador experto introduce un defecto por cada 10 LOC, si se detectasen el 99% de los defectos introducidos (siendo optimistas) aun permanecería 1 defecto por KLOC.
	- Sistemas operativos. La tasa de defectos de Linux es 0.1 defectos/KLOC. Las distintas versiones de Unix van de 0.6 a 0.7 defectos/KLOC

Lo recomendable es que el producto software vaya siendo evaluando a medida que se va construyendo
Es necesario llevar a cabo en paralelo al proceso de desarrollo, un proceso de evaluación o comprobación de los distintos productos  o modelos que se van generando en el que participaran desarrolladores y clientes.

## TAREA
- Investigar los errores mas comunes del software
	- ### Caída de la red AT&T 1990

		de [Jose Emmanuel Sandoval Sanchez](https://moodle.ingsoftware.uaz.edu.mx/user/view.php?id=3499&course=292) - martes, 4 de febrero de 2025, 10:06
		
		Número de respuestas: 0
		
		El 15 de enero de 1990, la red de AT&T en EE.UU. sufrió una caída masiva que duró nueve horas, bloqueando 75 millones de llamadas. Inicialmente se sospechó de un ataque hacker, pero la causa real fue un error en una actualización de software.
		
		El problema se originó por una única línea de código incorrecta que provocó un reinicio en cascada de los 114 conmutadores de la red, impidiendo la gestión de llamadas. El sistema, diseñado para ser altamente fiable, usaba un mecanismo de auto-reparación que terminó colapsando debido a un fallo en su protocolo de verificación.
		
		Este incidente evidenció la importancia del aseguramiento de calidad en el desarrollo de software, destacando aspectos como la ciberseguridad y la experiencia de usuario.
- Terminar la calculadora
	- En Carpeta Proyectos
Clave de acceso a Moodle: Testing@2025