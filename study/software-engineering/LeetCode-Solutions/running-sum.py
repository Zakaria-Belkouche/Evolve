# Given a list of numbers, return the cumulative sum through each position.
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        cumalitive = 0
        for i in range(len(nums)):
            cumalitive = cumalitive + nums[i]
            result.append(cumalitive)

        return result