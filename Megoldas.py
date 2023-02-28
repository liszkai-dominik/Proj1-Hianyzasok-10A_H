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
    def hiányzók(self) -> str:
        osszes_hianyzo = {}
        for sor in self._hianyzasok:
            if sor.név not in osszes_hianyzo:
                osszes_hianyzo[sor.név] = 0
        for sor in self._hianyzasok:
            for key in osszes_hianyzo.keys():
                if sor.név == key:
                    for ertek in sor.hianyzas:
                        if ertek == 'X':
                            osszes_hianyzo[sor.név] += 1
        max_ertek = max(osszes_hianyzo.values())
        nevek = {i for i in osszes_hianyzo if osszes_hianyzo[i] == max_ertek }
        for elem in nevek:
            return elem

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
