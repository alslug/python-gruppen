#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 03-03
Simple Tkinter class with Picture Label, button, functions and methods.
Introducing grid
Tow label showing a .ppm picture, each label picture has 2 buttons assigned that can change the picture
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):
		
		self.photo1 = PhotoImage(file="python01.ppm")
		self.my_label1 = Label(master, image=self.photo1)
		self.my_label1.grid(row=0, column=0, columnspan=2)
		
		self.my_button1 = Button(master, text="picture 01", command=self.my_click1)
		self.my_button1.grid(row=1, column=0)

		self.my_button2 = Button(master, text="picture 02", command=self.my_click2)
		self.my_button2.grid(row=1, column=1)

		self.photo2 = PhotoImage(file="python02.ppm")
		self.my_label2 = Label(master, image=self.photo2)
		self.my_label2.grid(row=2, column=0, columnspan=2)
		
		self.my_button3 = Button(master, text="picture 01", command=self.my_click3)
		self.my_button3.grid(row=3, column=0)

		self.my_button4 = Button(master, text="picture 02", command=self.my_click4)
		self.my_button4.grid(row=3, column=1)
		
		master.mainloop()
		
	def my_click1(self):
		logging.debug('change picture 1 to picture01')
		self.photo1 = PhotoImage(file="python01.ppm")
		self.my_label1.config(image=self.photo1)

	def my_click2(self):
		logging.debug('change picture 1 to picture02')
		self.photo1 = PhotoImage(file="python02.ppm")
		self.my_label1.config(image=self.photo1)

	def my_click3(self):
		logging.debug('change picture 2 to picture01')
		self.photo2 = PhotoImage(file="python01.ppm")
		self.my_label2.config(image=self.photo2)

	def my_click4(self):
		logging.debug('change picture 2 to picture01')
		self.photo2 = PhotoImage(file="python02.ppm")
		self.my_label2.config(image=self.photo2)

master = Tk()

mygui = my_gui(master)
logging.debug('Creating the class')

logging.debug('End of program')
