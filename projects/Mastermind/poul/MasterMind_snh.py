#!/usr/bin/python3
#MasterMind-20190703pel

import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#logging.disable()

logging.debug('Start of program')

def generer_farver(randomList):
	for i in range(4):
		randomList[i] = colorList[random.randint(0, 7)]
	logging.debug('random list:{}'.format(randomList))

def generer_farver_1gang(randomList):
	for i in range(4):
		tilfaeldig_farve = colorList[random.randint(0, 7)]
		logging.debug('tilfaeldig_farve:{}'.format(tilfaeldig_farve))
		while tilfaeldig_farve in randomList:
			tilfaeldig_farve = colorList[random.randint(0, 7)]
			logging.debug('tilfaeldig_farve:{}'.format(tilfaeldig_farve))
		randomList[i] = tilfaeldig_farve
	logging.debug('random list:{}'.format(randomList))

def gaet_input(farvegaet, gaet_nr):
	print("indtast dit gæt {} i farver adskilt med komma eks: sort,gul,grøn,pink".format(gaet_nr))
	input_str = input()
	if input_str != "":
		while (len(input_str.split(",")) != 4) or ("" in input_str.split(",")):
			input_str = input("skriv venligst farverne som i eksemplet:")
		farvegaet = input_str.lower().split(",")
	logging.debug('svar farve:{}'.format(farvegaet))
	return farvegaet

def vis_svar_pos(farvegaet, randomList):
	gaettet = ["tom"]*4		#tom=farve og pos ikke gættet rigtigt; sort=farve og pos gættet rigtigt; hvid=farve gættet rigtigt
	#find korrekt farve og pos
	for i in range(len(farvegaet)):
		if farvegaet[i] == randomList[i]:
			gaettet[i] = "sort"
	logging.debug('find korrekt farve og pos:{}'.format(gaettet))
	#find korrekt farve
	for i in range(len(farvegaet)):
		if gaettet[i] != "tom":
			continue
		if farvegaet[i] in randomList:
			gaettet[i] = "hvid"
	logging.debug('find korrekt farve:{}'.format(gaettet))
	print ("Her er følgende svar for dit gæt:{}".format(",".join(gaettet)))

def vis_svar_sorteret(farvegaet, randomList):
	gaettet = ["tom"]*4		#tom=farve og pos ikke gættet rigtigt; sort=farve og pos gættet rigtigt; hvid=farve gættet rigtigt
	#find korrekt farve og pos
	for i in range(len(farvegaet)):
		if farvegaet[i] == randomList[i]:
			gaettet[i] = "sort"
	logging.debug('find korrekt farve og pos:{}'.format(gaettet))
	#find korrekt farve
	for i in range(len(farvegaet)):
		if gaettet[i] != "tom":
			continue
		if farvegaet[i] in randomList:
			gaettet[i] = "hvid"
	logging.debug('find korrekt farve og pos:{}'.format(gaettet))
	print ("Her er følgende svar for dit gæt:", end="")
	#vis svar i 
	#vis korrekt farve og pos
	for gaet in gaettet:
		if gaet == "sort":
			print ("sort,", end="")
	#vis korrekt farve og pos
	for gaet in gaettet:
		if gaet == "hvid":
			print ("hvid,", end="")
	print ("")

def vis_korrekt_svar(farvegaet, randomList):
	print ("Du gættede forkert!")
	print ("Dit gæt var følgende:{}".format(",".join(farvegaet)))
	print ("Det rigtige svar var følgende:{}".format(",".join(randomList)))


#Main 
colorList = ["gul", "rød", "grøn", "blå", "orange", "sort", "hvid", "pink"]
antal_gaet = 2
print("---\nMasterMind\nAlslug-Python-Gruppen\n---\n")
print("----")

print("Farverne i MasterMind er:{}".format(",".join(colorList)), end="\n\n")
print("Du har {} gæt!!!".format(antal_gaet), end="\n\n")

#farvegaet = [""]*4
farvegaet = ["sort", "gul", "grøn", "pink"]
randomList = [""]*4
generer_farver_1gang(randomList)
print ("De tilfældige tal er følgende:{}".format(",".join(randomList)), end="\n\n")

for gaet_nr in range (1, antal_gaet + 1):
	logging.debug('gæt nr:{}'.format(gaet_nr))
	farvegaet = gaet_input(farvegaet, gaet_nr)
	logging.debug('svar farve:{}'.format(farvegaet))
	if farvegaet == randomList:
		print("Du gættede rigtigt")
		break
	else:
#		vis_svar_pos(farvegaet, randomList)
		vis_svar_sorteret(farvegaet, randomList)
#		print("værdierne er ikke ens")

if farvegaet != randomList:
	vis_korrekt_svar(farvegaet, randomList)

logging.debug('End of program')

