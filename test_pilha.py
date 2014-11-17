#!/usr/bin/python

import unittest
from pilha import Pilha

class TestPilha(unittest.TestCase):

	def test_pilha_vazia(self):
		p = Pilha()
		self.assertTrue(p.pilhaVazia())
		self.assertEqual(p.tamanho(), 0)

	def test_empilha_elementos(self):
		p = Pilha()
		p.empilha(1)
		self.assertFalse(p.pilhaVazia())
		self.assertEqual(p.tamanho(), 1)

		p.empilha(2)
		self.assertFalse(p.pilhaVazia())
		self.assertEqual(p.tamanho(), 2)

	def test_desempilha_elemento(self):
		p = Pilha()
		p.empilha(1)
		p.empilha(2)
		p.desempilha()
		self.assertFalse(p.pilhaVazia())
		self.assertEqual(p.tamanho(), 1)

	def test_desempilhar_pilha_vazia(self):
		p = Pilha()
		self.assertTrue(p.pilhaVazia())
		p.desempilha()
		self.assertFalse(p.desempilha())

	def test_empilhar_em_pilha_cheia(self):
		p = Pilha()
		p.empilha(1)
		p.empilha(2)
		p.empilha(3)
		self.assertTrue(p.pilhaCheia())
		self.assertEqual(p.tamanho(), 3)
		p.empilha(4)
		self.assertFalse(p.empilha(4))


if __name__ == '__main__':
	unittest.main()