#!/usr/bin/python3

def comma_code(values):
	no_val = len (values) - 1
	return_value = ""
	i = 0
	for value in values:
		if (i == 0):
			return_value = value
		elif (i == no_val):
			return_value += ", and " + value
		else:
			return_value += ", " + value
		i += 1
	return return_value

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))
