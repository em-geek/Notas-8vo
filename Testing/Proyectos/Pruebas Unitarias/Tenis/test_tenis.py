import unittest
from tenis import JuegoTenis


class TestJuegoTenis(unittest.TestCase):

    def setUp(self):
        self.juego = JuegoTenis("Jugador1", "Jugador2")

    def test_puntaje_inicial(self):
        self.assertEqual(self.juego.obtener_puntaje(), "0 - 0")

    def test_primer_punto(self):
        self.juego.anotar_punto("Jugador1")
        self.assertEqual(self.juego.obtener_puntaje(), "15 - 0")

    def test_empate(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador2")
        self.assertEqual(self.juego.obtener_puntaje(), "15 - 15")

    def test_deuce(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.assertEqual(self.juego.obtener_puntaje(), "Deuce")

    def test_ventaja(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador1")
        self.assertEqual(self.juego.obtener_puntaje(), "Ventaja Jugador1")

    def test_ventaja2(self):
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador2")
        self.assertEqual(self.juego.obtener_puntaje(), "Ventaja Jugador2")

    def test_ganador1(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.assertEqual(self.juego.obtener_puntaje(), "Gana Jugador1")

    def test_ganador2(self):
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.assertEqual(self.juego.obtener_puntaje(), "Gana Jugador2")

    def test_gana_despues_de_ventaja(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador1")  # Ventaja Jugador1
        self.juego.anotar_punto("Jugador1")  # Gana Jugador1
        self.assertEqual(self.juego.obtener_puntaje(), "Gana Jugador1")

    def test_gana_despues_de_ventaja2(self):
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador2")  # Ventaja Jugador2
        self.juego.anotar_punto("Jugador2")  # Gana Jugador2
        self.assertEqual(self.juego.obtener_puntaje(), "Gana Jugador2")

    def test_ventaja_y_deuce(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador1")  # Ventaja Jugador1
        self.juego.anotar_punto("Jugador2")  # Deuce otra vez
        self.assertEqual(self.juego.obtener_puntaje(), "Deuce")

    def test_anotar_punto_jugador_invalido(self):
        self.juego.anotar_punto("Jugador3")  # No debería afectar el puntaje
        self.assertEqual(self.juego.obtener_puntaje(), "0 - 0")

    def test_no_se_puede_seguir_jugando_despues_de_ganar(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")  # Gana Jugador1

        self.juego.anotar_punto("Jugador2")  # Intentar sumar después de ganar
        self.assertEqual(self.juego.obtener_puntaje(), "Gana Jugador1")

    def test_ganador_sin_que_el_otro_anote(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")  # Gana Jugador1
        self.assertEqual(self.juego.obtener_puntaje(), "Gana Jugador1")

    def test_partida_larga_con_muchas_ventajas(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")  # Deuce

        self.juego.anotar_punto("Jugador1")  # Ventaja Jugador1
        self.juego.anotar_punto("Jugador2")  # Deuce
        self.juego.anotar_punto("Jugador2")  # Ventaja Jugador2
        self.juego.anotar_punto("Jugador1")  # Deuce
        self.juego.anotar_punto("Jugador1")  # Ventaja Jugador1
        self.juego.anotar_punto("Jugador1")  # Gana Jugador1

        self.assertEqual(self.juego.obtener_puntaje(), "Gana Jugador1")

    def test_deuce_a_victoria(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")
        self.juego.anotar_punto("Jugador2")  # Deuce

        self.juego.anotar_punto("Jugador1")  # Ventaja Jugador1
        self.juego.anotar_punto("Jugador1")  # Gana Jugador1

        self.assertEqual(self.juego.obtener_puntaje(), "Gana Jugador1")

    def test_no_se_puede_seguir_despues_de_ganar(self):
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")
        self.juego.anotar_punto("Jugador1")  # Gana Jugador1

        self.juego.anotar_punto("Jugador2")  # No debería afectar el puntaje
        self.juego.anotar_punto("Jugador2")  # No debería afectar el puntaje

        self.assertEqual(self.juego.obtener_puntaje(), "Gana Jugador1")

    def test_puntajes_intermedios(self):
        self.juego.anotar_punto("Jugador1")
        self.assertEqual(self.juego.obtener_puntaje(), "15 - 0")

        self.juego.anotar_punto("Jugador2")
        self.assertEqual(self.juego.obtener_puntaje(), "15 - 15")

        self.juego.anotar_punto("Jugador1")
        self.assertEqual(self.juego.obtener_puntaje(), "30 - 15")

        self.juego.anotar_punto("Jugador1")
        self.assertEqual(self.juego.obtener_puntaje(), "40 - 15")

        self.juego.anotar_punto("Jugador2")
        self.assertEqual(self.juego.obtener_puntaje(), "40 - 30")


if __name__ == '__main__':
    unittest.main()
