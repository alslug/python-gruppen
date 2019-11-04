#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.08.15
Title: Simple TKinter Class 14-01
Simple Tkinter class with Button, Message, functions and methods.
Window showing 3 button.
When the button "Show info" is pushed a info window is showed
When the button "Show warning" is pushed a warning window is showed
When the button "Show error" is pushed a error window is showed
'''

from tkinter import *
from tkinter import messagebox
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_button1 = Button(master, text="Show info", command=self.start_dialog_info)
		self.my_button1.grid(row=0, column=0, sticky=N+W+S)
		self.my_button2 = Button(master, text="Show warning", command=self.start_dialog_warning)
		self.my_button2.grid(row=0, column=1, sticky=N+S)
		self.my_button3 = Button(master, text="Show error", command=self.start_dialog_error)
		self.my_button3.grid(row=0, column=2, sticky=N+E+S)


		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)

		master.mainloop()

	def start_dialog_info(self):
		messagebox.showinfo("Info Title", "This is a info text")

	def start_dialog_warning(self):
		messagebox.showwarning("Waring Title", "This is a waring text")

	def start_dialog_error(self):
		messagebox.showerror("Error Title", "This is a error text")
		
master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
