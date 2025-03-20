import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_dos_mas_dos(self):
        resultado = self.calc.sumar(2, 2)
        self.assertEqual(4, resultado)

    def test_caracter_en_el_primer_parametro(self):
        resultado = self.calc.sumar('X', 2)
        self.assertEqual('Solo se pueden sumar numeros', resultado)

# Pruebas para sumar
    def test_sumar_dos_mas_dos(self):
        self.assertEqual(self.calc.sumar(2, 2), 4)

    def test_sumar_tres_mas_dos(self):
        self.assertEqual(self.calc.sumar(3, 2), 5)

    def test_sumar_caracter_y_numero(self):
        self.assertEqual(self.calc.sumar('X', 2),
                         'Solo se pueden sumar numeros')

    def test_sumar_numero_y_caracter(self):
        self.assertEqual(self.calc.sumar(2, 'X'),
                         'Solo se pueden sumar numeros')

    def test_sumar_negativo_y_numero(self):
        self.assertEqual(self.calc.sumar(-2, 2),
                         'Solo se puede sumar numeros positivos y el cero')

    def test_sumar_flotante_y_numero(self):
        self.assertEqual(self.calc.sumar(4.5, 2),
                         'Solo se puede sumar numeros enteros')

    def test_sumar_cero_y_numero(self):
        self.assertEqual(self.calc.sumar(0, 5), 5)

    def test_sumar_cero_y_cero(self):
        self.assertEqual(self.calc.sumar(0, 0), 0)

    def test_sumar_grandes_numeros(self):
        self.assertEqual(self.calc.sumar(1000, 2000), 3000)

    # Pruebas para restar
    def test_restar_cinco_menos_tres(self):
        self.assertEqual(self.calc.restar(5, 3), 2)

    def test_restar_diez_menos_cero(self):
        self.assertEqual(self.calc.restar(10, 0), 10)

    def test_restar_cero_menos_cero(self):
        self.assertEqual(self.calc.restar(0, 0), 0)

    def test_restar_positivo_y_negativo(self):
        self.assertEqual(self.calc.restar(2, -2),
                         'Solo se puede restar numeros positivos y el cero')

    def test_restar_caracter_y_numero(self):
        self.assertEqual(self.calc.restar('X', 2),
                         'Solo se pueden restar numeros')

    def test_restar_flotante_y_numero(self):
        self.assertEqual(self.calc.restar(4.5, 2),
                         'Solo se puede restar numeros enteros')

    def test_restar_menor_menos_mayor(self):
        self.assertEqual(self.calc.restar(3, 5), -2)

    def test_restar_iguales(self):
        self.assertEqual(self.calc.restar(1, 1), 0)

    def test_restar_grandes_numeros(self):
        self.assertEqual(self.calc.restar(9999, 8888), 1111)

    # Pruebas para multiplicar
    def test_multiplicar_tres_por_tres(self):
        self.assertEqual(self.calc.multiplicar(3, 3), 9)

    def test_multiplicar_dos_por_cero(self):
        self.assertEqual(self.calc.multiplicar(2, 0), 0)

    def test_multiplicar_cinco_por_uno(self):
        self.assertEqual(self.calc.multiplicar(5, 1), 5)

    def test_multiplicar_negativo_y_numero(self):
        self.assertEqual(self.calc.multiplicar(-1, 2),
                         'Solo se puede multiplicar numeros positivos y el cero')

    def test_multiplicar_flotante_y_numero(self):
        self.assertEqual(self.calc.multiplicar(3.5, 2),
                         'Solo se puede multiplicar numeros enteros')

    def test_multiplicar_caracter_y_numero(self):
        self.assertEqual(self.calc.multiplicar('X', 2),
                         'Solo se pueden multiplicar numeros')

    def test_multiplicar_uno_por_mil(self):
        self.assertEqual(self.calc.multiplicar(1, 1000), 1000)

    def test_multiplicar_cien_por_cien(self):
        self.assertEqual(self.calc.multiplicar(100, 100), 10000)

    def test_multiplicar_cero_por_grande(self):
        self.assertEqual(self.calc.multiplicar(0, 999), 0)

    # Pruebas para dividir
    def test_dividir_diez_entre_dos(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_dividir_nueve_entre_tres(self):
        self.assertEqual(self.calc.dividir(9, 3), 3.0)

    def test_dividir_cinco_entre_cinco(self):
        self.assertEqual(self.calc.dividir(5, 5), 1.0)

    def test_dividir_diez_entre_cero(self):
        self.assertEqual(self.calc.dividir(10, 0),
                         'Solo se puede dividir positivos')

    def test_dividir_cero_entre_diez(self):
        self.assertEqual(self.calc.dividir(0, 10),
                         'Solo se puede dividir positivos')

    def test_dividir_caracter_y_numero(self):
        self.assertEqual(self.calc.dividir('X', 2),
                         'Solo se pueden dividir numeros')

    def test_dividir_flotante_y_numero(self):
        self.assertEqual(self.calc.dividir(3.5, 2),
                         'Solo se puede dividir numeros enteros')

    def test_dividir_uno_entre_uno(self):
        self.assertEqual(self.calc.dividir(1, 1), 1.0)

    def test_dividir_cien_entre_diez(self):
        self.assertEqual(self.calc.dividir(100, 10), 10.0)

    def test_dividir_siete_entre_dos(self):
        self.assertEqual(self.calc.dividir(7, 2), 3.5)

    def test_dividir_mil_entre_cinco(self):
        self.assertEqual(self.calc.dividir(1000, 5), 200.0)


if __name__ == '__main__':
    unittest.main()
