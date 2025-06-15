lis = []
for i in range (5):
    row= list(map(int, input().split()))
    lis.append(row)
cord = []
for j in range(5):
    for k in range (5):
        if(lis[j][k]==1):
            cord = [j, k]
            break
        else:
            continue

ans = abs(cord[0]-2) + abs(cord[1]-2)
print(ans)
