def main() -> None:
# 1. feladat: Beolvasás
    naplo = {}
    with open('naplo.txt', 'r', encoding='utf-8') as file:
        for sor in file:
            if sor[0] == "#":
                egyNap = sor.strip().split(" ")
                egyNapKulcs = egyNap[1] + "." + egyNap[2]
                naplo[egyNapKulcs] = []
            else:
                egyHianyzo = sor.strip().split(" ")
                naplo[egyNapKulcs].append([egyHianyzo[0] + " " + egyHianyzo[1], egyHianyzo[2]])
