#!/usr/bin/python

class Pilha():
	
	def __init__(self):
		self.dados = []

	def tamanho(self):
		return len(self.dados)

	def pilhaVazia(self):
		return self.dados == []

	def empilha(self, item):
		self.dados.append(item)

	def desempilha(self):
		if not self.pilhaVazia():
			return self.dados.pop()

	def pilhaCheia(self):
		capacidade = 3
		return self.tamanho() == capacidade

