import math
print("Enter the numbers to generate 5 point summary")
n = list(map(int,input().split()))
n = list(set(n))
n.sort()
nmin = min(n)
nmax = max(n)
nmedian = math.ceil(len(n)/2) - 1
nq1 = math.ceil(nmedian/2)
nq3 = math.ceil((len(n)-nmedian)/2)-1+nmedian

print("Sorted data ")
print(n)
print("min: " + str(nmin) +"max: "+str(nmax)+"median: "+str(n[int(nmedian)])+"q1: "+str(n[int(nq1)])+"q3: "+str(n[int(nq3)]))

