from Megoldas import Megoldas


def main() -> None:
    # 1. feladat: Beolvasás
    mo: Megoldas = Megoldas('naplo.txt')
    # 2. feladat:
    print('2. feladat')
    print(f'A naplóban {len(mo.hianyzasok)} bejegyzés van.')


    # 3. feladat
    print('3.feladat:')
    print(f'Az igazolt hiányzások száma {mo.igazolt_hianyzas}, az igazolatlanoké {mo.igazolatlan_hianyzas} óra. ')

    # 5. feladat:
    print("5. feladat")
    honap = int(input("A hónap sorszáma= "))
    nap = int(input("A nap sorszáma= "))
    print(f'Azon a napon {mo.hetnapja(honap, nap)} volt.')


if __name__ == "__main__":
    main()
