import unittest
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch( 
        'builtins.input',
        return_value='50'
    )
    def test_ingreso_correcto(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 50)

    @patch(
        'builtins.input',
        return_value='-50'
    )
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(Exception):
            ingrese_numero()


if __name__ == '__main__':
    unittest.main() 
