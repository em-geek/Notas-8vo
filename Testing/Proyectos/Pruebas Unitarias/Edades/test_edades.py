import unittest
from edades import edades

class TestEdades(unittest.TestCase):
    
    def test_edad_negativa(self):
        self.assertEqual(edades(-1), 'No existes')
    
    def test_edad_nino(self):
        self.assertEqual(edades(3), 'Eres niño')
    
    def test_edad_adolescente_limite_inferior(self):
        self.assertEqual(edades(13), 'Eres adolescente')
    
    def test_edad_adolescente(self):
        self.assertEqual(edades(16), 'Eres adolescente')
    
    def test_edad_adulto(self):
        self.assertEqual(edades(20), 'Eres adulto')
    
    def test_edad_adulto_mayor(self):
        self.assertEqual(edades(80), 'Eres adulto mayor')
    
    def test_edad_adulto_mayor_limite_superior(self):
        self.assertEqual(edades(100), 'Eres adulto mayor')
    
    def test_edad_mumm_raead(self):
        self.assertEqual(edades(200), 'Eres Mumm-Raead')
    
    def test_edad_caracter(self):
        self.assertEqual(edades('X'), 'Eres Chabelo')
    
    def test_edad_flotante(self):
        self.assertEqual(edades(19.2), 'Los meses no cuentan')
    
    def test_edad_cero(self):
        self.assertEqual(edades(0), 'No existes')

if __name__ == '__main__':
    unittest.main()
