
import unittest
from unittest.mock import patch

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.exceptions import ingrese_numero, NumeroDebeSerPositivo


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
        with self.assertRaises(NumeroDebeSerPositivo): 
            ingrese_numero()

    @patch(
        'builtins.input',
        return_value='aaoe'
    )
    def test_ingreso_texto_no_num(self, patch_input):
        with self.assertRaises(ValueError):  
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()
