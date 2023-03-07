from Hianyzasok import Hianyzasok
from Seged import Seged


class Megoldas:
    _hianyzasok: list[Hianyzasok] = []

    def hianyzasok_szama(self, nap: str, oraszam: int) -> int:
        napok: int = 0
        for sor in self._hianyzasok:
            if Seged.hetnapja(sor.honap, sor.nap) == nap and sor.hianyzas[oraszam - 1] == 'X' or sor.hianyzas[oraszam - 1] == 'I':
                napok += 1
        return napok

    @property
    def bejegyzesek_szama(self) -> int:
        return len(self._hianyzasok)

    @property
    def igazolt_hianyzas(self) -> int:
        igazolt: int = 0
        for sor in self._hianyzasok:
            for érték in sor.hianyzas:
                igazolt += érték.count('X')
        return igazolt

    @property
    def igazolatlan_hianyzas(self) -> int:
        igazolatlan: int = 0
        for sor in self._hianyzasok:
            for érték in sor.hianyzas:
                igazolatlan += érték.count('I')
        return igazolatlan

    @property
    def hianyzok(self) -> str:
        osszes_hianyzas: dict[str, int] = {}
        for sor in self._hianyzasok:
            if sor.nev not in osszes_hianyzas:
                osszes_hianyzas[sor.nev] = 0
        for sor in self._hianyzasok:
            osszes_hianyzas[sor.nev] += sor.aznapi_hianyzas
        max_ertek = max(osszes_hianyzas.values())
        vissza: str = ''
        for key, value in osszes_hianyzas.items():
            if value == max_ertek:
                vissza += f'{key},'
        return vissza[:-1]

    def _file_beolvasasa(self, állomány_neve: str) -> None:
        with open(állomány_neve, 'r', encoding='utf-8') as file:
            dátum: str = ''
            for sor in file.read().splitlines():
                if sor[0] == "#":
                    dátum = sor
                else:
                    self._hianyzasok.append(Hianyzasok(dátum, sor))

    def __init__(self, állomány_neve: str) -> None:
        self._hianyzasok = []
        self._file_beolvasasa(állomány_neve)
