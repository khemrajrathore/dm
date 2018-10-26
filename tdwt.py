import pandas as pd

data = pd.read_csv("tdwt.csv")
print(data.head())

locationset = set(data["location"])
#print(locationset)

locationdict = {}
for i in locationset:
	locationdict[i] = 0

for i,j in zip(data["location"],range(len(data))):
	locationdict[i] += data.loc[j,"count"]


#calculating tv twt and comp twt
tv_twt = {}
for i in range(len(locationdict)):
	tv_twt[str(data.loc[i,"location"])] = data.loc[i,"count"]/locationdict[str(data.loc[i,"location"])]

comp_twt = {}
for i in range(len(locationdict),len(data)):
	comp_twt[str(data.loc[i,"location"])] = data.loc[i,"count"]/locationdict[str(data.loc[i,"location"])]


tvsum, compsum = 0, 0
for i in range(len(data)):
	if(data.loc[i,"item"]=="TV"):
		tvsum += data.loc[i,"count"]
	else:
		compsum += data.loc[i,"count"]

#calculating tv dwt and comp dwt
tv_dwt = {}
for i in range(len(locationdict)):
	tv_dwt[str(data.loc[i,"location"])] = data.loc[i,"count"]/tvsum

comp_dwt = {}
for i in range(len(locationdict),len(data)):
	comp_dwt[str(data.loc[i,"location"])] = data.loc[i,"count"]/compsum


#print(tvsum,compsum)
print("twt")
print("tv ",tv_twt,"comp ",comp_twt)
print("dwt")
print("tv ",tv_dwt,"comp ",comp_dwt)
#print(locationdict)

