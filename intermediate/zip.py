x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

##for a, b, c in zip(x, y, z):
##    print(a, b, c)

[print(a, b, c) for a, b, c in zip(x, y, z)]
    
print(dict(zip(x, y)))

