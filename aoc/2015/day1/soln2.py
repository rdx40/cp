with open("input.txt", "r") as file:
    data = file.read().strip()
floor = 0
for i in range (len(data)):
    if data[i] == ')':
        floor -= 1
    else:
        floor += 1
    if floor == -1:
        print(i+1) #indxing from 0
        break

