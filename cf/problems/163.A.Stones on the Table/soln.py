def stones_to_remove(n, s):
    count = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
    return count

n = int(input())
s = input().strip()
print(stones_to_remove(n, s))

