
import datetime
def calculate_age(birthdate):
	birthdate=datetime.datetime.strptime(birthdate,"%d-%m-%Y")
	today=datetime.date.today()
	age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
	return age
	
	

def convert_salary_to_dollars(salary_in_rupees):
	return 0.012*salary_in_rupees
    
birthdate = input()
salary_in_rupees = float(input())
age = calculate_age(birthdate)
salary_in_dollars = convert_salary_to_dollars(salary_in_rupees)
print(f"Age: {age}")
print(f"Salary in dollars: {salary_in_dollars:.2f}")
 