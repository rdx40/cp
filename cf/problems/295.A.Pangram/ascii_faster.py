n = int(input())
s = input()
def is_pangram(n, s):
    if n < 26:
        return "NO"
    seen = [False] * 26
    for c in s.lower():
        if 'a' <= c <= 'z':
            seen[ord(c) - ord('a')] = True
    return "YES" if all(seen) else "NO"
print(is_pangram(n,s))
