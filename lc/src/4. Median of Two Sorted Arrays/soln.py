class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)
        mid = n // 2
        if n % 2 == 1:
            return float(nums[mid])
        else:
            return (nums[mid - 1] + nums[mid]) / 2.0
