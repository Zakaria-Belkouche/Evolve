# For each position, return the product of all input values except the value at that position.
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        from math import prod

        answer = []
        product = math.prod(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                temp = math.prod(nums[0:i]) * math.prod(nums[i+1:])
                answer.append(int(temp))
            else:
                temp = product/nums[i]
                answer.append(int(temp))


        return answer