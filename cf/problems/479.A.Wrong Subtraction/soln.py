a, b = map(int, input().split())

while(b>0):
    if(a % 10 != 0):
        a -= 1
    else:
        a //= 10
    b -= 1

print(a)
