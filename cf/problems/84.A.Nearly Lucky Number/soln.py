n = input()
lucky = "47"

lucky_cnt = sum(1 for i in n if i in lucky)

if (str(lucky_cnt) in lucky):
    print("YES")
else:
    print("NO")
