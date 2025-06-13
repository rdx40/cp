n = 4000000
a = 2
b = 8
summ = a

while b < n:
    summ += b
    a, b = b, 4*b+a

print(summ)
