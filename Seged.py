class Seged:
    @staticmethod
    def hetnapja(hónap: int, nap: int) -> str:
        napok_neve = ["vasarnap", "hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat"]
        napok_száma = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
        nap_sorszam = (napok_száma[hónap - 1] + nap) % 7
        return napok_neve[nap_sorszam]
