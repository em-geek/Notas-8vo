Característica: Agregar programa academico
Como administrador del sistema de cargas académicas
quiero agregar un programa academico
para agregarlo a las unidades

Escenario: Datos correctos
Dado ingreso a la plataforma en la url "http://127.0.0.1:8000/"
Y le doy click al menú Programas, luego click en el submenú Nuevo
Y registró el programa "Ingenieria Perrona" y su abreviación "IP" en la unidad academica de "Unidad Académica de Ingeniería Eléctrica"
Cuando presiono el boton Agregar en programas
Entonces puedo ver el programa "Ingenieria Perrona" en la lista de unidades.