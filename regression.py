import random
random.seed(5)
n=10
x = [random.uniform(1,100) for i in range(n)]
y = [random.uniform(1,300) for i in range(n)]

sumy = sum(y)
sumx = sum(x)
x2 = [i**2 for i in x]
y2 = [i**2 for i in y]
sumy2 = sum(y2)
sumx2 = sum(x2)
xy = [i*j for i,j in zip(x,y)]
sumxy = sum(xy) 
a = (sumy*sumx2 - sumx*sumxy)/(n*sumx2 - sumx**2)
b = (n*sumxy - sumx*sumy)/(n*sumx2 - sumx**2)
print("The equation is y = a + bx")
print("a : ",a)
print("b : ",b)
