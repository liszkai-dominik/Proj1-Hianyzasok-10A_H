from unittest import TestCase
from Megoldas import Megoldas
from Seged import Seged


class TestMegoldas(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mo1: Megoldas = Megoldas('naplo.txt')
        cls.mo2: Seged = Seged()

    def test_bejegyzesek_szama(self) -> None:
        self.assertEqual(self.mo1.bejegyzesek_szama, 139)

    def test_igazolt_hianyzas(self) -> None:
        self.assertEqual(self.mo1.igazolt_hianyzas, 788)

    def test_igazolatlan_hianyzas(self) -> None:
        self.assertEqual(self.mo1.igazolatlan_hianyzas, 18)

    def test_hetnapja(self) -> None:
        self.assertEqual(self.mo2.hetnapja(1, 15), 'hétfő')
        self.assertEqual(self.mo2.hetnapja(2, 6), 'kedd')
        self.assertEqual(self.mo2.hetnapja(2, 23), 'péntek')
        self.assertEqual(self.mo2.hetnapja(2, 5), 'hétfő')
        self.assertEqual(self.mo2.hetnapja(5, 18), 'péntek')

    def test_hianyzasok_szama(self) -> None:
        self.assertEqual(self.mo1.hianyzasok_szama('szerda', 3), 49)
        self.assertEqual(self.mo1.hianyzasok_szama('hétfő', 5), 14)
        self.assertEqual(self.mo1.hianyzasok_szama('kedd', 2), 23)
        self.assertEqual(self.mo1.hianyzasok_szama('péntek', 7), 2)
        self.assertEqual(self.mo1.hianyzasok_szama('csütörtök', 1), 23)

    def test_hianyzok(self) -> None:
        self.assertEqual(self.mo1.hianyzok, 'KiviAdrienn,JujubaIbolya')
