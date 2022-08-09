#O(n) time, O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

#Same, but no modifying data
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        loc = glo= nums[0]
        for i in range(1, len(nums)):
            loc = max(loc+nums[i], nums[i])
            glo = max(loc, glo)
        return glo