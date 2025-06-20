n = int(input())

lis = []

for i in range(n):
    lis.append(input())

groups = 1 
for i in range(1, len(lis)):
    if lis[i] != lis[i - 1]:
        groups += 1

print(groups)

