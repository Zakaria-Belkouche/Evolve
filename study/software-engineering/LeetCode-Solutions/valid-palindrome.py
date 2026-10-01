# Ignore non-alphanumeric characters and letter case when checking whether the text reads alike both ways.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        x = "".join(letter.lower() for letter in s if letter.isalnum())
        backwards = x[::-1]
        if backwards == x:
            return True
        else:
            return False