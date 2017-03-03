# Python Object-Oriented Programming: Class Methods and Static Methods
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    #This creates a method that affects the entire class; the class instance variable (labeled 'cls') is
    #passed automatically
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_01 = Employee('Corey', 'Schafer', 50000)
emp_02 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)
emp_01.raise_amt = 1.06

print(Employee.raise_amt)
print(emp_01.raise_amt)
print(emp_02.raise_amt)

print()

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_1.pay)

print(new_emp_2.email)
print(new_emp_2.pay)

print(new_emp_3.email)
print(new_emp_3.pay)

import datetime
my_date = datetime.date(2016, 12, 18)

print(Employee.is_workday(my_date))