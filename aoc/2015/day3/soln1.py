with open("input.txt", "r") as file:
    data = file.read().strip()

x, y = 0, 0
visited = {(x, y)}
for move in data:
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '>':
        x += 1
    elif move == '<':
        x -= 1
    visited.add((x, y))
print(len(visited))