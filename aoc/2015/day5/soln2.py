def is_nice_part_two(string):
    has_pair_twice = any(string[i:i+2] in string[i+2:] for i in range(len(string) - 1))
    has_repeat_with_gap = any(string[i] == string[i+2] for i in range(len(string) - 2))
    
    return has_pair_twice and has_repeat_with_gap

with open("input.txt", "r") as file:
    data = file.read().splitlines()
nice_count = sum(1 for string in data if is_nice_part_two(string))

print(f"Number of nice strings: {nice_count}")