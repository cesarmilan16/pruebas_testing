import unittest
from registro_usuarios import RegistroUsuarios


class TestRegistroUsuarios(unittest.TestCase):
    def setUp(self):
        self.registro = RegistroUsuarios()

    def test_registrar_usuario(self):
        self.registro.registrar_usuario("Juan", "juan@example.com")
        self.assertEqual(len(self.registro.usuarios), 1)

    def test_mostrar_usuarios(self):
        self.registro.registrar_usuario("María", "maria@example.com")
        self.registro.registrar_usuario("Pedro", "pedro@example.com")
        self.assertEqual(len(self.registro.mostrar_usuarios()), 2)
        self.assertIn({'nombre': "María", 'email': "maria@example.com"}, self.registro.mostrar_usuarios())
        self.assertIn({'nombre': "Pedro", 'email': "pedro@example.com"}, self.registro.mostrar_usuarios())


if __name__ == '__main__':
    unittest.main()
