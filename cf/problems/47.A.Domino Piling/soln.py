m, n = map(int, input().split())
total_squares = m * n
# So we can fit total_squares // 2 dominoes
max_dominoes = total_squares // 2
print(max_dominoes)

