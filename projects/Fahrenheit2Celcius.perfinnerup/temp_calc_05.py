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
logging.disable(10)
logging.debug('Start of program')       
        
def convert_temp():
    if my_listbox1.curselection()[0] == 0:    #celcius -> fahrenheit selected
        logging.debug('change from celcius to fahrenheit')
        my_entry2_str.set(float(my_entry1_str.get()) * 1.8 + 32)
    elif my_listbox1.curselection()[0] == 1:    #fahrenheit -> celcius selected
        logging.debug('change from fahrenheit to celcius')
        my_entry2_str.set((float(my_entry1_str.get()) - 32)/ 1.8)
        

def change_txt_in_label():
    master.update()
    logging.debug('current selected {} {}'.format(my_listbox1.curselection()[0], convert_list[my_listbox1.curselection()[0]].split(" -> ")))      
    temp_txt = convert_list[my_listbox1.curselection()[0]].split(" -> ") #split "celcius -> fahrenheit" into list["celcius", "fahrenheit"]
    my_label1_str.set("Temperature in {}:".format(temp_txt[0])) #set label1 text to "temperature in celcius/fahrenheit"
    my_label2_str.set("Temperature in {}:".format(temp_txt[1])) #set label2 text to "temperature in fahrenheit/celcius"
    convert_temp()

def my_listbox1_click(value):
    change_txt_in_label()
   
master = Tk()  #Create Tkinter window
logging.debug('Creating the class')
master.title("Temp calc") #Change window title

logging.debug('create my_label1')
my_label1_str = StringVar() #create the variable "my_label1_str"
my_label1 = Label(master, textvariable=my_label1_str) #create the label "my_label1"
my_label1.grid(row=0, column=0) #place "my_label1" on row=0 column=0

logging.debug('create my_entry1')       
my_entry1_str = StringVar()
my_entry1 = Entry(master, textvariable=my_entry1_str, justify=RIGHT) #create the entry "my_entry1"
my_entry1_str.set("0.0")
my_entry1.grid(row=0, column=1)

logging.debug('create my_listbox1')     
my_listbox1 = Listbox(master, height=2, selectmode=SINGLE) #create the listbox "my_listbox1"
my_listbox1.grid(row=1, column=0, columnspan=2)
#create the convertion list
convert_list = ["Celcius -> Fahrenheit", "Fahrenheit -> Celcius"]
for text in convert_list:
    my_listbox1.insert(END, text) #insert the convertion list into "my_listbox1"
my_listbox1.select_set(0) #select the first item in "my_listbox1"
logging.debug('current selected {}'.format(my_listbox1.curselection()[0]))      
my_listbox1.bind("<Button-1>", my_listbox1_click) #create the mouse button handle for "my_listbox1"

logging.debug('create my_button1')      
my_button1 = Button(master, text="Konverter", command=convert_temp) #create the button "my_button1"
my_button1.grid(row=2, column=0, columnspan=2)

logging.debug('create my_label2')
my_label2_str = StringVar()
my_label2 = Label(master, textvariable=my_label2_str) #create the label "my_label2"
my_label2.grid(row=3, column=0)

logging.debug('create my_entry2')       
my_entry2_str = StringVar()
my_entry2 = Entry(master, textvariable=my_entry2_str, state="readonly", justify=RIGHT) #create the entry "my_entry2" in readonly mode
my_entry2.grid(row=3, column=1)

change_txt_in_label() #First time call this function

master.mainloop()

logging.debug('End of program')
