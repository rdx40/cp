n = int(input())
ans = 0 
while (n>0):
    test = input()
    if(test[1] == '+'):
        ans += 1
    else:
        ans -= 1
    n -= 1

print(ans)

