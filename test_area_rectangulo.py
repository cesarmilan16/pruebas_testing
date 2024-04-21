import unittest
from area_rectangulo import Rectangulo


class TestRectangulo(unittest.TestCase):
    def setUp(self):
        self.rectangulo = Rectangulo(10, 5)

    def test_area_rectangulo(self):
        resultado_esperado = 50
        resultado_obtenido = self.rectangulo.calcular_area()
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_perimetro_rectangulo(self):
        resultado_esperado = 30
        resultado_obtenido = self.rectangulo.calcular_perimetro()
        self.assertEqual(resultado_obtenido, resultado_esperado)


if __name__ == '__main__':
    unittest.main()
