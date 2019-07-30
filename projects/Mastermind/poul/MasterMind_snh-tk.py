#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: MasterMind game
This game is based upon the board Game Mastermind written in python with Tkinter GUI.
'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable()
logging.debug('Start of program')


class MasterMind:

	def __init__(self, master):
		self.master = master
		master.title("MasterMind")
	
		self.colour_list = ["red", "yellow", "green", "blue", "white", "black"]
		self.actual_guess = [""]*4
		self.random_colours = [""]*4
		self.guess_no = 0
		self.listbox = [None]*6
		self.combobox = [None]*4
		self.label_no = tk.Label(master, text="no:{}".format(guess_count))
		self.label_no.grid(row=0, column=0)
		for i in range(4):
			self.combobox[i] = ttk.Combobox(master, values=self.colour_list)
			self.combobox[i].grid(row=0, column=i + 1)
			self.combobox[i].current(i)
			
		self.label_reweal = tk.Label(master, text="reweal:")
		self.label_reweal.grid(row=0, column=5)
		for i in range(6):
			self.listbox[i] = tk.Listbox(master)
			self.listbox[i].grid(row=1, column=i)

		self.button_guess = tk.Button(master, text="Guess", command=self.make_guess)
		self.button_guess.grid(columnspan=5, row=2, column=0)
		self.button_clear = tk.Button(master, text="Clear", command=self.clear_guess)
		self.button_clear.grid(row=2, column=5)
#		logging.debug('colour_list:{}'.format(colour_list))
		for i in range(1, guess_count + 1):
			self.listbox[0].insert(tk.END, str(i))
		self.listbox[0].config(width=5)
		self.listbox[1].config(width=10)
		self.listbox[2].config(width=10)
		self.listbox[3].config(width=10)
		self.listbox[4].config(width=10)
		self.listbox[5].config(width=30)
		self.combobox[0].config(width=10)
		self.combobox[1].config(width=10)
		self.combobox[2].config(width=10)
		self.combobox[3].config(width=10)
		
		self.generate_random_colours()
		tk.mainloop()
		

	def make_guess(self):
#		print(self.combobox[0].current(), self.combobox[0].get())
		for i in range(4):
			self.listbox[i+1].insert(tk.END, self.combobox[i].get())
			self.actual_guess[i] = self.combobox[i].get()
		logging.debug('actual_guess:{}'.format(self.actual_guess))
		
		if self.actual_guess == self.random_colours:
			self.correct_asnwer()
			self.clear_guess()
		else:
			self.reveal_info_pos()
		
			self.guess_no += 1
			if self.guess_no == guess_count:
				self.show_correct_asnwer()
				self.clear_guess()


	def clear_guess(self):
#		print(self.combobox[0].current(), self.combobox[0].get())
		for i in range(5):
			self.listbox[i+1].delete(0, tk.END)
		self.random_colours = [""]*4
		self.actual_guess = [""]*4
		self.guess_no = 0
		self.generate_random_colours()

	def generate_random_colours(self):
		for i in range(4):
			random_colour = self.colour_list[random.randint(0, len(self.colour_list) - 1)]
			logging.debug('Random Colour:{}'.format(random_colour))
			while random_colour in self.random_colours:
				random_colour = self.colour_list[random.randint(0, len(self.colour_list) - 1)]
				logging.debug('Random Colour:{}'.format(random_colour))
			self.random_colours[i] = random_colour
		logging.debug('Random Colour list:{}'.format(self.random_colours))

	def reveal_info_pos(self):
		guess = ["empty"]*4		#empty=farve og pos ikke gættet rigtigt; black=farve og pos gættet rigtigt; white=farve gættet rigtigt
		#find korrekt farve og pos
		for i in range(len(self.actual_guess)):
			if self.actual_guess[i] == self.random_colours[i]:
				guess[i] = "black"
		logging.debug('find correct color and pos:{}'.format(guess))
		#find korrekt farve
		for i in range(len(self.actual_guess)):
			if guess[i] != "empty":
				continue
			if self.actual_guess[i] in self.random_colours:
				guess[i] = "white"
		logging.debug('find correct colour:{}'.format(guess))
		self.listbox[5].insert(tk.END, ",".join(guess))

	def reveal_info(self):
		guess = [""]*4		#empty=farve og pos ikke gættet rigtigt; black=farve og pos gættet rigtigt; white=farve gættet rigtigt
		#find korrekt farve og pos
		for i in range(len(self.actual_guess)):
			if self.actual_guess[i] == self.random_colours[i]:
				guess[i] = "black"
		logging.debug('find correct color and pos:{}'.format(guess))
		#find korrekt farve
		for i in range(len(self.actual_guess)):
			if guess[i] != "empty":
				continue
			if self.actual_guess[i] in self.random_colours:
				guess[i] = "white"
		logging.debug('find correct colour:{}'.format(guess))
		#vis svar i 
		answer = [""]*4
		i = 0 
		#vis korrekt farve og pos
		for gues in guess:
			if gues == "black":
				answer[i] = "black"
				i += 1
		#vis korrekt farve og pos
		for gues in guess:
			if gues == "white":
				answer[i] = "white"
				i += 1
		self.listbox[5].insert(tk.END, ",".join(answer))

	def correct_asnwer(self):
		messagebox.showinfo("You guessed right!", "You guessed: {}\nThe answer was: {}".format(", ".join(self.actual_guess), ", ".join(self.random_colours)))

	def show_correct_asnwer(self):
		messagebox.showinfo("You guessed wrong!", "You guessed: {}\nThe correct answer was: {}".format(", ".join(self.actual_guess), ", ".join(self.random_colours)))

guess_count = 10

root = tk.Tk()
mm = MasterMind(root)

logging.debug('End of program')

