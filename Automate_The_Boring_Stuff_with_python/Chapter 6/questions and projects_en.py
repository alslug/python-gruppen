Practice Questions
Q: 1. What are escape characters?
	escape character lader dig indsætte characterer som ellers vil være umulige at indsætte
	
Q: 2. What do the \n and \t escape characters represent?
	\n is newline
	\t is tabulator
	
Q: 3. How can you put a \ backslash character in a string?
	by inserting \\
	test = "Dette er enten\\eller"

Q: 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
	Fordi at strengen er indrammet med anførselstegen.
	
Q: 5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
	med tre dobbelte abostroffer strenge
	tekst = '''Dette
	er en
	tekst'''

Q: 6. What do the following expressions evaluate to?
'Hello world!'[1]
'Hello world!'[0:5]
'Hello world!'[:5]
'Hello world!'[3:]
	'Hello world!'[1] => 'e'
	'Hello world!'[0:5] => 'Hello'
	'Hello world!'[:5] => 'Hello'
	'Hello world!'[3:] 'lo world!'

Q: 7. What do the following expressions evaluate to?
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
	'Hello'.upper() => 'HELLO'
	'Hello'.upper().isupper() => True
	'Hello'.upper().lower() => 'hello'
	
Q: 8. What do the following expressions evaluate to?
'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())
	>>> 'Remember, remember, the fifth of November.'.split()
	['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
	>>> '-'.join('There can be only one.'.split())
	There-can-be-only-one.
	
Q: 9. What string methods can you use to right-justify, left-justify, and center a string?
	ljust(), rjust() and center()
	
Q: 10. How can you trim whitespace characters from the beginning or end of a string?
	fjerne tomme karakterer fra begyndelsen
	lstrip()
	fjerne tomme karakterer fra slutningen
	rstrip()

Practice Projects
For practice, write a program that does the following.

Table Printer
Write a function named printTable() that takes a list of lists of strings and displays
it in a well-organized table with each column right-justified. Assume that all the
inner lists will contain the same number of strings. For example, the value could
look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:
apples Alice dogs
oranges Bob cats
cherries Carol moose
banana David goose
Hint: Your code will first have to find the longest string in each of the inner lists so
that the whole column can be wide enough to fit all the strings. You can store the
maximum width of each column as a list of integers. The printTable() function can
begin with colWidths = [0] * len(tableData), which will create a list containing the
same number of 0 values as the number of inner lists in tableData. That way,
colWidths[0] can store the width of the longest string in tableData[0], colWidths[1]
can store the width of the longest string in tableData[1], and so on. You can then
find the largest value in the colWidths list to find out what integer width to pass to
the rjust() string method.