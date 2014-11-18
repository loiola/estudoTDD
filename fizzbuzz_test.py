#!/usr/bin/env python

import unittest
from fizzbuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):

	def test_NumeroSimples(self):
		self.assertEqual(fizzBuzz(1), 1)
		self.assertEqual(fizzBuzz(2), 2)
		self.assertEqual(fizzBuzz(4), 4)

	def test_MultiploDeTres(self):
		self.assertEqual(fizzBuzz(3), "fizz")
		self.assertEqual(fizzBuzz(9), "fizz")

	def test_MultiploDeCinco(self):
		self.assertEqual(fizzBuzz(5), "buzz")
		self.assertEqual(fizzBuzz(10), "buzz")

	def test_MultiploDeTresECinco(self):
		self.assertEqual(fizzBuzz(15), "fizzbuzz")

if __name__ == '__main__':
	unittest.main()