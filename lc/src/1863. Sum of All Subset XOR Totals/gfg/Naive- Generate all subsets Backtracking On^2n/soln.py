# for [1, 2, 3]

# start with -> []

# now iter2 take any ele say 1 -> i can either take 1 -> [1]
#                             -> or not take 1       -> []

# now two branches [] [1]

# now iter2 take 2 -> branch 1 -> take 2 -> [1,2]
#                              -> not take-> [1]
#                  -> branch 2 -> take 2 -> [2]
#                              -> not take->[]

# now 4 branches [] [1] [2] [1,2]

# now iter3 take 3 -> branch 1 -> take 3 -> [1,2,3]
#                              -> dont take->[1,2]
#                 -> branch 2  -> take 3 -> [1,3]
#                              -> dont take -> [1]
#                 ->branch 3   -> take 3 -> [2,3]
#                             -> dont take ->[2]
#                 -> branch 4 -> take 3 ->[3]
#                             -> dont take ->[]
# Now FINALLY -> [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]

class Solution(object):
    def subsetRecur(self, i, arr, res, subset):
        if i == len(arr):
            res.append(subset[:])
            return

        subset.append(arr[i])
        self.subsetRecur(i + 1, arr, res, subset)
        subset.pop()
        self.subsetRecur(i + 1, arr, res, subset)

    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        subset = []
        res = []
        self.subsetRecur(0, nums, res, subset)

        ans = 0
        for it in res:
            xor_val = 0
            for val in it:
                xor_val ^= val
            ans += xor_val
        return ans
