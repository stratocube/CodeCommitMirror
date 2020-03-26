from math import sqrt

a = sqrt(2)
b = 1

while a != b:
    b = (a+b)/2
    a = sqrt(b*a)

print(4/a)