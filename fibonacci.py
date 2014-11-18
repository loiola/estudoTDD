#!/usr/bin/env python


def fibonacci(number):
	
	if number == 0:
		return 0

	elif number == 1:
		return 1

	elif number >= 2:
		fib = fibonacci(number-1) + fibonacci(number-2)
		return fib


number = int(raw_input("Digite um numero: "))
fibonacci(number)
print ("Fibonacci de %d eh %d" %(number, fibonacci(number)))