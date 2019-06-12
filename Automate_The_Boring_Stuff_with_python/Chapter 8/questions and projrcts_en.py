Practice Question
Q: 1. What is a relative path relative to?
	which is relative to the program’s current working directory
	
Q: 2. What does an absolute path start with?
	which always begins with the root folder
	
Q: 3. What do the os.getcwd() and os.chdir() functions do?
	os.getcwd() #gets the current dir
	os.chdir() #changes to a directory of your wish
	
Q: 4. What are the . and .. folders?
	. is the current folder
	.. is the parrent folder

Q: 5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
	C:\bacon\eggs\		spam.txt
		Dir name		base name

Q: 6. What are the three “mode” arguments that can be passed to the open() function?
	r = read, w = write, a = append

Q: 7. What happens if an existing file is opened in write mode?
Write mode will overwrite the existing file and start from scratch, just like when you overwrite a variable’s value with a new value

Q: 8. What is the difference between the read() and readlines() methods?
	read = read in their contents as one large string (with the read() method
	readlines = as a list of strings (with the readlines() method)

Q: 9. What data structure does a shelf value resemble?
	You can save variables in your Python programs to binary shelf files using the shelve module

Practice Projects
For practice, design and write the following programs.

Extending Multiclipboard
Extend the multiclipboard program in this chapter so that it has a delete <keyword>
command line argument that will delete a keyword from the shelf. Then add a
delete command line argument that will delete all keywords.

Mad Libs
Create a Mad Libs program that reads in text files and lets the user add their own
text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the
text file. For example, a text file may look like this:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to replace them.
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
The following text file would then be created:
The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
The results should be printed to the screen and saved to a new text file.

Rexex Search
Write a program that opens all .txt files in a folder and searches for any line that
matches a user-supplied regular expression. The results should be printed to the
screen.