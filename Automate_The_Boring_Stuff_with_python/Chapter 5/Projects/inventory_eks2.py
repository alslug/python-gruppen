# inventory.py

def displayInventory (inventar):
    print ( "Beholdning:")
    item_total = 0
    for k, v in inventar.items():
        print("%d\t%s" % (v, k))
        item_total += v
    print ("\nSamlet antal elementer:" + str(item_total))

def addToInventory (inventar, addedItems):
    for item in addedItems:
        if item in inventar.keys():
            inventar[item] += 1     #Her lægges en til den eksistenrende nøgle
        else:
            inventar[item] = 1      #Her oprettes en ny nøgle med 1
#        print (item)
	# Din kode skrives her
#    return inventar

inv = {'guldmønter': 42, 'reb': 1}
dragonLoot = ['guldmønter', 'dolk', 'guldmønter', 'guldmønter', 'rubin']

displayInventory (inv)
print (dragonLoot)
#inv = addToInventory (inv, dragonLoot)
addToInventory (inv, dragonLoot)
displayInventory (inv)


'''
Beholdning:
12 pil
42 guldmønter
1 reb
6 fakkel
1 dolk
Samlet antal genstande: 62
'''
