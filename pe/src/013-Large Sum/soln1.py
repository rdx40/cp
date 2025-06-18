with open("input.txt", "r") as file:
    data = file.read().splitlines()
sum1 = 0
for d in data:
    sum1 += int(d)
sum2 = str(sum1)
print(sum2[:10])
