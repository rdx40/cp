n, m = map(int, input().split())

lis = list(map(int, input().split()))
cnt = 0

# Adjust for 1-based index in the problem
for i in range(n):
    if lis[i] >= lis[m - 1] and lis[i]>0:
        cnt += 1

print(cnt)

