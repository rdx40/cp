with open("input.txt", "r") as file:
    data = file.read().splitlines()

grid = [[0 for i in range(1000)] for j in range(1000)]

inst = []
for d in data:
    inst.append(d)

for line in inst:
    if line.startswith("turn on"):
        op = "on"
        coords = line[len("turn on "):]
    elif line.startswith("turn off"):
        op = "off"
        coords = line[len("turn off "):]
    elif line.startswith("toggle"):
        op = "toggle"
        coords = line[len("toggle "):]

    start, end = coords.split(" through ")
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if op == "on":
                grid[x][y] = 1
            elif op == "off":
                grid[x][y] = 0
            elif op == "toggle":
                grid[x][y] = 1 - grid[x][y]

print(sum(sum(row) for row in grid))
