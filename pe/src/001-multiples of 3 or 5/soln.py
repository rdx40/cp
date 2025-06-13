def sum_n(n, a):
    m = (n - 1) // a
    return a * m * (m + 1) // 2

print(sum_n(1000, 3) + sum_n(1000, 5) - sum_n(1000, 15))

