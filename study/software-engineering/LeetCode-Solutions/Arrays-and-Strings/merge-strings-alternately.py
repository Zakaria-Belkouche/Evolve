# Interleave characters from two strings, then append any characters left over.
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        if len(word1) >= len(word2):
            for i in range(len(word1)):
                if i <= len(word2) - 1:
                    result += f"{word1[i]}{word2[i]}"
                else:
                    result += f"{word1[i]}"
        else:
            for i in range(len(word2)):
                if i<= len(word1) - 1:
                    result += f"{word1[i]}{word2[i]}"
                else:
                    result += f"{word2[i]}"
        
        return result
            