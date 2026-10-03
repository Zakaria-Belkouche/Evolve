# Each row contains one customer's account balances; return the greatest row total.
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealths = []
        for customer in accounts:
            wealth = sum(customer)
            wealths.append(wealth)

        return max(wealths)