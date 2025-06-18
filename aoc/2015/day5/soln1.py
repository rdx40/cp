def is_nice(string):
    vowels = "aeiou"
    vowel_count = sum(1 for char in string if char in vowels)
    if vowel_count < 3:
        return False
    has_double_letter = any(string[i] == string[i + 1] for i in range(len(string) - 1))
    if not has_double_letter:
        return False
    forbidden_substrings = ["ab", "cd", "pq", "xy"]
    if any(substring in string for substring in forbidden_substrings):
        return False

    return True

with open("input.txt", "r") as file:
    data = file.read().splitlines()
nice_count = sum(1 for string in data if is_nice(string))

print(f"Number of nice strings: {nice_count}")
