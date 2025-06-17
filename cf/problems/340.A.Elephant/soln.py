x = int(input())
min_steps = x // 5
if x % 5 != 0:
    min_steps += 1
print(min_steps)
