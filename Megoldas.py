from Hianyzasok import Hianyzasok


class Megoldas:
    hianyzasok: list[Hianyzasok] = []

    @property
    def igazolt_hianyzas(self) -> int:
        igazolt: int = 0
        for sor in self.hianyzasok:
            for érték in sor.hianyzas:
                igazolt += érték.count('X')
        return igazolt

    @property
    def igazolatlan_hianyzas(self) -> int:
        igazolatlan: int = 0
        for sor in self.hianyzasok:
            for érték in sor.hianyzas:
                igazolatlan += érték.count('I')
        return igazolatlan

    def hetnapja(self, hónap: int, nap: int) -> str:
        napok_neve = ["vasarnap", "hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat"]
        napok_száma = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
        nap_sorszam = (napok_száma[hónap - 1] + nap) % 7
        return napok_neve[nap_sorszam]

    def hianyzasok_szama(self, nap: str, oraszam: int) -> int:
        napok: int = 0
        for sor in self.hianyzasok:
            if self.hetnapja(sor.honap, sor.nap) == nap and sor.hianyzas[oraszam - 1] == 'X' or sor.hianyzas[oraszam - 1] == 'I':
                napok += 1
        return napok

    def __init__(self, állomány_neve: str) -> None:
        self._hianyzasok = []
        with open(állomány_neve, 'r', encoding='utf-8') as file:
            dátum: str = ''
            for sor in file.read().splitlines():
                if sor[0] == "#":
                    dátum = sor
                else:
                    self.hianyzasok.append(Hianyzasok(dátum, sor))
