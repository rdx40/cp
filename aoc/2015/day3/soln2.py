with open("input.txt", "r") as file:
    data = file.read().strip()

santa_x, santa_y = 0, 0
robo_x, robo_y = 0, 0
visited = {(0, 0)}

for i, move in enumerate(data):
    if i % 2 == 0:
        if move == '^':
            santa_y += 1
        elif move == 'v':
            santa_y -= 1
        elif move == '>':
            santa_x += 1
        elif move == '<':
            santa_x -= 1
        visited.add((santa_x, santa_y))
    else:
        if move == '^':
            robo_y += 1
        elif move == 'v':
            robo_y -= 1
        elif move == '>':
            robo_x += 1
        elif move == '<':
            robo_x -= 1
        visited.add((robo_x, robo_y))
print(len(visited))