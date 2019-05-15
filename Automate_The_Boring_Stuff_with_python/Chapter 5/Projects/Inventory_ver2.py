#!/usr/bin/python3

def addToInventory(inventory, loot):
	for item in loot:
		if item in inventory.keys():
			inventory[item] += 1
		else:
			inventory[item] = 1
	return inventory
		
def displayInventory(inventory):
	items_total = 0
	print("Inventory:")
	for key, value in inventory.items():
		print ("%d %s" % (value, key))
		items_total += value
	print ("Total number of items: %d" % items_total)

Player1Inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Player1Inventory = addToInventory(Player1Inventory, dragonLoot)

displayInventory(Player1Inventory)


'''
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
'''

