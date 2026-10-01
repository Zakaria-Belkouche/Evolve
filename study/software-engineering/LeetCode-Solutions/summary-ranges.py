# Compress sorted, unique consecutive integers into single values or start-to-end ranges.

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        if not nums:
            return []

        if len(nums) == 1:
            answer = [f"{nums[0]}"]
            return answer

        result = []
        start = 0

        for i in range(0, len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                continue
            else:
                if start == i:
                    result.append(f"{nums[i]}")
                    start = i + 1
                else:
                    result.append(f"{nums[start]}->{nums[i]}")
                    start = i + 1
        
        if nums[-1] != nums[-2] + 1:
            result.append(f"{nums[-1]}")
        else:
            result.append(f"{nums[start]}->{nums[-1]}")

        return result

        
