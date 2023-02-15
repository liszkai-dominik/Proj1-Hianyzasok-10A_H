from Megoldas import Megoldas


def main() -> None:
    mo: Megoldas = Megoldas('naplo.txt')
    print(len(mo.hianyzasok))


if __name__ == "__main__":
    main()
