n = input()

for i in range(int(n)+1, int(n)+1000, 1):
    if(len(set(str(i))) == 4):
       print(i)
       break

