#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple Class
Simple Class with functions and methods.
'''

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_class:
	def __init__(self):
		self.my_string = "This is my string"
		logging.debug('my_string={}'.format(self.my_string))
		
	def my_print(self):
		print(self.my_string)
		logging.debug('print my_class.my_string')


myclass = my_class()
logging.debug('create myclass')

myclass.my_print()
logging.debug('print {}'.format(myclass.my_string))

myclass.my_string = "I changed my string"
logging.debug('myclass.my_string ={}'.format(myclass.my_string))

myclass.my_print()
logging.debug('print {}'.format(myclass.my_string))

logging.debug('End of program')

 
