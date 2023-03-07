from unittest import TestCase
from Seged import Seged


class TestSeged(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mo1: Seged = Seged()

    def test_hetnapja(self) -> None:
        self.assertEqual(self.mo1.hetnapja(1, 15), 'hétfő')
        self.assertEqual(self.mo1.hetnapja(2, 6), 'kedd')
        self.assertEqual(self.mo1.hetnapja(2, 23), 'péntek')
        self.assertEqual(self.mo1.hetnapja(2, 5), 'hétfő')
        self.assertEqual(self.mo1.hetnapja(5, 18), 'péntek')
