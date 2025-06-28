def count_divisors(n):
    count = 0
    root = int(n**0.5)
    for i in range(1, root + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

def n_divisors(limit):
    n = 1
    triangle = 1
    while True:
        if count_divisors(triangle) > limit:
            return triangle
        n += 1
        triangle += n

print(n_divisors(500))
