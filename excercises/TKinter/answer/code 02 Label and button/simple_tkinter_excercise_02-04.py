#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 02-04
Simple Tkinter class with Label, entry, button, functions and methods.
By use of vairables. Swaping text from entry text field over to text label by pushing the button
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):
		self.my_string1 = StringVar()
		self.my_string1.set("This is my string!")
		self.my_label1 = Label(master, textvariable=self.my_string1)
		self.my_label1.pack()

		self.my_string2 = StringVar()
		self.my_entry1 = Entry(master, textvariable=self.my_string2)
		self.my_entry1.pack()
		self.my_string2.set("I changed my text")

		self.my_button1 = Button(master, text="Change Text", command=self.my_click)
		self.my_button1.pack(side=LEFT)
		
		master.mainloop()
		
	def my_click(self):
		logging.debug('button click')
		tmp_str = self.my_string1.get()
		self.my_string1.set(self.my_string2.get())
		self.my_string2.set(tmp_str)

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
