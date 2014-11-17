#!/usr/bin/env python

# Duas formas de implementar fibonacci:

def fibonacci(number):
	number = raw_input('Digite um numero: ')

	if number == 0:
		return 'Fibonacci de 0 eh igual a 0'
	elif number == 1:
		return 'Fibonacci de 1 eh igual a 1'
	else:
		return 'Fibonacci de %s eh %s' % (number, fibonacci(number-1) + fibonacci(number-2))