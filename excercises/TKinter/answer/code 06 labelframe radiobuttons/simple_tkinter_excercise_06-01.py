#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 06-01
Simple Tkinter class with Label, entry, button, functions and methods.
A labelframe containing a label a entry and a button. Each time the button is pressed the text from the label swappes to the entry.
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
		self.my_string1.set("This is my text!")

		self.my_string2 = StringVar()
		self.my_entry1 = Entry(group, width=30, textvariable=self.my_string2)
		self.my_entry1.grid(row=1, column=0, sticky=EW)
		self.my_string2.set("This is a new text!")

		self.my_button1 = Button(group, text="Swap text", command=self.my_click1)
		self.my_button1.grid(row=2, column=0, sticky=EW)

		# added resizing configs
		master.columnconfigure(0, weight=0)
		master.columnconfigure(1, weight=1)
		master.columnconfigure(2, weight=0)
		master.rowconfigure(0, weight=0)
		master.rowconfigure(1, weight=1)
		master.rowconfigure(2, weight=0)

		master.mainloop()
		
	def my_click1(self):
		logging.debug('button click')
		tmp_txt = self.my_string2.get()
		self.my_string2.set(self.my_string1.get())
		self.my_string1.set(tmp_txt)

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
