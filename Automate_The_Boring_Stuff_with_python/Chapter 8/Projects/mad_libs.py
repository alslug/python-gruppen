#!/usr/bin/python3
import re, sys, os

search_list = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
new_text = ''
with open('test.txt', 'r') as read_file:
	read_file_txt = read_file.read()
#	print (read_file_txt)
#	read_file_list = re.compile(r'[\w]{1,}').findall(read_file_txt)
	read_file_list = read_file_txt.split(' ')
#	print (read_file_list)
	new_text = ""
	for text in read_file_list:
		if (text.strip(".,;:?")) in search_list:
#			print (text.strip(".,;:?"))
			print (' Enter an %s:' % text.lower(), end = '')
			new_text += text.replace(text.strip(".,;:?"), input())
		else:
#			print (text)
			new_text += text
		new_text += ' '
print(new_text)

'''
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.
'''
