# Add one to a non-negative integer represented by its digits and return the resulting digits.
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        number = "".join(str(digit) for digit in digits)
        number = int(number) + 1
        number = str(number)
        return list(int(digit) for digit in number)

