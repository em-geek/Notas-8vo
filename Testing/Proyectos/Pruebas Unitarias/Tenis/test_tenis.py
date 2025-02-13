import unittest
from tenis import Tenis

class TestTenis(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_impresion_de_score(self):
        resultado = score()
        self.assertEqual('P1: 0 - P2: 0', resultado)
    
    def test_score_a_player1(self):
        self.tenis.anotar(1)
        resultado = score()
        self.assertEqual('P1: 15 - P2: 0', resultado)

    def test_score_a_player2(self):
        self.tenis.anotar(2)
        resultado = score()
        self.assertEqual('P1: 0 - P2: 15', resultado)