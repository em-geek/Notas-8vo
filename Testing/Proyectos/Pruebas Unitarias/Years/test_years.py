import unittest
from years import Years


class TestYears(unittest.TestCase):

    def setUp(self):
        self.year = Years()

    def test_fecha_menor_a_1800(self):
        self.assertEqual(self.year.convertir_fecha('21/11/1780'),
                         'Fecha invalida, el año no debe ser menor a 1800.')

    def test_mes_invalido(self):
        self.assertEqual(self.year.convertir_fecha(
            '21/13/1980'), 'El mes proporcionado no existe')

    def test_dia_invalido_bisiesto(self):
        self.assertEqual(self.year.convertir_fecha(
            '29/02/2023'), 'El dia proporcionado no existe')

    def test_fecha_fuera_de_rango(self):
        self.assertEqual(self.year.convertir_fecha(
            '24/06/2025'), 'La fecha debe de estar dentro del rango desde 1800 hasta la fecha actual')

    def test_mes_con_doble_digito_extra(self):
        self.assertEqual(self.year.convertir_fecha(
            '29/022/2024'), 'El mes proporcionado no existe')

    def test_formato_invalido_texto(self):
        self.assertEqual(self.year.convertir_fecha(
            'HOLA'), 'El formato proporcionado no se detecta como una fecha DD/MM/AAAA')

    def test_formato_invalido_guiones(self):
        self.assertEqual(self.year.convertir_fecha(
            '01-02-2021'), 'El formato proporcionado no se detecta como una fecha DD/MM/AAAA')

    def test_ceros_en_fecha(self):
        self.assertEqual(self.year.convertir_fecha('00/00/0000'),
                         'Fecha invalida, el año no debe ser menor a 1800.')

    def test_caracteres_no_numericos(self):
        self.assertEqual(self.year.convertir_fecha('XX/01/2025'),
                         'El dia, mes y año debe estar escrito en numero')

    def test_cadena_vacia(self):
        self.assertEqual(self.year.convertir_fecha(
            ''), 'La entrada no debe de estar vacia')

    def test_fecha_valida_fuera_de_rango(self):
        self.assertEqual(self.year.convertir_fecha(
            '10/03/2026'), 'La fecha debe de estar dentro del rango desde 1800 hasta la fecha actual')

    def test_fecha_extremadamente_antigua(self):
        self.assertEqual(self.year.convertir_fecha('01/01/1750'),
                         'Fecha invalida, el año no debe ser menor a 1800.')

    def test_fecha_correcta_texto(self):
        self.assertEqual(self.year.convertir_fecha('21/11/1980'),
                         'Veintiuno de noviembre de mil novecientos ochenta')

    def test_fecha_bisiesto_valida(self):
        self.assertEqual(self.year.convertir_fecha('29/02/2024'),
                         'Veintinueve de febrero de dos mil veinticuatro')
        
    def test_fecha_valida_mil(self):
        self.assertEqual(self.year.convertir_fecha(
            '10/03/2000'), 'Diez de marzo de dos mil')


if __name__ == '__main__':
    unittest.main()
