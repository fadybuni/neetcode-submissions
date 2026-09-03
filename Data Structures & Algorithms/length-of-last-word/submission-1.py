class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s)-1
        res = 0
        letter = False
        while s[j] == " " and j >= 0:
            j -= 1

        while s[j] != " " and j >= 0:
            res += 1
            j -= 1
        
        return res