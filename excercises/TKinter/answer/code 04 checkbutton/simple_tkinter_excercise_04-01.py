#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 04-01
Simple Tkinter class with checkbutton, button, functions and methods.
A checkbutton with label text howing. Each time the button is pressed the status is printed
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):
		self.my_int = IntVar()
		self.my_checkbutton1 = Checkbutton(master, text="Checked", variable=self.my_int)
		self.my_checkbutton1.grid(row=0, column=0)

		self.my_button1 = Button(master, text="Check Status", command=self.my_click)
		self.my_button1.grid(row=1, column=0)
		
		master.mainloop()
		
	def my_click(self):
		logging.debug('button click')
		print ("my_int={}".format(str(self.my_int.get())))

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
