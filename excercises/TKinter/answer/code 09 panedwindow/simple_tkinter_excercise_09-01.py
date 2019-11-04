#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 09-01
Simple Tkinter class with panedwindow, Label.
Window showing a paned window with 2 labels with text "Top Pane" and "Buttom Pane"
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.my_panedwindow1 = PanedWindow(master, orient=VERTICAL, sashrelief=SUNKEN, cursor="circle", height=100)
		self.my_panedwindow1.grid(row=0, column=0, sticky=NS)

		self.my_label1 = Label(self.my_panedwindow1, text="Top Pane")
		self.my_panedwindow1.add(self.my_label1)

		self.my_label2 = Label(self.my_panedwindow1, text="Buttom Pane")
		self.my_panedwindow1.add(self.my_label2)

		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.columnconfigure(1, weight=1)
		master.rowconfigure(0, weight=1)
		master.rowconfigure(1, weight=1)

		master.mainloop()
		
master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
