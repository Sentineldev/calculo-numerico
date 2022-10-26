


#standart imports
import unittest


#local imports

import errores
import teoremas




class TestErrores(unittest.TestCase):


    def test_error_abs(self):

        self.assertEqual(errores.error_absoluto(20_000,19_999),1)
        self.assertEqual(errores.error_absoluto(5,4),1)


    def test_error_relativo(self):
        self.assertEqual(errores.error_relativo(1,20_000),5e-05)
        self.assertEqual(errores.error_relativo(1,5),0.2)


class TestTeoremas(unittest.TestCase):
    

    def tests_valor_intermedio(self):

        self.assertFalse(teoremas.existe_valor_intermedio(
            lambda x : x-4,
            4,
            4
        ))

        self.assertTrue(teoremas.existe_valor_intermedio(
            lambda x : x-4,
            1,
            5
        ))


    def test_es_raiz(self):

        self.assertTrue(teoremas.es_numero_raiz(
            lambda x : x^2-4,
            -2
        ))
        self.assertFalse(teoremas.es_numero_raiz(
            lambda x : x^2-4,
            4
        ))

    










if __name__ == "__main__":
    unittest.main()