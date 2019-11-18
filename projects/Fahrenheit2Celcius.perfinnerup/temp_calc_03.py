#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple Celcius to Fahrenheit conversion-01
Simple Celcius to Fahrenheit conversion
'''

from tkinter import *
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()
logging.debug('Start of program')		
		
def konverter():
    logging.debug('change from ceicius to fahrenheit')
    my_string2.set(float(my_string1.get()) * 1.8 + 32)
   
master = Tk()
logging.debug('Creating the class')

logging.debug('create my_label1')		
my_label1 = Label(master, text="Temp i Celcius:")
my_label1.grid(row=0, column=0)

logging.debug('create my_entry1')		
my_string1 = StringVar()
my_entry1 = Entry(master, textvariable=my_string1, justify=RIGHT)
my_string1.set("0.0")
my_entry1.grid(row=0, column=1)

logging.debug('create my_listbox1')		
my_listbox1 = Listbox(master, height=2, selectmode=SINGLE)
my_listbox1.grid(row=1, column=0, columnspan=2)
convert_list = ["Celcius -> Fahrenheit", "Fahrenheit -> Celcius"]
for text in convert_list:
    my_listbox1.insert(END, text)
my_listbox1.select_set(0)
logging.debug('current selected {}'.format(my_listbox1.curselection()[0]))		


logging.debug('create my_button1')		
my_button1 = Button(master, text="Konverter", command=konverter)
my_button1.grid(row=2, column=0, columnspan=2)

logging.debug('create mylabel2')		
my_label2 = Label(master, text="Temp i Fahrenheit:")
my_label2.grid(row=3, column=0)

logging.debug('create my_entry2')		
my_string2 = StringVar()
my_entry2 = Entry(master, textvariable=my_string2, state="readonly", justify=RIGHT)
my_entry2.grid(row=3, column=1)

konverter()

master.mainloop()



logging.debug('End of program')
