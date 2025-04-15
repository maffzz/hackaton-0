import unittest
from src.main import calculate  # Asegúrate que calculate esté en main.py

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calculate("2 + 3"), 5)

    def test_resta(self):
        self.assertEqual(calculate("5 - 2"), 3)

    def test_multiplicacion(self):
        self.assertEqual(calculate("4 * 3"), 12)

if __name__ == '__main__':
    unittest.main()
