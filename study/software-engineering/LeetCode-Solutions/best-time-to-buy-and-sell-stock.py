# Choose one buy day and a later sell day for maximum profit; return 0 if none is possible.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        ranges = [0]

        for i in range(0, len(prices) - 1):
            if prices[i] > max(prices[i+1:]):
                continue

            if prices[i] == min(prices):
                temp = max(prices[i+1:]) - prices[i]
                ranges.append(temp)
                break
            
            else:
                temp = max(prices[i+1:]) - prices[i]
                if temp < max(ranges):
                    continue
                else:
                    ranges.append(temp)

        if not ranges:
            return 0
        else:
            return max(ranges)

# Above solution works... But it does not pass all test cases as runtime is too long.
# ===================================================================================
# Will re-do this solution from scratch later... Skipping for now. 