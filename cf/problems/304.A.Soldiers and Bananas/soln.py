k, n, w = map(int, input().split())

cost = 0
for i in range(w):
    cost += (i+1)*k
print(cost - n)
