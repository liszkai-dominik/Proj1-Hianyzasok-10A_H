from Hianyzasok import Hianyzasok


class Megoldas:
    hianyzasok: list[Hianyzasok] = []

    def hetnapja(self, hónap: int, nap: int) -> str:
        napok_neve = ["vasarnap", "hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat"]
        napok_száma = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
        nap_sorszam = (napok_száma[hónap - 1] + nap) % 7
        return napok_neve[nap_sorszam]

    def __init__(self, állomány_neve: str) -> None:
        self._hianyzasok = []
        with open(állomány_neve, 'r', encoding='utf-8') as file:
            dátum: str = ''
            for sor in file.read().splitlines():
                if sor[0] == "#":
                    dátum = sor
                else:
                    self.hianyzasok.append(Hianyzasok(dátum, sor))
