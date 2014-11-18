#!/urs/bin/env python

import unittest
from fibonacci import fibonacci

class TestFibonacciFunction(unittest.TestCase):
	
	def test_fibonacci_of_zero(self):
		self.assertEqual(fibonacci(0), 0)

	def test_fibonnacci_resultado_um(self):
		self.assertEqual(fibonacci(1), 1)
		self.assertEqual(fibonacci(2), 1)

	def test_finonacci_demais_resultados(self):
		self.assertEqual(fibonacci(3), 2)
		self.assertEqual(fibonacci(7), 13)


if __name__ == '__main__':
	unittest.main()