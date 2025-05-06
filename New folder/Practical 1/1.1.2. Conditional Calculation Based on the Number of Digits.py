n=int(input())
if(n>0 and n<10):
	print(n*n)
elif(n<100):
	a=n**0.5
	print('%.2f'%a)
elif(n<1000):
	a=n**(1/3)
	print('%.2f'%a)
elif(n>=1000):
	print("Invalid")