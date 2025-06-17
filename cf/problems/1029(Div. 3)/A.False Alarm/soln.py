t = int(input())

for i in range(t):
    n, x = map(int, input().split())
    door_state = list(map(int, input().split()))

    button_pressed = False
    time = 0

    j = 0
    while j < n:
        if door_state[j] == 0:
            j += 1
            time += 1
        else:
            if button_pressed:
                print("NO")
                break
            button_pressed = True
            time += 1
            j += 1
            for _ in range(x - 1):
                if j >= n:
                    break
                j += 1
                time += 1
    else:
        print("YES")