class Hianyzasok:
    _dátum: str
    _v_név: str
    _k_név: str
    _hiányzás: str

    def __init__(self, sor: str) -> None:
        dátum, v_név, k_név, hiányzás = sor.split(';')
        self._dátum = dátum
        self._v_név = v_név
        self._k_név = k_név
        self._hiányzás = hiányzás