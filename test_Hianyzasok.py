from unittest import TestCase
from Hianyzasok import Hianyzasok


class TestHianyzasok(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hianyzas1: Hianyzasok = Hianyzasok(datum='# 01 15', sor='Galagonya Alfonz OXXXXXX')
        cls.hianyzas2: Hianyzasok = Hianyzasok(datum='# 02 06', sor='Naspolya Frigyes XXXXXXX')
        cls.hianyzas3: Hianyzasok = Hianyzasok(datum='# 02 23', sor='Eper Lehel XXXXXXN')
        cls.hianyzas4: Hianyzasok = Hianyzasok(datum='# 02 05', sor='Jujuba Ibolya IIXXXXX')
        cls.hianyzas5: Hianyzasok = Hianyzasok(datum='# 05 18', sor='Citrom Lajos XXXXXXN')

    def test_nev(self) -> None:
        self.assertEqual(self.hianyzas1.nev, 'GalagonyaAlfonz')
        self.assertEqual(self.hianyzas2.nev, 'NaspolyaFrigyes')
        self.assertEqual(self.hianyzas3.nev, 'EperLehel')
        self.assertEqual(self.hianyzas4.nev, 'JujubaIbolya')
        self.assertEqual(self.hianyzas5.nev, 'CitromLajos')

    def test_hianyzas(self) -> None:
        self.assertEqual(self.hianyzas1.hianyzas, 'OXXXXXX')
        self.assertEqual(self.hianyzas2.hianyzas, 'XXXXXXX')
        self.assertEqual(self.hianyzas3.hianyzas, 'XXXXXXN')
        self.assertEqual(self.hianyzas4.hianyzas, 'IIXXXXX')
        self.assertEqual(self.hianyzas5.hianyzas, 'XXXXXXN')

    def test_nap(self) -> None:
        self.assertEqual(self.hianyzas1.nap, 15)
        self.assertEqual(self.hianyzas2.nap, 6)
        self.assertEqual(self.hianyzas3.nap, 23)
        self.assertEqual(self.hianyzas4.nap, 5)
        self.assertEqual(self.hianyzas5.nap, 18)

    def test_honap(self) -> None:
        self.assertEqual(self.hianyzas1.honap, 1)
        self.assertEqual(self.hianyzas2.honap, 2)
        self.assertEqual(self.hianyzas3.honap, 2)
        self.assertEqual(self.hianyzas4.honap, 2)
        self.assertEqual(self.hianyzas5.honap, 5)

    def test_datum(self) -> None:
        self.assertEqual(self.hianyzas1.datum, '# 01 15')
        self.assertEqual(self.hianyzas2.datum, '# 02 06')
        self.assertEqual(self.hianyzas3.datum, '# 02 23')
        self.assertEqual(self.hianyzas4.datum, '# 02 05')
        self.assertEqual(self.hianyzas5.datum, '# 05 18')

    def test_aznapi_hianyzas(self) -> None:
        self.assertEqual(self.hianyzas1.aznapi_hianyzas, 6)
        self.assertEqual(self.hianyzas2.aznapi_hianyzas, 7)
        self.assertEqual(self.hianyzas3.aznapi_hianyzas, 6)
        self.assertEqual(self.hianyzas4.aznapi_hianyzas, 7)
        self.assertEqual(self.hianyzas5.aznapi_hianyzas, 6)