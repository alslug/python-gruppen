#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.08.15
Title: Simple TKinter Class 15-02
Simple Tkinter class with Button, Message, functions and methods.
Window showing 3 button.
When the button "Type in a String" is pushed a Type in a String window is showed
When the button "Show warning" is pushed a Type in a Integer window is showed
When the button "Show error" is pushed a Type in a Float window is showed
'''

from tkinter import *
from tkinter import simpledialog
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_button1 = Button(master, text="Type in a String", command=self.start_dialog_entry_str)
		self.my_button1.grid(row=0, column=0, sticky=N+W+S)
		self.my_button2 = Button(master, text="Type in a Integer", command=self.start_dialog_entry_int)
		self.my_button2.grid(row=0, column=1, sticky=N+S)
		self.my_button3 = Button(master, text="Type in a Float", command=self.start_dialog_entry_float)
		self.my_button3.grid(row=0, column=2, sticky=N+E+S)

		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)

		master.mainloop()

	def start_dialog_entry_str(self):
		ret_val = simpledialog.askstring("Type in a String", "Write some text")
		logging.debug('ret_val={}'.format(ret_val))

	def start_dialog_entry_int(self):
		ret_val = simpledialog.askinteger("Type in a Integer", "Write an integer")
		logging.debug('ret_val={}'.format(ret_val))

	def start_dialog_entry_float(self):
		ret_val = simpledialog.askfloat("Type in a Flost", "Write an decimal number")
		logging.debug('ret_val={}'.format(ret_val))

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
