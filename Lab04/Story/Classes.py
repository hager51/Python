import re
from Person import Person

class Office():
    Employees = {}
    employeesNum = len(Employees)

    def __init__(self, name):
        self.name = name
    
    def update(self, ID, newSalary):
        E = Emp(self.Employees[ID][0], self.Employees[ID][1], self.Employees[ID][2], self.Employees[ID][3], list(self.Employees.keys())[ID-1], self.Employees[ID][4], self.Employees[ID][5], self.Employees[ID][6], self.Employees[ID][7])
        E.salary = newSalary
        return E

    def get_all_employees(self):
        for k, v in self.Employees.items():
            print("id : ", k, "\tname : ", v[0])
        print("\n")

    def get_employee(self, id):
        f = 1
        for key in self.Employees.keys():
            if id == key:
                f = 0
                break
            else:
                f = 1
        if f == 0:
            print("Employee exist and it's data: " , self.Employees[id], "\n")
        else:
            print("This employee dose not exist\n")

    def hire(self, emp):
        newEmp = Emp(emp.name, emp.money, emp.mood, emp.healthRate
                    , emp.id, emp.car.name, emp.email, emp.salary
                    , emp.distanceToWork)
        Office.Employees.update({newEmp.id : [newEmp.name, newEmp.money, newEmp.mood, newEmp.healthRate, newEmp.car.name, 
                                                newEmp.email, newEmp.salary, newEmp.distanceToWork]})

    def fire(self, empid):
        for key in self.Employees.keys():
            if key == empid:
                del self.Employees[key]
                break

    def deduct(self, empid, deduction):
        for key in self.Employees.keys():
            if key == empid:
                self.Employees[key][6] -= deduction
                break
        return self.update(empid, self.Employees[key][6])

    def reward(self, empid, reward):
        for key in self.Employees.keys():
            if key == empid:
                self.Employees[key][6] += reward
                break
        return self.update(empid, self.Employees[key][6])  

    def check_lateness(self, empid, moveHour):
        if moveHour > 9:
            self.deduct(empid, 10)
            return "late"
        else:
            self.reward(empid, 10)
            return "not late"
    
    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        arrive = moveHour + (distance/velocity) 
        if arrive > targetHour:
            print("Late...!\n")
        else:
            print("Not Late...!\n")

    def change_emps_num(cls, num):
        cls.employeesNum = num
        return cls.employeesNum
        

class Car:
    def __init__(self, name = None, fuelRate = 0, velocity = 0):
        self.name = name
        while True:
            if fuelRate >= 0 and fuelRate <= 100:
                self.fuelRate = fuelRate
                break
            else:
                print("Fuel rate muct be between 0 and 100\n")

        while True:
            if velocity >= 0 and velocity <= 200:
                self.velocity = velocity
                break
            else:
                print("Velocity rate muct be between 0 and 200\n")

    def run(self, v, d, distanceToWork):
        print("Your at beginning fuel rate = ", self.fuelRate, "\n")
        self.fuelRate -= self.fuelRate * (d/1000) * 1/100
        
        while d and self.fuelRate>0:
            if v > 200:
                self.velocity = 200
            else:
                self.velocity = v
            
            d -= self.velocity*5

        if ((distanceToWork - d)/1000)%(distanceToWork/1000) == 0:
            self.stop(1)
        else :
            self.stop(2)
        print("Your Velocity = ", self.velocity, "\n")
        print("Your remaining distance = ", ((distanceToWork - d)/1000)%20, "km\n")
        print("Your fuel rate after arrive = ", self.fuelRate, "\n")
        
    def stop(self, n):
        self.velocity = 0
        if n == 2:
            print("The flue rate become 0 and did not arrive yet\n")
        elif n == 1:
            print("You arrive to your destination\n")


class Emp(Person):
    reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def __init__(self, ename = None, emoney = None, emood = None, ehealthRate = None,
                id = None, car = None, email = None, salary = None, distanceToWork = None):
        super(Emp, self).__init__(ename, emoney, emood, ehealthRate)
    
        self.id = id
        self.car = Car()
        self.car.name = car
        while True:
            if re.fullmatch(self.reg, email):
                self.email = email
                break
            else:
                print("Invalid mail\n")
        while True:
            if salary >= 1000:
                self.salary = salary
                break
            else:
                print("Salary must be 1000 or more\n")
        self.distanceToWork = distanceToWork
        self.update()
    
    def update(self):
        Office.Employees.update({self.id : [self.name, self.money, self.mood, self.healthRate, 
                                            self.car.name, self.email, self.salary, self.distanceToWork]})


    def sleep(self, hours):
        super(Emp, self).sleep(hours)
        self.update()

    
    def buy(self, items):
        super(Emp, self).buy(items)
        self.update()


    def eat(self, meals):
        super(Emp, self).eat(meals)
        self.update()


    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"
        self.update()


    def drive(self, distance, time):
        d = distance*1000
        velocity = (d)/((9-time)*60)
        self.car.run(velocity, d, self.distanceToWork*1000)


    def refuel(self, gasAmount = 100):
        self.car.fuelRate += gasAmount


    def send_mail(self, to, subject, msg, receiver_name):
        file = open("Email_Composer.txt", "a")
        file.write("From: " + self.email + "\n")
        if re.fullmatch(self.reg, to):
            file.write("To: " + to + "\n")  
        else:
            print("Invalid receiver mail")
        file.write("Subj: " + subject + "\n\n")
        file.write("Hi, " + receiver_name + "\n")
        file.write(msg + "\n")
        file.write("\nThanks \n" + self.name)
        file.close()