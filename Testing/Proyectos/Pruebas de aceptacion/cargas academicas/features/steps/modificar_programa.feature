Característica: Modificar programa academico
Como administrador del sistema de cargas académicas
quiero modificar un programa academico
ya que es necesario cambiar algunas cosas

Escenario: Modificar programa existente
Dado ingreso a la plataforma en la url "http://127.0.0.1:8000/"
Y le doy click al menú Programas, luego click en el submenú Lista
Y presiono el boton Editar del programa "Ingenieria Perrona"
Y cambio los datos del programa con nombre "Ingenieria Magnifica" y su abreviación "IM" en la unidad academica de "Unidad Académica de Derecho"
Y presiono el boton Agregar en programas
Cuando refresco la vista
Entonces puedo ver el programa "Ingenieria Magnifica" en la lista de unidades.