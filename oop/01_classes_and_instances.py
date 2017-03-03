# Python Object-Oriented Programming: Classes and Instances


class Employee:
    # This is the constructor method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# Initializing objects; sets variable name to self
emp_01 = Employee('Corey', 'Schafer', 50000)
emp_02 = Employee('Test', 'User', 60000)

#print(emp_01)
#print(emp_02)

print(emp_01.email)
print(emp_02.email)

# These lines do the same thing!  The first one requires the instance variable, whereas the second one uses self!
print(Employee.fullname(emp_02))
print(emp_02.fullname())