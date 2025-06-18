a = int(input())
res = input()
Anton = res.count('A')
Danik = abs(a - Anton)

if (Anton > Danik):
    print("Anton")
elif (Danik > Anton):
    print("Danik")
else:
    print("Friendship")
