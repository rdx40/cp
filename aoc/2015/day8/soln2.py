with open("input.txt", "r") as file:
    data = file.read().splitlines()

Oglength = 0
encoded_length = 0

for line in data:
    Oglength += len(line)
    encoded = line.replace('\\', '\\\\').replace('"', '\\"')
    encoded = f'"{encoded}"'
    encoded_length += len(encoded)

print(encoded_length - Oglength)

