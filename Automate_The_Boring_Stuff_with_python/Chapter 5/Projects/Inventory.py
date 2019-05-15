#!/usr/bin/python3

def displayInventory(inventory):
	items_total = 0
	print("Inventory:")
	for key, value in inventory.items():
		print ("%d %s" % (value, key))
		items_total += value
	print ("Total number of items: %d" % items_total)
		

Player1Inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Player2Inventory = {'rope': 5, 'torch': 2, 'gold coin': 142, 'dagger': 3, 'arrow': 24}
displayInventory(Player1Inventory)
displayInventory(Player2Inventory)

'''
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
'''
