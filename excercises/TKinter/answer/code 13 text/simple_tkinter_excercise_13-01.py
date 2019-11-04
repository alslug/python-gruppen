#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 13-01
Simple Tkinter class with Label, entry, button, functions and methods.
Window showing 1 labes and 1 textbox.
Label contain text "Text Widget"
Textbox contains "When, in disgrace with fortune and men's eyes,\nI all alone beweep my outcast state,\nAnd trouble deaf heaven with my bootless cries,\nAnd look upon myself and curse my fate"
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_label1 = Label(master, text="Text Widget")
		self.my_label1.grid(row=0, column=0, sticky=NW)

		self.my_textbox = Text(master)
		self.my_textbox.insert(END, "When, in disgrace with fortune and men's eyes,\nI all alone beweep my outcast state,\nAnd trouble deaf heaven with my bootless cries,\nAnd look upon myself and curse my fate")
		self.my_textbox.grid(row=1, column=0, sticky=NW)

		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)
		master.rowconfigure(1, weight=1)

		master.mainloop()
		
master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
