limit = 4000000
a, b = 1, 2
summ = 0

while a < limit:
    if a % 2 == 0:
        summ += a
    a, b = b, a + b

print(summ)
