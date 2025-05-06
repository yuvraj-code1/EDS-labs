n=int(input())
marks=list(map(int,input().split()))
if any(mark<40 for mark in marks):
	print("Fail")
else:
	total=sum(marks)
	per=total/n
	print("Aggregate Percentage:",'%.2f'%per)
	if(per>75):
		print("Grade: Distinction")
	elif(per>=60):
		print("Grade: First Division")
	elif(per>=50):
		print("Grade: Second Division")
	elif(per>=40):
		print("Grade: Third Division")
	else:
		print("Fail")
