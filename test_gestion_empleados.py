import unittest
from gestion_empleados import Empleado


class TestEmpleado(unittest.TestCase):
    def test_calcular_salario_anual(self):
        empleado = Empleado("Juan", "Perez", 1000, 10)
        resultado_esperado = 12500
        resultado_obtenido = empleado.calcular_salario_anual()
        self.assertEqual(resultado_obtenido, resultado_esperado)


if __name__ == '__main__':
    unittest.main()
