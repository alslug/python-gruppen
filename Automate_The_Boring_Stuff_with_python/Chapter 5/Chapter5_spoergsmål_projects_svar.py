
Q: 1. Hvordan ser koden for en tom ordbog ud?
	Spam = {}

Q: 2. Hvordan ser en ordbog værdi med en nøgle 'foo' og en værdi 42 ud?
	spam = {"foo" : 42} spam = [42]

Q: 3. Hvad er hovedforskellen mellem en ordbog og en liste?
	Forskellen fra lists, ting i dictionaries er ikke sorteret(uordnet), men dictionaries indeholder nøgler som tildeles en værdi 

Q: 4. Hvad sker der, hvis du prøver at få adgang til spam ['foo'], hvis spam er {'bar': 100}?
	Du vil få en "KeyError:"

Q: 5. Hvis en ordbog er gemt i spam, Hvordan er forskellen mellem udtryk 'kat' in spam og 'kat' in spam.keys ()?
	Der er ingen forskel bortset fra at du kan bruge spam.keys() i en for løkke

Q: 6. Hvis en dictonary er gemt i spam, Hvordan er forskellen mellem udtryk 'cat' in spam og 'cat' in spam.values ()?
	>>> spam = {"cat" : "main coon", "animal" : "cat"}
	>>> spam["cat"]
	'main coon'
	>>> spam.values()
	dict_values(['main coon', 'cat'])

Q: 7. Hvad er en genvejen til følgende kode?
hvis 'farve' ikke er i spam:
spam ['color'] = 'sort'
	spam.setdefault('color', 'black')

Q: 8. Hvilket modul og funktion kan bruges til "pretty print" ordbog værdier?
	pprint.pprint()



Praktiske Projects
Til praksis, skriv programmer til at udføre følgende opgaver.

Fantasy Spil Lager
Du laver et fantasy videospil. Modellen for datastrukturen til lageret vil være en dictonary, hvor nøglerne er strengværdier, der beskriver elementet på lageret, og værdien er heltals værdier, der angiver, hvor mange af den pågældende vare spilleren har. For eksempel er ordbogens værdi {'reb': 1, 'fakkel': 6, 'guldmønt ': 42,' dolk ': 1,' pil ': 12} betyder, at afspilleren har 1 reb, 6 fakler, 42 guldmønter og så videre.

Skriv en funktion, der hedder displayInventory(), der gøre det muligt at vise "Lageret" på følgende måde:

Beholdning:
12 pil
42 guldmønter
1 reb
6 fakkel
1 dolk
Samlet antal genstande: 62

Tip: Du kan bruge en for-loop til at køre igennem alle emnerne i en dictonary.

# inventory.py
stuff = {'reb': 1, 'fakkel': 6, 'guldmønter': 42, 'dolk': 1, 'pil': 12}

def displayInventory (inventar):
print ( "Beholdning:")
item_total = 0
for k, v i inventar.items():
	# Skriv din kode her
print ("Samlet antal elementer:" + str(item_total))

displayInventory (stuff)

List to Dictonary funktion for fantasy spil lager
Forestil dig, at en overlevet drage skat er repræsenteret som en liste over strenge som denne:

dragonLoot = ['guldmønter', 'dolk', 'guldmønter', 'guldmønter', 'rubin']

Skriv en funktion med navnet addToInventory (inventar, addedItems), hvor opgørelsen parameter er en dictionary, der repræsenterer spillerens lager (som i det foregående projekt) og parameteren addedItems er en liste ved navn dragonLoot. AddToInventory() funktionen skal returnere en dictonary, der repræsenterer det opdaterede lager. Bemærk at listen over tilføjede emner kan indeholde multipler af samme emne. Din kode kunne se sådan ud:

def addToInventory (inventar, addedItems):
	# Din kode skrives her

inv = {'guldmønter': 42, 'reb': 1}
dragonLoot = ['guldmønter', 'dolk', 'guldmønter', 'guldmønter', 'rubin']
inv = addToInventory (inv, dragonLoot)
displayInventory (inv)

Det foregående program (med din displayInventory () funktion fra det foregående projekt) ville vise følgende:

Beholdning:
45 guldmønter
1 reb
1 rubin
1 dolk
Samlet antal emner: 48