#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 04-02
Simple Tkinter class with checkbutton, button, functions and methods.
A checkbutton with label text showing "Checked". Each time the checkbutton is changed the status is printed
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):
		self.my_int = IntVar()
		self.my_label1 = Checkbutton(master, text="Expand", variable=self.my_int, command=self.my_click)
		self.my_label1.grid(row=0, column=0)

		master.mainloop()
		
	def my_click(self):
		logging.debug('button click')
		print ("my_int={}".format(str(self.my_int.get())))

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
