# Return an index where the sums on its left and right are equal, or -1 if none exists.
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[(i+1):]):
                return i
                
        return -1