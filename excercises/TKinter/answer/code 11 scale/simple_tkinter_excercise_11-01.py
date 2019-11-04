#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 11-01
Simple Tkinter class with Label, entry, button, functions and methods.
Window showing 2 labes and 2 types of scale one vertical and one horizontal
When altering the slider 1 the label 1 text shows the coresponding value
When altering the slider 2 the label 2 text shows the coresponding value
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

		self.my_string2 = StringVar()
		self.my_label2 = Label(master, textvariable=self.my_string2)
		self.my_label2.grid(row=1, column=0, sticky=NW)
		self.my_string2.set("Value2 = ")
		
		self.my_scale_var1 = DoubleVar()
		self.my_scale1 = Scale(master, from_=0, to=100, orient=HORIZONTAL, variable=self.my_scale_var1, command=self.scale1_changed)
		self.my_scale1.grid(row=2, column=0, sticky=NW)
		
		self.my_scale_var2 = DoubleVar()
		self.my_scale12 = Scale(master, from_=0, to=200, variable=self.my_scale_var2, command=self.scale2_changed)
		self.my_scale12.grid(row=0, column=1, rowspan=3, sticky=NE)

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
