#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 01
Simple Tkinter class with functions and methods.
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):
		self.my_label1 = Label(master, text="This is my string!")
		self.my_label1.pack()

		self.my_message1 = Message(master, text="this is quite a long message, but it can still be much more longer. Dont you think")
		self.my_message1.pack()
		
		master.mainloop()

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
