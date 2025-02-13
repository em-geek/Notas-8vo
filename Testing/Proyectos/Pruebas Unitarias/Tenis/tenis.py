
class JuegoTenis:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.puntajes = {jugador1: 0, jugador2: 0}
        self.nombres_puntajes = ["0", "15", "30", "40"]

    def obtener_puntaje(self):
        puntaje1 = self.puntajes[self.jugador1]
        puntaje2 = self.puntajes[self.jugador2]

        if puntaje1 >= 3 and puntaje2 >= 3:
            if puntaje1 == puntaje2:
                return "Deuce"
            elif puntaje1 == puntaje2 + 1:
                return f"Ventaja {self.jugador1}"
            elif puntaje2 == puntaje1 + 1:
                return f"Ventaja {self.jugador2}"
            elif puntaje1 >= puntaje2 + 2:
                return f"Gana {self.jugador1}"
            elif puntaje2 >= puntaje1 + 2:
                return f"Gana {self.jugador2}"

        if puntaje1 >= 4:
            return f"Gana {self.jugador1}"
        if puntaje2 >= 4:
            return f"Gana {self.jugador2}"

        return f"{self.nombres_puntajes[puntaje1]} - {self.nombres_puntajes[puntaje2]}"

    def anotar_punto(self, jugador):
        if jugador in self.puntajes:
            self.puntajes[jugador] += 1