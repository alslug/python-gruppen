#!/usr/bin/python3

def printTable(tableData):
	noItemsInTableData = len(tableData)						#Get length og list tableData
	noItemsInListData = len(tableData[0])					#Get length og list in tableData
	colWidth = [0] * len(tableData)							#make a colWith list
	for i in range(noItemsInTableData):						#find max text length for each column
		for j in range(noItemsInListData):
			if colWidth[i] < len(tableData[i][j]):
				colWidth[i] = len(tableData[i][j])
	for i in range(noItemsInListData):						#print out each list in a colum
		print_string = ""
		for j in range(noItemsInTableData):
			print_string += tableData[j][i].rjust(colWidth[j] + 1, " ")
		print(print_string + " ") 

		
tableData = [
['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

'''
Example of output

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''
