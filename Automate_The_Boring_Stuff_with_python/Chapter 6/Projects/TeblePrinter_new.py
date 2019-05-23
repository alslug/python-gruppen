#!/usr/bin/python3

def printTable(tableData):
	noItemsInTableData = len(tableData)						#Get length og list tableData
#	print ("lengthOfTableData %d" % lengthOfTableData)
	noItemsInListData = len(tableData[0])					#Get length og list in tableData
#	print ("noItemsInListData %d" % noItemsInListData)
	colWidth = [0] * len(tableData)							#make a colWith list
#	print(tableData)
	for i in range(noItemsInTableData):						#find max text length for each column
		for j in range(noItemsInListData):
#			print ("%s %d" % (tableData[i][j], len(tableData[i][j])))
			if colWidth[i] < len(tableData[i][j]):
				colWidth[i] = len(tableData[i][j])
#			print (colWidth)
#	print(tableData)
	for i in range(noItemsInListData):						#print out each list in a colum
		for j in range(noItemsInTableData):
			print(("{0:>" + str(colWidth[j] + 1) + "}").format(tableData[j][i]), end = "")
		print() 

		
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
