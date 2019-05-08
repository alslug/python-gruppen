#!/usr/bin/python3

def collatz(number):
	return_number = 0
	if not (number % 2 ):
		return_number = number // 2
	else:
		return_number = 3 * number + 1
	return return_number

return_number = 0
while (return_number != 1):
	number = int(input())
	return_number = collatz(number)
	print(return_number)
