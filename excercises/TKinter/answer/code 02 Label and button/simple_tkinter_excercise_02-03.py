#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 02-03
Simple Tkinter class with Label, entry, button, functions and methods.
By use of vairables. Changeing the label text from the entry text by pushing the button
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):
		self.my_string = StringVar()
		self.my_string.set("This is my string!")
		self.my_label1 = Label(master, textvariable=self.my_string)
		self.my_label1.pack()

		self.my_entry1 = Entry(master)
		self.my_entry1.insert(0, "I changed my text")
		self.my_entry1.pack()

		self.my_button1 = Button(master, text="Change Text", command=self.my_click)
		self.my_button1.pack(side=LEFT)
		
		master.mainloop()
		
	def my_click(self):
		logging.debug('button click')
		self.my_string.set(self.my_entry1.get())

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
