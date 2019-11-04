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

my_label1 = Label(master, text="Temp i Celcius:")
my_label1.grid(row=0, column=0)

my_string1 = StringVar()
my_entry1 = Entry(master, textvariable=my_string1, justify=RIGHT)
my_string1.set("0.0")
my_entry1.grid(row=0, column=1)

my_button1 = Button(master, text="Konverter", command=konverter)
my_button1.grid(row=1, column=0, columnspan=2)

my_label2 = Label(master, text="Temp i Fahrenheit:")
my_label2.grid(row=2, column=0)

my_string2 = StringVar()
my_entry2 = Entry(master, textvariable=my_string2, state=DISABLED, justify=RIGHT)
my_entry2.grid(row=2, column=1)

konverter()

master.mainloop()


logging.debug('End of program')
