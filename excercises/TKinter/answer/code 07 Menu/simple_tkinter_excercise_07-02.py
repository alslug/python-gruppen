#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 07-02
Simple Tkinter class with Label, entry, button, functions and methods.
label with a simple menu with 3 dropdown menues "File", "Edit", "Help".
"File" opens another menu with "Open", "Save", "Exit"
"Edit" opens another menu with "Cut", "Copy", "Paste"
"Help" opens another menu with "About", "Save", "Exit"
"File->Exit" runs the functionmaster.quit
All other menu entries runs my_click
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
		self.my_label1.grid(row=0, column=0, sticky=EW)
		self.my_string1.set("")

		# create a toplevel menu
		self.menubar = Menu(master)

		# create a pulldown menu, and add it to the menu bar
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="Open", command=self.my_click1)
		self.filemenu.add_command(label="Save", command=self.my_click1)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command=master.quit)
		self.menubar.add_cascade(label="File", menu=self.filemenu)

		# create more pulldown menus
		editmenu = Menu(self.menubar, tearoff=0)
		editmenu.add_command(label="Cut", command=self.my_click1)
		editmenu.add_command(label="Copy", command=self.my_click1)
		editmenu.add_command(label="Paste", command=self.my_click1)
		self.menubar.add_cascade(label="Edit", menu=editmenu)

		helpmenu = Menu(self.menubar, tearoff=0)
		helpmenu.add_command(label="About", command=self.my_click1)
		self.menubar.add_cascade(label="Help", menu=helpmenu)

		# display the menu
		master.config(menu=self.menubar)

		# added resizing configs
		master.columnconfigure(0, weight=0)
		master.rowconfigure(0, weight=0)

		master.mainloop()
		
	def my_click1(self):
		logging.debug('button click')
		

master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
