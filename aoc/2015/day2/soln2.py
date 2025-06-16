with open("input.txt", "r") as file:
    data = file.read().splitlines()
tot_rib = 0
for d in data:
   a,b,c = map(int , d.split('x'))
   smallest_peri = 2*(a+b+c - max(a,b,c))
   bow = a*b*c
   tot_rib += smallest_peri + bow
print(tot_rib)