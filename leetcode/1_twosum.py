#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cmp = dict()
        for index, val in enumerate(nums):
            comp = target - val
            if comp in cmp:
                return [index, cmp[comp]]
            else:
                cmp[val] = index
        
        return []