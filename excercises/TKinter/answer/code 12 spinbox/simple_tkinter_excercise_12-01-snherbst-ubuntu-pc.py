#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 02-02
Simple Tkinter class with Label, entry, button, functions and methods.
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_listbox1 = Listbox(master)
		self.my_listbox1.grid(row=0, column=0)

		
		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.columnconfigure(1, weight=1)
		master.rowconfigure(0, weight=1)
		master.rowconfigure(1, weight=1)
		master.rowconfigure(2, weight=1)

		master.mainloop()
		
	def scale1_changed(self, value):
		logging.debug('value {}'.format(value))
		self.my_string1.set("Value1 = {}".format(self.my_scale_var1.get()))

	def scale2_changed(self, value):
		logging.debug('value {}'.format(value))
		self.my_string2.set("Value1 = {}".format(self.my_scale_var2.get()))
		
		
master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
