#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 05-03
Simple Tkinter class with Label, listbox, entry, buttons, functions and methods.
This project shows a label with the text "Wish List:", a listbox with a predefined list ["Winnie Poe", "Guitar", "Hot Wheels Track", "Camera"], a entry containing the text "Nintendo Switch" and  two button with the text "Add a wish" and "Delete a Wish". This time with at scrollbar for the listbox.
The window is configured so its possible to maximize the window. For each widget the anghor is configured
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_label1 = Label(master, text="Wish List:")
		self.my_label1.grid(row=0, column=0, columnspan=3, sticky=EW)

		self.my_scrollbar1 = Scrollbar(master, orient=VERTICAL)
		self.my_listbox1 = Listbox(master, width=30, yscrollcommand=self.my_scrollbar1.set)
		for item in ["Winnie Poe", "Guitar", "Hot Wheels Track", "Camera"]:
			self.my_listbox1.insert(END, item)
		self.my_scrollbar1.config(command=self.my_listbox1.yview)
		self.my_scrollbar1.grid(row=1, column=2, sticky=N+S+E)
		self.my_listbox1.grid(row=1, column=0, columnspan=2, sticky=N+E+W+S)

		self.my_string = StringVar()
		self.my_entry1 = Entry(master, width=30, textvariable=self.my_string)
		self.my_entry1.grid(row=2, column=0, columnspan=3, sticky=EW)
		self.my_string.set("Nintendo Switch")

		self.my_button1 = Button(master, text="Add a Wish", command=self.my_click1)
		self.my_button1.grid(row=3, column=0, sticky=EW)

		self.my_button1 = Button(master, text="Delete a Wish", command=self.my_click2)
		self.my_button1.grid(row=3, column=1, sticky=EW)
		
		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.columnconfigure(1, weight=1)
		master.columnconfigure(2, weight=0)
		master.rowconfigure(0, weight=0)
		master.rowconfigure(1, weight=1)
		master.rowconfigure(2, weight=0)
		master.rowconfigure(3, weight=0)

		master.mainloop()
		
	def my_click1(self):
		logging.debug('button click')
		self.my_listbox1.insert(END, self.my_string.get())

	def my_click2(self):
		logging.debug('button click')
		self.my_listbox1.delete(ANCHOR)

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
