import csv
data = []
no_of_dept = 0
no_of_class = 0
no_of_result = 0

def csv_reader(fobj):
	reader = csv.DictReader(fobj)
	for line in reader:
		data.append(line)

	dept = []
	clas = []
	result = []
	for itm in data:
		dept.append(itm["dept"])
		clas.append(itm["class"])
		result.append(itm["result"])

	#calculate no of distinct entries in each column
	no_of_dept = len(set(dept))	
	no_of_class = len(set(clas))
	no_of_result = len(set(result))
	#confirm the index for each entry of column like 'IT' has index 1 in dept
	dept = list(set(dept))
	clas = list(set(clas))
	result = list(set(result))

	##generating dict to store index of the values
	deptindex = {}
	classindex = {}
	resultindex = {}
	for i in dept:
		deptindex[i] = dept.index(i)
	#print(deptindex)

	for i in clas:
		classindex[i] = clas.index(i)

	for i in result:
		resultindex[i] = result.index(i)

	#print(resultindex)

	#indexes created successfully till above


	olap = []
	for i in dept:
		temp1 = []
		for j in clas:
			tmp = [0]*no_of_result
			temp1.append(tmp)
		olap.append(temp1)

	#updating olap
	for itm in data:
		deptvalue = itm["dept"]
		classvalue = itm["class"]
		resultvalue = itm["result"]
		#print(str(deptindex))
		#print(dept.index[deptindex])
		olap[deptindex[deptvalue]][classindex[classvalue]][resultindex[resultvalue]]+=1

	displayolap(olap,deptindex,classindex,resultindex)

	print("Enter your query in form of indexes: give -1 if you want aggregation ")
	inp = list(map(int,input().split()))

	finalresult = 0
	for i in range(len(olap)):
		if(inp[0] != i and inp[0] != -1):
			continue
		for j in range(len(olap[i])):
			if(inp[1] != j and inp[1] != -1):
				continue
			for k in range(len(olap[i][j])):
				if(inp[2] != k and inp[2] != -1):
					continue
				finalresult += olap[i][j][k]
				#print(i,j,k)

			


	print("The total count is : "+str(finalresult))
		#print(inp)
	
def displayolap(olap,deptindex,classindex,resultindex):

	print(deptindex)
	print(classindex)
	print(resultindex)

	for i in range(len(olap)):
		for j in range(len(olap[i])):
			for k in range(len(olap[i][j])):
				print(olap[i][j][k],end=" ")
			print("  ")
		print("  ")


	#print(data)

if __name__ == '__main__':
	with open("dmolap.csv") as fobj:
		csv_reader(fobj)