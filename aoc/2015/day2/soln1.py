with open("input.txt", "r") as file:
    data = file.read().splitlines()
sum1 = 0
for d in data:
   a,b,c = map(int , d.split('x'))
   sa = 2*a*b + 2*b*c + 2*a*c
   slck = min(a*b, b*c, c*a)
   sum1 += sa + slck
print(sum1)