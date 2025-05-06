import numpy as np
def create_array():
	r,c = map(int,input().split())
	lst = []
	for i in range(r):
		row_list = list(map(int,input().split()))
		lst.extend(row_list)
	a=np.array(lst).reshape(r,c)
	return a

arr=create_array()
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)