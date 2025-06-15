# Open and read the file
with open("input.txt", "r") as file:
    data = file.read().strip()
floor = 0
for _ in data:
    if _ == ')':
        floor -= 1
    else:
        floor += 1
print(floor)

