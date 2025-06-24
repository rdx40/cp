class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """

        res = []
        for n, i in zip(nums, index):
            res.insert(i, n)
        return res


        
