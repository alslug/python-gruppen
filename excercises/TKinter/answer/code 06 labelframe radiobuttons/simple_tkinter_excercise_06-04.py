#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 06-04
Simple Tkinter class with Label, entry, button, functions and methods.
A labelframe containing a label 3 radiobuttons based upon a LIST. each selection gives another text in the label.
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		group = LabelFrame(master, text="Text Group", padx=5, pady=5)
		group.grid(row=0, column=0, padx=5, pady=5)

		self.my_string1 = StringVar()
		self.my_label1 = Label(group, textvariable=self.my_string1)
		self.my_label1.grid(row=0, column=0, sticky=EW)
		self.my_string1.set("")

		self.my_text = ["This is my text!", "This is a new text!", "This is another text!", "Yet another text!"]
		self.my_int1 = IntVar()
		self.my_rb = [None]*len(self.my_text)
		for i in range(len(self.my_text)):
			self.my_rb[i] = Radiobutton(group, text=self.my_text[i], variable=self.my_int1, value=i, command=self.my_click1)
			self.my_rb[i].grid(row=1+i, column=0, sticky=W)
		self.my_string1.set(self.my_text[self.my_int1.get()])

		# added resizing configs
		master.columnconfigure(0, weight=0)
		master.columnconfigure(1, weight=0)
		master.columnconfigure(2, weight=0)
		master.rowconfigure(0, weight=0)
		master.rowconfigure(1, weight=0)
		master.rowconfigure(2, weight=0)

		master.mainloop()
		
	def my_click1(self):
		logging.debug('button click')
		self.my_string1.set(self.my_text[self.my_int1.get()])

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
