# -*- coding: utf-8 -*-

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x == y)
print(x == z)

print(x is z)      # The 'is' operator compares addresses in memory
print(x is y)

a = ['apple', 'banana']
print('banana' in a) # Checks for string presence; for array elements, it must be written exactly the same.

name = 'john'        # For a variable, it can search within the string; must be written exactly the same.
print('jo' in name)