class Hianyzasok:
    datum: int
    nev: str
    bejegyzes: str
    hianyzasok: str

    def __init__(self, sor: str) -> None:
        dátum, név, bejegyzes, hiányzások = sor.split(' ')
        self.datum = int(dátum)
        self.nev = név
        self.bejegyzes = bejegyzes
        self.hianyzasok = hiányzások
