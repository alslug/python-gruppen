#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 08-01
Simple Tkinter class with Label, entry, button, functions and methods.
Window showing a option menu containing values "one", "two", "three" and a label. Both widgets have the same StringVar parameter.
The optionmenu calls the function my_click
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_string1 = StringVar()
		self.my_string1.set("one") # default value

		self.my_optionmenu = OptionMenu(master, self.my_string1, "one", "two", "three", command=self.my_click1)
		self.my_optionmenu.grid(row=0, column=0, sticky=EW)

		self.my_label1 = Label(master, textvariable=self.my_string1)
		self.my_label1.grid(row=1, column=0, sticky=EW)
		self.my_string1.set("")

		# added resizing configs
		master.columnconfigure(0, weight=0)
		master.columnconfigure(1, weight=0)
		master.rowconfigure(0, weight=0)
		master.rowconfigure(1, weight=0)

		master.mainloop()
		
	def my_click1(self, value_selected):
		logging.debug('button click')
		logging.debug('value_selected={}'.format(value_selected))

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
