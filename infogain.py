import random
import math
import pandas as pd

def entropy(a,b):
	sumab = a+b
	a  = round(a/(sumab),2)
	b  = round(b/(sumab),2)
	if(a == 0 or b == 0):
		return 0
	print("a,b",a,b)
	return (-(a*math.log(a,2))-(b*math.log(b,2))) 


data = pd.read_csv("infogain.csv")
n = len(data)

"""random.seed(10)

outlook = [random.randint(0,2) for i in range(n)]
temp = [random.randint(0,2) for i in range(n)]
humidity = [random.randint(0,1) for i in range(n)]
windy = [random.randint(0,1) for i in range(n)]
play_golf = [random.randint(0,1) for i in range(n)]"""

outlook = list(data["outlook"])
temp = list(data["temp"])
humidity = list(data["humidity"])
windy = list(data["windy"])
play_golf = list(data["playgolf"])

print("Outlook Temp Humidity Windy Play_Golf")
for i in range(n):
	print(str(outlook[i])+"   "+ str(temp[i]) +"   "+ str(humidity[i]) +"    " +str(windy[i]) +"   "+ str(play_golf[i]))

yes = 0
for i in range(len(data)):
	if(str(data.loc[i,"playgolf"]) == "yes"):
		yes += 1  
	#print(data.loc[i,"playgolf"])
no = n - yes
print(yes,no)
ent = {}
ent["play_golf"] = entropy(yes,no)

cntsunny  = 0
cntovercast = 0
cntrainy = 0
sunnyyes = 0
overcastyes = 0
rainyyes = 0

for i in range(n):
	if(outlook[i] == "sunny"):
		cntsunny+=1
	elif(outlook[i] == "overcast"):
		cntovercast+=1	
	else:
		cntrainy+=1
for i in range(n):
	if(outlook[i] == "sunny" and play_golf[i] == "yes"):
		sunnyyes+=1
	elif(outlook[i] == "overcast" and play_golf[i] == "yes"):
		overcastyes+=1
	if(outlook[i] == "rainy" and play_golf[i] == "yes"):
		rainyyes+=1
ent["play_golf_outlook"] = (cntsunny/n)*entropy(sunnyyes,cntsunny-sunnyyes) + (cntovercast/n)*entropy(overcastyes,cntovercast-overcastyes) + (cntrainy/n)*entropy(rainyyes,cntrainy-rainyyes)

infogain = ent["play_golf"] - ent["play_golf_outlook"]
print(ent,infogain)
	

