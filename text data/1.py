l=[]
f = open('Hello.txt', 'r')
for word in f:
	s=word 
words=s.split()
set_a=set(words)
print("Dictionary:")
print(set_a)
print("Enter the substring with proper case to find:")
n=input()
if n in set_a:
	for a in set_a:
		if a == n :
			print("1",end="")
		else:
			print("0",end="")
	print()
else:
	print("Word is not present in text file")
