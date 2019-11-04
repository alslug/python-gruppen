#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.08.15
Title: Simple TKinter Class 15-01
Simple Tkinter class with Button, Message, functions and methods.
Window showing 1 button.
When the button "Show Color" is pushed a color dialog is showed selected the color red
'''

from tkinter import *
from tkinter import colorchooser
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_button1 = Button(master, text="Show Color", command=self.start_dialog_color)
		self.my_button1.grid(row=0, column=0, sticky=N+W+S)

		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)

		master.mainloop()

	def start_dialog_color(self):
		ret_val = colorchooser.askcolor((255,0,0), title="Vis Farve")
		logging.debug('ret_val={}'.format(ret_val))

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
