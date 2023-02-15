from Hianyzasok import Hianyzasok


class Megoldas:
    hianyzasok: list[Hianyzasok] = []

    def __init__(self, állomány_neve: str) -> None:
        self._hianyzasok = []
        with open(állomány_neve, 'r', encoding='utf-8') as file:
            for értékek in file.read().splitlines():
                if értékek[0] == "#":
                    h_n = értékek.strip().split(" ")
                    dátum = h_n[1] + "." + h_n[2]
                else:
                    while értékek[0] != "#":
                        sor: str = ""
                        hiányzó = értékek.strip().split(" ")
                        teljes_név = hiányzó[0] + ";" + hiányzó[1]
                        hiányzás = hiányzó[2]
                        sor: str = dátum + ";" + teljes_név + ";" + hiányzás
                        self.hianyzasok.append(Hianyzasok(sor))
        