n = 100

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

j = str(factorial(100))


sum = 0
for k in j:
    sum += int(k)

print(sum)

