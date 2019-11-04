#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.08.15
Title: Simple TKinter Class 14-02
Simple Tkinter class with Button, Message, functions and methods.
Window showing 4 button.
When the button "Show askquestion" is pushed a askquestion window is showed
When the button "Show askokcancel" is pushed a askokcancel window is showed
When the button "Show askyesno" is pushed a askyesno window is showed
When the button "Show askretrycancel" is pushed a askretrycancel window is showed
'''

from tkinter import *
from tkinter import messagebox
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_button1 = Button(master, text="Show askquestion", command=self.start_dialog_askquestion)
		self.my_button1.grid(row=0, column=0, sticky=N+W+S)
		self.my_button2 = Button(master, text="Show askokcancel", command=self.start_dialog_askokcancel)
		self.my_button2.grid(row=0, column=1, sticky=N+S)
		self.my_button3 = Button(master, text="Show askyesno", command=self.start_dialog_askyesno)
		self.my_button3.grid(row=0, column=2, sticky=N+S)
		self.my_button4 = Button(master, text="Show askretrycancel", command=self.start_dialog_askretrycancel)
		self.my_button4.grid(row=0, column=3, sticky=N+E+S)

		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)

		master.mainloop()

	def start_dialog_askquestion(self):
		ret_val = messagebox.askquestion("Askquestion Title", "This is a askquestion text")
		logging.debug('return val={}'.format(ret_val))
		if ret_val == "yes":
			messagebox.showinfo("Askquestion", "You pressed YES")
		else:
			messagebox.showinfo("Askquestion", "You pressed NO")

	def start_dialog_askokcancel(self):
		ret_val = messagebox.askokcancel("Askokcancel Title", "This is a askokcancel text")
		logging.debug('return val={}'.format(ret_val))
		if ret_val:
			messagebox.showinfo("Askokcancel", "You pressed OK")
		else:
			messagebox.showinfo("Askokcancel", "You pressed CANCEL")

	def start_dialog_askyesno(self):
		ret_val = messagebox.askyesno("Askyesno Title", "This is a askyesno text")
		logging.debug('return val={}'.format(ret_val))
		if ret_val:
			messagebox.showinfo("Askyesno", "You pressed YES")
		else:
			messagebox.showinfo("Askyesno", "You pressed NO")

	def start_dialog_askretrycancel(self):
		ret_val = messagebox.askretrycancel("askretrycancel Title", "This is a askretrycancel text")
		logging.debug('return val={}'.format(ret_val))
		if ret_val:
			messagebox.showinfo("askretrycancel", "You pressed RETRY")
		else:
			messagebox.showinfo("askretrycancel", "You pressed CANCEL")

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
