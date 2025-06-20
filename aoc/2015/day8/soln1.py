import ast
with open("input.txt", "r") as file:
    data = file.read().splitlines()

noCode = 0
noMem = 0

for line in data:
    noCode += len(line)
    noMem += len(ast.literal_eval(line))
print(noCode - noMem)

