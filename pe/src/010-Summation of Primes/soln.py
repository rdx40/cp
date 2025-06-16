def isPrime(n):
    if n <= 1 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def sumPrime(n):
    sum1 = 0
    for i in range(2, n + 1):
        if isPrime(i):
            sum1 += i
    print(sum1)

n = 2000000
sumPrime(n)

