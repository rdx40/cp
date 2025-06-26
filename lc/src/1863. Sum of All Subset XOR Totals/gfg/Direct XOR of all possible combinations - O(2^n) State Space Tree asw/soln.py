class Solution(object):
    def xorRecur(self,i, sum, arr):
        if i == len(arr):
            return sum
        take = self.xorRecur(i + 1, sum ^ arr[i], arr)
        noTake = self.xorRecur(i + 1, sum, arr)
        return take + noTake

    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.xorRecur(0,0,nums)
        


