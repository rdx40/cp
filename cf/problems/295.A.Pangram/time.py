import time

# Input example
n = 35
s = "TheQuickBrownFoxJumpsOverTheLazyDog"

# -------- A. Using ASCII (manual check) --------
start_a = time.time()

def is_pangram_ascii(n, s):
    if n < 26:
        return "NO"
    seen = [False] * 26
    for c in s.lower():
        if 'a' <= c <= 'z':
            seen[ord(c) - ord('a')] = True
    return "YES" if all(seen) else "NO"

result_a = is_pangram_ascii(n, s)
end_a = time.time()
time_a = end_a - start_a

# -------- B. Using Optimal Set-based Solution --------
start_b = time.time()

def is_pangram_set(n, s):
    return "YES" if len(set(s.lower())) >= 26 else "NO"

result_b = is_pangram_set(n, s)
end_b = time.time()
time_b = end_b - start_b

# -------- Output results --------
print("ASCII Solution: ", result_a, "Time:", time_a)
print("Set-Based Solution: ", result_b, "Time:", time_b)

