from Seged import Seged
from Megoldas import Megoldas


def main() -> None:
    # 1. feladat: Beolvasás
    mo: Megoldas = Megoldas('naplo.txt')
    # 2. feladat:
    print('2. feladat')
    print(f'A naplóban {mo.bejegyzesek_szama} bejegyzés van.')

    # 3. feladat
    print('3.feladat:')
    print(f'Az igazolt hiányzások száma {mo.igazolt_hianyzas}, az igazolatlanoké {mo.igazolatlan_hianyzas} óra. ')

    # 5. feladat:
    print("5. feladat")
    honap = int(input("A hónap sorszáma= "))
    nap = int(input("A nap sorszáma= "))
    print(f'Azon a napon {Seged.hetnapja(honap, nap)} volt.')

    # 6. feladat
    print("6. feladat: ")
    adott_nap: str = str(input('A nap neve='))
    adott_ora: int = int(input('Az óra sorszáma='))
    print(f'Ekkor összesen {mo.hianyzasok_szama(adott_nap, adott_ora)} óra hiányzás történt.')

    # 7. feladat:
    print('7. feladat')
    print(f'A legtöbbet hiányzó tanulók: {mo.hiányzók}')


if __name__ == "__main__":
    main()
