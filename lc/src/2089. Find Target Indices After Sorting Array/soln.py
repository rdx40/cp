class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        numsSorted = sorted(nums)
        for i in range(len(numsSorted)):
            if numsSorted[i]==target:
                res.append(i)
            
        return res




        
