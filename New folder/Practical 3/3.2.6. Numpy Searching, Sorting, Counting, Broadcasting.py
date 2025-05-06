import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
s=np.where(array1==search_value)
print(s[0])
# Count occurrences in array1
c=np.count_nonzero(array1==count_value)
print(c)
# Broadcasting addition
print(array1+ broadcast_value)
# Sort the first array
print(np.sort(array1))

#nanargmax()
#nanargmin()