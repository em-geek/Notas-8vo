import re

class GestorUsuarios:
    def __init__(self):
        ''''
         Usamos un diccionario para almacenar usuarios: clave = correo, valor = diccionario con nombre y edad
         El uso de diccionarios me va a permitir validar el correo de manera mas sencilla, ya que no tengo que aplicar
         tantas validaciones para el correo
         https://interactivechaos.com/es/manual/tutorial-de-python/diccionarios
        '''
        self.usuarios = {}
        '''
            Expresión regular para validar el formato del correo: usuario@dominio.com
            Se uso la pagina: https://regex101.com/
        '''
        self.regex_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

    def registrar_usuario(self, nombre: str, correo: str, edad: int):
        # Validación de correo duplicado
        if correo in self.usuarios:
            raise ValueError("El correo ya está registrado.")
        # Validación de formato del correo
        if not self.regex_email.match(correo):
            raise ValueError("Formato de correo inválido.")
        # Validación de edad positiva y tipo entero
        if not isinstance(edad, int) or edad <= 0:
            raise ValueError("La edad debe ser un número entero positivo.")

        # Registro del usuario
        self.usuarios[correo] = {'nombre': nombre, 'edad': edad}
        return (f"Usuario registrado: {nombre} ({correo}), {edad} años.")

    def actualizar_usuario(self, correo: str, nuevo_nombre: str = None, nueva_edad: int = None):
        # Verificar que el usuario existe
        if correo not in self.usuarios:
            raise ValueError("El usuario no existe.")

        # Actualizar el nombre si se proporciona
        if nuevo_nombre is not None:
            self.usuarios[correo]['nombre'] = nuevo_nombre

        # Actualizar la edad si se proporciona, validando que sea entero positivo
        if nueva_edad is not None:
            if not isinstance(nueva_edad, int) or nueva_edad <= 0:
                raise ValueError("La edad debe ser un número entero positivo.")
            self.usuarios[correo]['edad'] = nueva_edad

        return (f"Usuario actualizado: {correo}")

    def eliminar_usuario(self, correo: str):
        # Verificar que el usuario existe
        if correo not in self.usuarios:
            raise ValueError("El usuario no existe.")
        # Eliminar el usuario
        del self.usuarios[correo]
        return (f"Usuario eliminado: {correo}")

    def listar_usuarios(self):
        # Si no hay usuarios, informar
        if not self.usuarios:
            return ("No hay usuarios registrados.")
        else:
            for correo, info in self.usuarios.items():
                return (f"Correo: {correo}, Nombre: {info['nombre']}, Edad: {info['edad']}")
