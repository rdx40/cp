class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stonesSorted = sorted(stones)
        while len(stonesSorted) > 1:
            x = stonesSorted.pop() 
            y = stonesSorted.pop()
            if x != y:
                stonesSorted.append(x - y)
            stonesSorted.sort()
        return stonesSorted[0] if stonesSorted else 0

