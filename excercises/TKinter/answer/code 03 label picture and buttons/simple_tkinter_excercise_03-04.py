#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 03-04
Simple Tkinter class with Picture Label, button, functions and methods.
A Picture label showing a .jpg picture, the label picture has 5 buttons assigned that can change the picture
'''

from tkinter import *
from PIL import Image, ImageTk
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):
		
		self.my_button1 = Button(master, text="picture 01", command=self.my_click1)
		self.my_button1.grid(row=0, column=0)

		self.my_button2 = Button(master, text="picture 02", command=self.my_click2)
		self.my_button2.grid(row=0, column=1)

		self.my_button3 = Button(master, text="picture 03", command=self.my_click3)
		self.my_button3.grid(row=0, column=2)

		self.my_button4 = Button(master, text="picture 04", command=self.my_click4)
		self.my_button4.grid(row=0, column=3)

		self.my_button4 = Button(master, text="picture 05", command=self.my_click5)
		self.my_button4.grid(row=0, column=4)

		self.image = Image.open("python01.jpg")
		self.photo = ImageTk.PhotoImage(self.image)
		self.my_label1 = Label(master, image=self.photo)
		self.my_label1.grid(row=1, column=0, columnspan=5)
		
		
		master.mainloop()
		
	def change_picture(self, image_file):
		logging.debug('change picture 1 to picture01')
		self.image = Image.open(image_file)
		self.photo = ImageTk.PhotoImage(self.image)
		self.my_label1.config(image=self.photo)

	def my_click1(self):
		logging.debug('change picture 1 to picture01')
		self.change_picture("python01.jpg")

	def my_click2(self):
		logging.debug('change picture 1 to picture02')
		self.change_picture("python02.jpg")

	def my_click3(self):
		logging.debug('change picture 2 to picture03')
		self.change_picture("python03.jpg")

	def my_click4(self):
		logging.debug('change picture 2 to picture04')
		self.change_picture("python04.jpg")

	def my_click5(self):
		logging.debug('change picture 2 to picture04')
		self.change_picture("python05.jpg")

master = Tk()

mygui = my_gui(master)
logging.debug('Creating the class')

logging.debug('End of program')
