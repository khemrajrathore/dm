import math
print("Enter x values:");
x = list(map(float,raw_input().split()))
print("Enter y values:")
y = list(map(float,raw_input().split()))
x_sum = sum(x)
x_sq = 0
for i in x:
	x_sq+=(i**2)
y_sum = sum(y)
y_sq = 0
for i in y:
	y_sq+=(i**2)
xy = 0
for i in range(len(x)):
	xy+=x[i]*y[i]
r = ((len(x)*xy)-(x_sum*y_sum))/(math.sqrt((len(x)*x_sq)-(x_sum**2))*math.sqrt((len(y)*y_sq)-(y_sum**2)))
r  = round(r,2)
print("regression coefficient: "+str(r))
