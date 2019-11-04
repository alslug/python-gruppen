#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 10-01
Simple Tkinter class with Label, button, functions and methods using place.
Windows showing a label and a button using place.
label is placed x=0, y=0
button is placed x=20, y=20
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_string1 = StringVar()
		self.my_label1 = Label(master, textvariable=self.my_string1)
		self.my_label1.place(x=0, y=0)
		self.my_string1.set("This is some text")

		self.my_button1 = Button(master, text="The text is changed", command=self.my_click1)
		self.my_button1.place(x=20, y=20)

		master.mainloop()
		
	def my_click1(self):
		self.my_string1.set("The text is changed")
	
master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
