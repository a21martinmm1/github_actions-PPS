# Crea un programa Python que resolva o reto FizzBuzz, onde existirá unha función que reciba como parámetro un número e devolverá “fizz” para valores divisibles por 3, “buzz” para valores divisibles por 5 e “ fizz buzz” para valores divisibles ao mesmo tempo por 3 e 5.
# Crea as probas necesarias para probar o código anterior.

# importar o módulo unittest
import unittest

# importamos a función fizzbuzz do arquivo funcions_exercicio_1.py
from funcions_exercicio_1 import fizzbuzz


# Crear unha clase TestUtils que estenda de unittest.TestCase.
class TestFizzBuzz(unittest.TestCase):
    # Comprobamos que cos múltiplos de 3 devolve fizz
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")
        self.assertEqual(fizzbuzz(6), "fizz")
        self.assertEqual(fizzbuzz(9), "fizz")

    # Comprobamos que cos múltiplos de 5 devolve buzz
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")
        self.assertEqual(fizzbuzz(10), "buzz")
        self.assertEqual(fizzbuzz(20), "buzz")

    # Comprobamos que cos múltiplos de 3 e 5 devolve fizz buzz
    def test_fizz_buzz(self):
        self.assertEqual(fizzbuzz(15), "fizz buzz")
        self.assertEqual(fizzbuzz(30), "fizz buzz")
        self.assertEqual(fizzbuzz(45), "fizz buzz")

    # Comprobamos que co resto devolve False
    def test_false(self):
        self.assertFalse(fizzbuzz(4))
        self.assertFalse(fizzbuzz(8))
        self.assertFalse(fizzbuzz(11))


if __name__ == "__main__":
    unittest.main()
