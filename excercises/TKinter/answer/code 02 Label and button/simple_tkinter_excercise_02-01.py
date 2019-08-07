#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 02-01
Simple Tkinter class with Label, button, functions and methods.
Changing the label text by pushing the button
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):
		self.my_string = "This is my string!"
		self.my_label1 = Label(master, text=self.my_string)
		self.my_label1.pack()
		self.my_button1 = Button(master, text="Change Text", command=self.my_click)
		self.my_button1.pack(side=LEFT)
		
		master.mainloop()
		
	def my_print(self):
		logging.debug('print my string')
		print (self.my_string)
	
	def form_update(self, master):
		logging.debug('update form')
		master.update()

	def my_click(self):
		self.my_string = 'I changed my text'
		logging.debug('I changed my text')
		self.my_label1.config(text=self.my_string)

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('printing my_string')
mygui.my_print()

logging.debug('End of program')
