#!/usr/bin/env python

def multiploDeTres(numero):
	return not numero % 3

def multiploDeCinco(numero):
	return not numero % 5

def fizzBuzz(numero):
	if multiploDeTres(numero) and multiploDeCinco(numero):
		return "fizzbuzz"

	if multiploDeTres(numero):
		return "fizz"

	if multiploDeCinco(numero):
		return "buzz"

	return numero

numero = int(raw_input("Digite um numero: "))
multiploDeTres(numero)
multiploDeCinco(numero)
fizzBuzz(numero)
print("O resultado fizzbuzz para o numero %d eh %s" %(numero, fizzBuzz(numero)))



