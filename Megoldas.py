from Hianyzasok import Hianyzasok


class Megoldas:
    hianyzasok: list[Hianyzasok] = []

    def __init__(self, állomány_neve: str) -> None:
        self._hianyzasok = []
        with open(állomány_neve, 'r', encoding='utf-8') as file:
            dátum: str = ''
            for sor in file.read().splitlines():
                if sor[0] == "#":
                    dátum = sor
                else:
                    self.hianyzasok.append(Hianyzasok(dátum, sor))
