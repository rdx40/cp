def compute():
    max_length = 0
    starting_number = 1
    collatz_lengths = {}
    for i in range(1, 1_000_000):
        length = collatz_chain_length(i, collatz_lengths)
        if length > max_length:
            max_length = length
            starting_number = i
    return starting_number
def collatz_chain_length(n, cache):
    original_n = n
    length = 0
    while n != 1:
        if n in cache:
            length += cache[n]
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    cache[original_n] = length + 1
    return cache[original_n]
result = compute()
print("Starting number with the longest Collatz sequence under 1,000,000:", result)
