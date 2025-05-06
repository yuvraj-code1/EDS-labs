# write the code..
lst=[]
while(True):
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	ch=int(input("Enter choice: "))
	if ch==1:
		ele=input("Integer: ")
		if ele.isdigit():
			ele=int(ele)
			lst.append(ele)
			print("List after adding:",lst)
		else:
			print("Invalid input")
	if ch==2:
		if lst:
			integer=int(input("Integer: "))
			if integer in lst:
				lst.remove(integer)
				print("List after removing:",lst)
			else :
				print("Element not found")
		else:
			print("List is empty")
	if ch==3:
		if lst:
			print(lst)
		else:
			print("List is empty")
	if ch==4:
		break
	elif ch>=4:
		print("Invalid choice")