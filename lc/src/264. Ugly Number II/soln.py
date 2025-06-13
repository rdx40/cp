class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i
        return n == 1

    def nthUglyNumber(self, n):
        count = 0
        i = 1
        while True:
            if self.isUgly(i):
                count += 1
                if count == n:
                    return i
            i += 1

