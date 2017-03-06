'''
Created on Mar 5, 2017

@author: Hunter
'''

empty_tuple = ()
test1 = ("a",) # Must include a comma for single element tuple or else result is a String!
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1)
print(test2)
print(test3)

# Tuples do not need parenthesis to create:

test4 = 1,
test5 = 1, 2
test6 = 1, 2, 3

print(type(test4))
print(type(test5))
print(type(test6))