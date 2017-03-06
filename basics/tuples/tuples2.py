'''
Created on Mar 5, 2017

@author: Hunter
'''
import sys

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

print("List size =", sys.getsizeof(list_eg))
print("Tuple size =", sys.getsizeof(tuple_eg))

# Lists:
# Add data, remove data, change data

# Tuples:
# Cannot be changed, "Immutable", made quickly