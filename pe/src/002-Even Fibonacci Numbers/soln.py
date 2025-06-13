n = 4000000
a = 1
b = 2
summ = 0
for i in range(0,n):
    if(a>4000000):
        break
    else:
        if(a%2 == 0):
            summ += a
        temp = b
        b = a+b
        a = temp

print(summ)

#0 # 1 2 
#1 # 2 3
#2 # 3 5
