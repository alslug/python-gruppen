#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 03-01
Simple Tkinter class with Picture Label, button, functions and methods.
A label showing a .ppm picture with 2 buttons that can change the pictures
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):
		self.photo = PhotoImage(file="python01.ppm")
		self.my_label1 = Label(master, image=self.photo)
		self.my_label1.pack()
		
		self.my_button1 = Button(master, text="Picture 01", command=self.my_click1)
		self.my_button1.pack(side=LEFT)

		self.my_button2 = Button(master, text="Picture 02", command=self.my_click2)
		self.my_button2.pack(side=RIGHT)
		
		master.mainloop()
		
	def my_click1(self):
		self.photo = PhotoImage(file="python01.ppm")
		self.my_label1.config(image=self.photo)

	def my_click2(self):
		self.photo = PhotoImage(file="python02.ppm")
		self.my_label1.config(image=self.photo)

master = Tk()

mygui = my_gui(master)
logging.debug('Creating the class')

logging.debug('End of program')
