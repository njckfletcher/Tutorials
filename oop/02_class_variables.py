# Python Object-Oriented Programming: Class Variables
class Employee:
    #These are a class variable
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        #Here, the class variable describing the number of employees is incremented every time the init method runs
        #as the init method runs every time an instance is created.  This is good use of changing the class variable
        #for the entire class rather than self (which only changes that instance)
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

        #This example would change the entire class variable, whereas the above example makes it specific to the instance
        #self.pay = int(self.pay * Employee.raise_amt)


emp_01 = Employee('Corey', 'Schafer', 50000)
emp_02 = Employee('Test', 'User', 60000)

#print(emp_01.__dict__)
#print(Employee.__dict__)

#This changes the entire class variable
#Employee.raise_amt = 1.05

emp_01.raise_amt = 1.05
print(emp_01.__dict__)

print(Employee.raise_amt)
print(emp_01.raise_amt)
print(emp_02.raise_amt)

print("There are " + str(Employee.num_of_emps) + " employees")