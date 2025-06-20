op = 0
sol = 0
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    op = op + b - a
    if op > sol:
        sol = op
print(sol)

