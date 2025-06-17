import hashlib
inp = 'ckczppom'

def advcoin(key):
    i = 1 
    while True:
        test = f"{key}{i}"
        result = hashlib.md5(test.encode()).hexdigest()
        if result.startswith("00000"):
            return i
        else:
            i+=1

print(advcoin(inp))
