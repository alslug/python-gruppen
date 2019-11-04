#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.08.15
Title: Simple TKinter Class 15-03
Simple Tkinter class with Button, Message, functions and methods.
Window showing 3 button.
When the button "Open File" is pushed a Open File window is showed
When the button "Save As File" is pushed a Save As File window is showed
'''

from tkinter import *
from tkinter import filedialog
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_button1 = Button(master, text="Open File", command=self.start_dialog_askopenfilename)
		self.my_button1.grid(row=0, column=0, sticky=N+W+S)
		self.my_button2 = Button(master, text="Save As File", command=self.start_dialog_asksaveasfilename)
		self.my_button2.grid(row=0, column=2, sticky=N+E+S)

		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)

		master.mainloop()

	def start_dialog_askopenfilename(self):
#		ret_val = filedialog.askopenfilename(defaultextension=".txt", title="Åben min Fil")
		ret_val = filedialog.askopenfilename(defaultextension=".txt", filetypes=(("My Text", "*.txt"), ("All files", "*")), title="Åben min Fil")
		logging.debug('ret_val={}'.format(ret_val))

	def start_dialog_asksaveasfilename(self):
		ret_val = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("My Text", "*.txt"), ("All files", "*")), title="Gem min Fil")
		logging.debug('ret_val={}'.format(ret_val))


master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
