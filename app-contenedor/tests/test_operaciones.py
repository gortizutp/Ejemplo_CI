import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from operaciones import sumar, restar, multiplicar, dividir, es_primo, factorial


class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(2, 5), -3)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 3), 12)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            dividir(5, 0)

    def test_es_primo(self):
        self.assertTrue(es_primo(7))
        self.assertFalse(es_primo(8))
        self.assertFalse(es_primo(1))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-3)


if __name__ == "__main__":
    unittest.main()
