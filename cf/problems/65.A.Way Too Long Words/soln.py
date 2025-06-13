n = int(input())
words = [0]*n
for j in range(n):
    words[j] = input()


for i in range(len(words)):
    if(len(words[i])>10):
        words[i] = words[i][0]+(str)(len(words[i])-2)+words[i][-1]


for word in words:
    print(word)
