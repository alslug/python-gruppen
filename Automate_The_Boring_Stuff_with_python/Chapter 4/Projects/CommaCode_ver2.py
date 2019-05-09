#!/usr/bin/python3

def comma_code(values):
	no_val = len (values) - 1
	return_value = ""
	for i in range(len(values)):
		if (i == 0):
			return_value = values[i]
		elif (i == no_val):
			return_value += ", and " + values[i]
		else:
			return_value += ", " + values[i]
		i += 1
	return return_value

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))
