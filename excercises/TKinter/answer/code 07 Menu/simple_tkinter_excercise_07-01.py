#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 07-01
Simple Tkinter class with Label, entry, button, functions and methods.
label with a simple menu with 2 entries "Hello", "Quit". "Hello" calls a function my_click that print a message. "Quit" runs master.quit
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_string1 = StringVar()
		self.my_label1 = Label(master, textvariable=self.my_string1)
		self.my_label1.grid(row=0, column=0, sticky=EW)
		self.my_string1.set("")

		# create a toplevel menu
		self.menubar = Menu(master)
		self.menubar.add_command(label="Hello!", command=self.my_click1)
		self.menubar.add_command(label="Quit!", command=master.quit)

		# display the menu
		master.config(menu=self.menubar)

		# added resizing configs
		master.columnconfigure(0, weight=0)
		master.rowconfigure(0, weight=0)

		master.mainloop()
		
	def my_click1(self):
		logging.debug('button click')
		

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
