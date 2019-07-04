#!/usr/bin/python3
#MasterMind-20190703pel

import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def generer_farver(randomList):
    for i in range(4):
        randomList[i] = colorList[random.randint(0, 7)]
    logging.debug('random list:{}'.format(randomList))

def gaet_input(farvegaet):
    print("indtast farverne adskilt med komma eks: sort,gul,grøn,pink")
    farvegaet = input().lower().split(",")
#    for felt_no in range(4):
#        print("Feltnr:{}".format(felt_no + 1))
#        farvegaet[felt_no] = input("Farve:")
    logging.debug('svar farve:{}'.format(farvegaet))
    return farvegaet
 
colorList = ["gul", "rød", "grøn", "blå", "orange", "sort", "hvid", "pink"]
print("---\nMasterMind\nAlslug-Python-Gruppen\n---\n")
print("----")

print("Farverne i MasterMind er:")
print(colorList)
print("\nDu har 20/tyve gæt!!!\n")

farvegaet = [""]*4
randomList = [""]*4
generer_farver(randomList)

for gaet_nr in range (1, 3):
    logging.debug('gæt nr:{}'.format(gaet_nr))
    farvegaet = gaet_input(farvegaet)
    logging.debug('svar farve:{}'.format(farvegaet))
    if farvegaet == randomList:
        print("værdierne er ens")
        break
    else:
        print("værdierne er ikke ens")
    
'''
    felt_no = 0
    while felt_no < 3:
            if felt_no == 3:
                break
            print("Feltnr:{}".format(felt_no + 1))
            farvegaet[felt_no] = input("Farve:")
            logging.debug('retur farve:{}'.format(farvegaet[felt_no]))
            felt_no += 1

    guess = 0
    rigtig = 0
    while guess < 3:
            if randomList[guess] == farveguess[guess]:
                rigtig += 1
                if rigtig == 3:
                    print("Du har vundet!")
                    break
    gaet_nr += 1
				
  		

if gaet_nr > 20:
    print("Du har tabt")
'''

logging.debug('End of program')

