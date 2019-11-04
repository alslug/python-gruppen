#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 13-05
Simple Tkinter class with Label, entry, button, functions and methods.
Window showing 1 labes and 1 textbox and 2 scrollbars for x and y.
Label contain text "Text Widget"
Textbox contains the text from the file Linus Torvalds - Quotes.txt
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_label1 = Label(master, text="Text Widget")
		self.my_label1.grid(row=0, column=0, columnspan=2, sticky=NW)

		self.my_scrollbar_y = Scrollbar(master, orient=VERTICAL)
		self.my_scrollbar_x = Scrollbar(master, orient=HORIZONTAL)
		self.my_textbox = Text(master, xscrollcommand=self.my_scrollbar_x.set, yscrollcommand=self.my_scrollbar_y.set)
		self.my_textbox.insert(END, "")
		self.my_textbox.grid(row=1, column=0, sticky=N+E+S+W)
		self.my_scrollbar_y.config(command=self.my_textbox.yview)
		self.my_scrollbar_y.grid(row=1, column=1, sticky=N+S+E)
		self.my_scrollbar_x.config(command=self.my_textbox.xview)
		self.my_scrollbar_x.grid(row=2, column=0, sticky=E+S+W)

		with open('Linus Torvalds - Quotes.txt', 'r') as read_file:
			self.my_textbox.insert(END, read_file.read())

		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)
		master.rowconfigure(1, weight=1)

		master.mainloop()
		
master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
