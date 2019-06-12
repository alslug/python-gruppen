#!/usr/bin/python3
import re, sys, os

def find_search_string(search_string, txt_line):
#	print (txt_line)
	if re.compile(search_string).search(txt_line) != None:
		print (txt_line, end="")

def open_file(search_string, filename):
	with open(filename, 'r') as read_file:
		for txt_line in read_file:
#			print(txt_line, end='')
			find_search_string(search_string, txt_line)

def search_dir_txt_files(search_string):
	print (search_string)
#	os.chdir(r'd:\Users\snherbst\OneDrive\Programmering\Automate the boring stuff with python\Chapter 8\Projects\rexex')
	os.chdir(r'/home/snherbst/OneDrive/Programmering/Automate the boring stuff with python/Chapter 8/Projects/rexex')
	for filename in os.listdir('./'):
		if filename.endswith(".txt"):
			print (filename)
			open_file(search_string, filename)

if len(sys.argv) > 1:
	if len(sys.argv[1]) > 0:
#	print (sys.argv[1])
		search_dir_txt_files(sys.argv[1])

'''
Rexex Search
Write a program that opens all .txt files in a folder and searches for any line that
matches a user-supplied regular expression. The results should be printed to the
screen.
'''
