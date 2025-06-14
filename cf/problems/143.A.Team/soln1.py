n = int(input()) #rows
m = 3 #cols
matrix = [];

for i in range(n):
    #row = input().split() # makes it str from int
    row = list(map(int, input().split()))
    matrix.append(row)

cnt = 0
for i in range(n):
    if(matrix[i].count(1))>=2:
        #if(list.count(1)>=2):
        cnt += 1

print(cnt)

