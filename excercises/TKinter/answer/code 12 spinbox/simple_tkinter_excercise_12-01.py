#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 12-01
Simple Tkinter class with Label, entry, button, functions and methods.
Window showing 1 labes and 1 spinbox. Both widget should point at the same StringVar
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
		self.my_label1.grid(row=0, column=0, sticky=NW)
		self.my_string1.set("Value1 = ")

		self.my_spinbox = Spinbox(master, from_=0, to=10, textvariable=self.my_string1, command=self.scale1_changed)
		self.my_spinbox.grid(row=1, column=0, sticky=NW)

		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)
		master.rowconfigure(1, weight=1)

		master.mainloop()
		
	def scale1_changed(self):
		logging.debug('value changed')
		
		
master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
