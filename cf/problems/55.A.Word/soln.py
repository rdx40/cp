str1 = input()
upp = sum(1 for c in str1 if c.isupper())
low = len(str1) - upp

if(upp>low):
    print(str1.upper())
else:
    print(str1.lower())

