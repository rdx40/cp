a = 1
b = 1

index = 2

while True:
    temp = b
    b += a
    a = temp
    index += 1
    if len(str(b)) == 1000:
        print(index)
        break