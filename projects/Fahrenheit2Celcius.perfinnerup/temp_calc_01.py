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
my_label1.pack()

my_string1 = StringVar()
my_entry1 = Entry(master, textvariable=my_string1)
my_string1.set("0.0")
my_entry1.pack()

my_button1 = Button(master, text="Konverter", command=konverter)
my_button1.pack(side=LEFT)
my_label2 = Label(master, text="Temp i Fahrenheit:")
my_label2.pack()

my_string2 = StringVar()
my_entry2 = Entry(master, textvariable=my_string2, state=DISABLED)
my_entry2.pack()

master.mainloop()


logging.debug('End of program')
