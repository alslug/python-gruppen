#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - deletes the keyword.
#        py.exe mcb.pyw delete - Deletes all keywords.

import shelve, pyperclip, sys, os

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
# List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
elif sys.argv[1].lower() == 'delete':
	if len(sys.argv) == 3:
		if sys.argv[2] in mcbShelf:
			del mcbShelf[sys.argv[2]]
	if len(sys.argv) == 2:
		for index, keyword in enumerate(mcbShelf):
			del mcbShelf[index]

mcbShelf.close()
