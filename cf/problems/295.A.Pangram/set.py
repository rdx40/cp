n = int(input())
s = input()
def is_pangram(n, s):
    return "YES" if len(set(s.lower())) >= 26 else "NO"
print(is_pangram(n, s))
