# Return the longest starting substring shared by every string in the list.
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        answer = ""

        lengths = []

        print(len(strs[0]))

        for word in strs:
            lengths.append(len(word))

        for i in range(min(lengths)):
            for word in strs[1:]:
                if strs[0][i] == word[i]:
                    continue
                else:
                    return answer.join(f"{strs[0][0:i]}")
        
        return f"{min(strs)}" 