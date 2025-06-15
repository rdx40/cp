n = 100
sum1 = 0
for i in range(n):
    sum1 += (i+1)**2
sqr_sum = (n*(n+1)//2)**2
print(sqr_sum - sum1)
