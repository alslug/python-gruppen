# inventory.py
stuff = {'reb': 1, 'fakkel': 6, 'guldmønter': 42, 'dolk': 1, 'pil': 12}

def displayInventory (inventar):
    print ( "Beholdning:")
    item_total = 0
    for k, v in inventar.items():
        print("%d\t%s" % (v, k))
        item_total += v
    print ("\nSamlet antal elementer:" + str(item_total))

displayInventory (stuff)


'''
Beholdning:
12 pil
42 guldmønter
1 reb
6 fakkel
1 dolk
Samlet antal genstande: 62
'''
