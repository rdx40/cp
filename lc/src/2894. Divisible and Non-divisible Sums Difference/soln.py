class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        def sOD(n, m):
            cnt = n // m
            return m * cnt * (cnt + 1) // 2

        totSum = n * (n + 1) // 2
        divSum = sOD(n, m)
        nonSum = totSum - divSum
        return nonSum - divSum

