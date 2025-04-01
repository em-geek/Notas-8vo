import unittest
from GestorUsuarios import GestorUsuarios

class TestRegistroUsuarios(unittest.TestCase):

    def setUp(self):
        self.registro = GestorUsuarios()

    # Prueba registro correcto de usuario
    def test_registrar_usuario_correcto(self):
        self.assertEqual(self.registro.registrar_usuario("Juan Perez", "test@correo.com", 12), 
                         "Usuario registrado: Juan Perez (test@correo.com), 12 años.")

    # Prueba registro correo existente
    def test_registrar_usuario_correo_duplicado(self):
        self.registro.registrar_usuario("Juan Perez", "test@correo.com", 12)
        with self.assertRaises(ValueError) as error: 
            self.registro.registrar_usuario("Juan Rodriguez", "test@correo.com", 20)
        self.assertEqual(str(error.exception), "El correo ya está registrado.")
        
    # Prueba registro correo erroneo
    def test_registrar_usuario_correo_erroneo(self):
        with self.assertRaises(ValueError) as error: 
            self.registro.registrar_usuario("Juan Rodriguez", "testcorreo.com", 20)
        self.assertEqual(str(error.exception), "Formato de correo inválido.")
    
    # Prueba registro edad erronea
    def test_registrar_usuario_edad_erronea(self):
        with self.assertRaises(ValueError) as error: 
            self.registro.registrar_usuario("Juan Rodriguez", "test@correo.com", -12)
        self.assertEqual(str(error.exception), "La edad debe ser un número entero positivo.")

    # Prueba cambios en usuario
    def test_actualizar_usuario(self):
        self.registro.registrar_usuario("Juan Perez", "test@correo.com", 12)
        self.assertEqual(self.registro.actualizar_usuario("test@correo.com", "Juan Jose", 51),
                          "Usuario actualizado: test@correo.com")
    
    # Prueba cambio en correo no existente
    def test_actualizacion_falla_correo(self):
        with self.assertRaises(ValueError) as error: 
            self.registro.actualizar_usuario("test@correo.com", "Juan Jose", 51)
        self.assertEqual(str(error.exception), "El usuario no existe.")

    # Prueba cambio en correo no existente
    def test_actualizacion_falla_edad(self):
        self.registro.registrar_usuario("Juan Perez", "test@correo.com", 12)
        with self.assertRaises(ValueError) as error: 
            self.registro.actualizar_usuario("test@correo.com", "Juan Jose", -12)
        self.assertEqual(str(error.exception), "La edad debe ser un número entero positivo.")

    # Prueba eliminar correo existente
    def test_eliminar_correo(self):
        self.registro.registrar_usuario("Juan Perez", "test@correo.com", 12)
        self.assertEqual(self.registro.eliminar_usuario("test@correo.com"), "Usuario eliminado: test@correo.com")
    
    # Prueba eliminar correo inexistente
    def test_eliminar_correo_no_existente(self):
        self.registro.registrar_usuario("Juan Perez", "test@correo.com", 12)
        with self.assertRaises(ValueError) as error: 
            self.registro.eliminar_usuario("tester@correo.com")
        self.assertEqual(str(error.exception), "El usuario no existe.")

    # Prueba listar usuarios
    def test_listar_correo(self):
        self.registro.registrar_usuario("Juan Perez", "test@correo.com", 12)
        self.assertEqual(self.registro.listar_usuarios(), "Correo: test@correo.com, Nombre: Juan Perez, Edad: 12")
    
    # Prueba listar usuarios inexistentes
    def test_listar_correo_inexistente(self):
        self.assertEqual(self.registro.listar_usuarios(), "No hay usuarios registrados.")
    


if __name__ == '__main__':
    unittest.main()