colors = list(map(int, input().split()))
unique_colors = set(colors)
needed_to_buy = 4 - len(unique_colors)
print(needed_to_buy)

