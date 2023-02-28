class Hianyzasok:
    _honap: int
    _nap: int
    _vezetek_nev: str
    _kereszt_nev: str
    _hianyzas: str

    @property
    def hianyzas(self) -> str:
        return self._hianyzas

    @property
    def honap(self) -> int:
        return self._honap

    @property
    def nap(self) -> int:
        return self._nap

    @property
    def név(self) -> str:
        return self._vezetek_nev + self._kereszt_nev

    @property
    def aznapi_hianyzas(self) -> int:
        return self.hianyzas.count('X') + self.hianyzas.count('I')

    def __init__(self, datum: str, sor: str) -> None:
        vezeték_név, kereszt_név, hiányzás = sor.split(' ')
        self._dátum = datum
        self._vezetek_nev = vezeték_név
        self._kereszt_nev = kereszt_név
        self._hianyzas = hiányzás

        o, p = datum.split(' ')[1:]
        self._honap = int(o)
        self._nap = int(p)
