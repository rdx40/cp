t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    door_state = list(map(int, input().split()))

    # Find the first and last occurrence of 1
    l, r = -1, -1
    for i in range(n):
        if door_state[i] == 1:
            if l == -1:
                l = i
            r = i

    # If no 1s are found, the range is 0
    if l == -1:
        print("YES")
    else:
        # Check if the range fits within x
        if x >= r - l + 1:
            print("YES")
        else:
            print("NO")