import math
inp = [8,10,15,20]

#min-max normalization
inpmin = min(inp)
inpmax = max(inp)
newmin = 0
newmax = 1

normalized = []
for i in inp:
	value = ((i - inpmin)/(inpmax - inpmin))*(newmax - newmin) + newmin
	normalized.append(round(value,2))

print("Using min-max normalization : " + str(normalized))

#z-score normalization
inpmean = sum(inp)/len(inp)
stddev = 0
for i in inp:
	stddev += (i-inpmean)**2
stddev = round(math.sqrt(stddev/len(inp)),2)

z_score = []
for i in inp:
	z_score.append(round((i-inpmean)/stddev,2))
print("Using z-score normalization : " + str(z_score))
#print(stddev)

#decimal scaling normalization
div = 10**len(str(inpmax))
decimalscaling = []
for i in inp:
	decimalscaling.append(round(i/div,2))
print("Using decimalscaling normalization : " + str(decimalscaling))