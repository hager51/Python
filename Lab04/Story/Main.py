from Classes import Emp, Office, Car
print("\n\n")

Emp1 = Emp("Ali", 2000, "happy", 70, 1, "Hyundai Venue", "ali@gmail.com", 3500, 15)
Emp2 = Emp("Ahmed", 1000, "tired", 50, 2, "Bajaj Qute", "ahmed@gmail.com", 3100, 25)
Emp3 = Emp("Eman", 1300, "happy", 100, 3, "Datsun Redi GO", "eman@gmail.com", 3700, 27)
Emp4 = Emp("Samy", 2220, "happy", 80, 5, "Fiat 128", "Samy@gmail.com", 2100, 20)
Off1 = Office("ITI")
C1 = Car("Datsun Redi GO", 100, 150)

#Check Employee Class Methods
Off1.get_employee(Emp1.id)
Emp1.sleep(8)
Emp1.eat(2)
Emp1.buy(5)
Off1.get_employee(Emp1.id)
Emp1.work(9)
Off1.get_employee(Emp1.id)

Emp2.send_mail("tuqa@gmsil.com", "test", "How are you?", "tuqa")

#Check Employee Class with Car Class Methods
Emp4.refuel(80)
Emp4.drive(15, 8)

#Check Office Class Methods
print("Getting All Employees .....\n")
Off1.get_all_employees()

print("Gettting Only One Employee Using ID .....\n")
Off1.get_employee(5)

print("Hiring New Employee .....\n")
Off1.hire(Emp("Hager", 1250, "lazy", 85, 4, "Swift", "hager@gmail.com", 3000, 18))
Off1.get_all_employees()
Off1.get_employee(4)

print("Firing Employee .....\n")
Off1.fire(4)
Off1.get_all_employees()
Off1.get_employee(4)

print("Salary before deduct = ", Emp1.salary)
Off1.get_employee(1)
Emp1 = Off1.deduct(1, 200)
print("Salary before deduct = ", Emp1.salary)
Off1.get_employee(1)

print("Salary before reward = ", Emp2.salary)
Off1.get_employee(2)
Emp2 = Off1.reward(2, 100)
print("Salary before reaward = ", Emp2.salary)
Off1.get_employee(2)

print("Checking Lateness of Employee .....\n")
print("Employee", Emp3.name, "is", Off1.check_lateness(Emp3.id, 8.50))


import json

my_details = {
    'Office Name': Off1.name,
    'Employees' : Off1.Employees
}

with open('Data.json', 'w') as json_file:
    json.dump(my_details, json_file)
