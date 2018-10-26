n = 3 #no of bins
inp = [3,7,8,13,22,22,26,22,26,28,30,37] #data on which to perform binning

inp.sort()
bins = []
lenghtofbin = len(inp)//n

for i in range(n):
	tmp = []
	for j in range(lenghtofbin):
		tmp.append(inp[i*lenghtofbin+j])

	bins.append(tmp)
print("Binning by equal frequency : ")
for i in bins:
	print(i)

print("\nBinning by bin means : ")
binmean = []
for i in range(n):
	binmean.append(sum(bins[i])/lenghtofbin)
	print(str(str(binmean[i])+str(" "))*lenghtofbin)

print('\nBinning by bin boundary :')
for i in range(n):
	for j in range(lenghtofbin):
		if(binmean[i] >= bins[i][j]):
			print(bins[i][0],end=" ")
		else:
			print(bins[i][lenghtofbin-1],end=" ")

	print("\n");


