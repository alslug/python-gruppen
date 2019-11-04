#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 16-01
From Simple TKinter Class 05-03
Create a key binding for the listbox when arrow down is pressed let it call its own function
Create a key binding for the listbox when arrow up is pressed let it call its own function
Create a key binding for the entry when enter is pressed let it call its own function
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')

class my_gui:
	def __init__(self, master):

		self.master = master
		self.my_label1 = Label(master, text="Wish List:")
		self.my_label1.grid(row=0, column=0, columnspan=3, sticky=EW)

		self.my_scrollbar1 = Scrollbar(master, orient=VERTICAL)
		self.my_listbox1 = Listbox(master, selectmode=SINGLE, width=30, yscrollcommand=self.my_scrollbar1.set)
		for item in ["Winnie Poe", "Guitar", "Hot Wheels Track", "Camera"]:
			self.my_listbox1.insert(END, item)
		self.my_listbox1.selection_set(0)
		self.my_scrollbar1.config(command=self.my_listbox1.yview)
		self.my_scrollbar1.grid(row=1, column=2, sticky=N+S+E)
		self.my_listbox1.grid(row=1, column=0, columnspan=2, sticky=N+E+W+S)
		self.my_listbox1.bind("<Up>", self.key_up_pressed)
		self.my_listbox1.bind("<Down>", self.key_down_pressed)

		self.my_string = StringVar()
		self.my_entry1 = Entry(master, width=30, textvariable=self.my_string)
		self.my_entry1.grid(row=2, column=0, columnspan=3, sticky=EW)
		self.my_string.set("Nintendo Switch")
		self.my_entry1.bind("<Return>", self.key_return_pressed)

		self.my_button1 = Button(master, text="Add a Wish", command=self.my_click1)
		self.my_button1.grid(row=3, column=0, sticky=EW)

		self.my_button1 = Button(master, text="Delete a Wish", command=self.my_click2)
		self.my_button1.grid(row=3, column=1, sticky=EW)
		
		# added resizing configs
		master.columnconfigure(0, weight=1)
		master.columnconfigure(1, weight=1)
		master.columnconfigure(2, weight=0)
		master.rowconfigure(0, weight=0)
		master.rowconfigure(1, weight=1)
		master.rowconfigure(2, weight=0)
		master.rowconfigure(3, weight=0)

		master.mainloop()
		
	def my_click1(self):
		logging.debug('button click')
		self.my_listbox1.insert(END, self.my_string.get())

	def my_click2(self):
		logging.debug('button click')
		self.my_listbox1.delete(ANCHOR)

	def callback(self, value):
		print("selected subject {}".format(value))

	def key_return_pressed(self, value):
		self.my_click1()

	def key_up_pressed(self, KeyPress):
		logging.debug('KeyPress={}'.format(KeyPress))
		logging.debug('Listbox Index={}'.format(self.my_listbox1.curselection()))
		logging.debug('Listbox size={}'.format(self.my_listbox1.size()))
		#<KeyPress event state=Mod1|0x40000 keysym=Down keycode=40 x=653 y=695>
		value = str(KeyPress).split(" ")[3].split("=")[1]
		logging.debug('KeyValue={}'.format(value))
		index_val = self.my_listbox1.curselection()[0]
		self.my_listbox1.selection_clear(index_val)
		if index_val > 0:
			logging.debug('Going one up')
			self.my_listbox1.selection_set(index_val - 1)
		else:
			logging.debug('Start of Listbox Reached')
		self.master.update()
		index_val = self.my_listbox1.curselection()[0]
		logging.debug('Listbox Index={}'.format(self.my_listbox1.curselection()))
		logging.debug('Listbox index={} size={} boolean={}'.format(index_val, self.my_listbox1.size() - 1, index_val < (self.my_listbox1.size() - 1)))
		print("selected subject {}".format(value))

	def key_down_pressed(self, KeyPress):
		logging.debug('KeyPress={}'.format(KeyPress))
		logging.debug('Listbox Index={}'.format(self.my_listbox1.curselection()))
		logging.debug('Listbox size={}'.format(self.my_listbox1.size()))
		#<KeyPress event state=Mod1|0x40000 keysym=Down keycode=40 x=653 y=695>
		value = str(KeyPress).split(" ")[3].split("=")[1]
		logging.debug('KeyValue={}'.format(value))
		index_val = self.my_listbox1.curselection()[0]
		self.my_listbox1.selection_clear(index_val)
		logging.debug('Listbox index={} size={} boolean={}'.format(index_val, self.my_listbox1.size() - 1, index_val < (self.my_listbox1.size() - 1)))
		if index_val < (self.my_listbox1.size() - 1):
			logging.debug('Going one down')
			self.my_listbox1.selection_set(index_val + 1)
		else:
			logging.debug('End of Listbox Reached')
		self.master.update()
		index_val = self.my_listbox1.curselection()[0]
		logging.debug('Listbox Index={}'.format(self.my_listbox1.curselection()))
		logging.debug('Listbox index={} size={} boolean={}'.format(index_val, self.my_listbox1.size() - 1, index_val < (self.my_listbox1.size() - 1)))
		print("selected subject {}".format(value))
	
master = Tk()

logging.debug('Creating the class')
mygui = my_gui(master)

logging.debug('End of program')
