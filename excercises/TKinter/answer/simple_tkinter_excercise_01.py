#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple Class
Simple Class with functions and methods.
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):
		self.my_string = "This is my string!"
		self.my_label1 = Label(master, text=self.my_string)
		self.my_label1.pack()
		
		master.mainloop()
		
	def my_print(self, master):
		print (self._mystring)
		logging.debug('update form')
	
	def form_update(self, master):
		master.update()
		logging.debug('update form')


master = Tk()

mygui = my_gui(master)
logging.debug('Creating the class')

mygui.my_print()
logging.debug('mygui.my_string = {}'.format(mygui.my_string))
mygui.my_string = "I changed my string!"
logging.debug('mygui.my_string = {}'.format(mygui.my_string))
mygui.form_update(master)		#This gives an error as the 

logging.debug('End of program')
