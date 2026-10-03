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

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        small = prices[0]
        profit = 0
        smallest = min(prices)
        

        for i in range(len(prices)):

            if prices[i] > small:
                continue

            if prices[i] < small:
                small = prices[i]

            if prices[i] == smallest:
                diff = max(prices[i:]) - small
                if diff > profit:
                    profit = diff
                break

            diff = max(prices[i:]) - small

            if diff > profit:
                profit = diff

        return profit

# ====================================================================================
# This solution works completely. Passes all test cases but it's still super slow...
# Barely meetings the max runtime to pass all test cases. 