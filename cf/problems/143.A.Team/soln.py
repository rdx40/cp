n = int(input()) #rows
m = 3 #cols
matrix = [];

for i in range(n):
    row = []
    for j in range(3):
        ele = int(input())
        row.append(ele)
    matrix.append(row)

cnt = 0
for i in range(n):
    if(matrix[i].count(1))>=2:
        #if(list.count(1)>=2):
        cnt += 1

print(cnt)

