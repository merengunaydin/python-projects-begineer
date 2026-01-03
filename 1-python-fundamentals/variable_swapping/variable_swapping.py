# -*- coding: utf-8 -*-

x = 10
y = 5

print(x, y)

x, y = y, x

print(x, y) # swapping numbers

values = 1, 2, 3, 4, 5  # creating a tuple

a, b, *c = values

print(a, b, c)  # c becomes a three-element list