num = input()
num1 = input()
res = int(num,2) ^ int(num1,2) ##bin to dec then xor
print(f'{res:0{len(num)}b}') ##back to bin
