def is_palindrome(n):
    return str(n) == str(n)[::-1]

mpali = 0

for a in range(999, 99, -1):
    for b in range(a, 99, -1):  # avoid duplicate pairs
        product = a * b
        if product <= mpali:
            break  # no need to check smaller products
        if is_palindrome(product):
            mpali = product
            factors = (a, b)

print(mpali)

