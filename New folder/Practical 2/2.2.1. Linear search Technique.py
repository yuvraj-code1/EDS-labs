list1=list(map(int,input().split()))
skey=int(input())

f=0
for i in range(len(list1)):
	if list1[i]==skey:
		f=1
		print(i)
		break
if(f==0):
	print("Not found")


















"""
e=input()
list=e.split()
list1=[]

for e in list:
	list1.append(int(e))
skey=int(input())

f=0
for i in range(len(list1)):
	if(list1[i]==skey):
		print(i)
		f = 1
		break

if(f==0):
	print("Not found")
	"""