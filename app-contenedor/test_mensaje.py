import unittest
from mensaje import generar_saludo

class TestMensaje(unittest.TestCase):
    
    def test_saludo(self):
        self.assertIn("bienvenido", generar_saludo("Profesor"))

if __name__ == "__main__":
    unittest.main()

    