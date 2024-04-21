import unittest
from gestion_biblioteca import Libro, Biblioteca


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.libro1 = Libro("Sol desnudo", "Isaac Asimov", "1954", "12345")

    def test_agregar_libro(self):
        self.biblioteca.agregar_libro(self.libro1)
        self.assertEqual(len(self.biblioteca.catalogo), 1)
        self.assertIn("12345", self.biblioteca.catalogo)

    def test_encontrar_libro(self):
        self.biblioteca.agregar_libro(self.libro1)
        resultado_esperado = "Titulo: Sol desnudo, Autor: Isaac Asimov, Año de publicación: 1954, ISBN: 12345"
        self.assertEqual(self.biblioteca.encontrar_libro("Sol desnudo"), resultado_esperado)


if __name__ == '__main__':
    unittest.main()
