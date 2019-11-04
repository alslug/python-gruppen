#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 06-02
Simple Tkinter class with Label, entry, radiobutton, button, functions and methods.
A labelframe containing a label 3 radiobuttons. each selection gives another text in the label.
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		group = LabelFrame(master, text="Group", padx=5, pady=5)
		group.grid(row=0, column=0, padx=5, pady=5)


		self.my_string1 = StringVar()
		self.my_label1 = Label(group, textvariable=self.my_string1)
		self.my_label1.grid(row=0, column=0, sticky=EW)
		self.my_string1.set("")

		self.my_text = ["This is my text!", "This is a new text!", "This is another text!"]
		self.my_int1 = IntVar()
		self.my_rb1 = Radiobutton(group, text="This is my text!", variable=self.my_int1, value=0, command=self.my_click1)
		self.my_rb1.grid(row=1, column=0, sticky=W)
		self.my_rb2 = Radiobutton(group, text="This is a new text!", variable=self.my_int1, value=1, command=self.my_click1)
		self.my_rb2.grid(row=2, column=0, sticky=W)
		self.my_rb3 = Radiobutton(group, text="This is another text!", variable=self.my_int1, value=2, command=self.my_click1)
		self.my_rb3.grid(row=3, column=0, sticky=W)
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
