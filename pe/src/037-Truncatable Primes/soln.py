def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    for i in range(len(s)):
        if not is_prime(int(s[:len(s)-i])):
            return False
    return True
found = []
num = 11

while len(found) < 11:
    if is_prime(num) and is_truncatable_prime(num):
        found.append(num)
    num += 2
print(sum(found))

