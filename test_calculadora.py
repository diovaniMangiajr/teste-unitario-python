# test_calculadora.py

import unittest

from calculadora import (
    calcular_media,
    dividir,
    multiplicar,
    potencia,
    somar,
    subtrair,
)


class TestCalculadora(unittest.TestCase):
    """Conjunto de testes unitários para as funções da calculadora."""

    def test_somar_com_varios_casos(self):
        """Testa a função somar com diferentes combinações de números."""
        casos = [
            (2, 3, 5),
            (5, 0, 5),
            (0, 0, 0),
            (-2, 5, 3),
            (-2, -3, -5),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(somar(a, b), esperado)

    def test_subtrair_com_varios_casos(self):
        """Testa a função subtrair com diferentes combinações de números."""
        casos = [
            (10, 5, 5),
            (5, 10, -5),
            (0, 0, 0),
            (-5, -2, -3),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(subtrair(a, b), esperado)

    def test_multiplicar_com_varios_casos(self):
        """Testa a função multiplicar com diferentes combinações de números."""
        casos = [
            (3, 4, 12),
            (5, 0, 0),
            (-2, 3, -6),
            (-2, -3, 6),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiplicar(a, b), esperado)

    def test_dividir_com_varios_casos(self):
        """Testa a função dividir com diferentes combinações de números."""
        casos = [
            (10, 2, 5),
            (5, 2, 2.5),
            (-10, 2, -5),
            (0, 5, 0),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(dividir(a, b), esperado)

    def test_dividir_por_zero(self):
        """Garante que a divisão por zero lança a exceção ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_potencia_com_varios_casos(self):
        """Testa a função potencia com bases e expoentes variados."""
        casos = [
            (2, 3, 8),
            (5, 0, 1),
            (10, 2, 100),
            (2, -1, 0.5),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(potencia(a, b), esperado)

    def test_calcular_media_com_varios_casos(self):
        """Testa a média aritmética com listas de números variados."""
        casos = [
            ([10, 20, 30, 40], 25),
            ([7.5], 7.5),
            ([-5, -15, -10], -10),
            ([1.5, 2.5, 3.5], 2.5),
            ([-10, 10], 0),
        ]

        for lista, esperado in casos:
            with self.subTest(lista=lista):
                self.assertEqual(calcular_media(lista), esperado)

    def test_calcular_media_lista_vazia(self):
        """Garante que calcular_media lança ValueError ao receber lista vazia."""
        with self.assertRaises(ValueError):
            calcular_media([])


if __name__ == "__main__":
    unittest.main()
