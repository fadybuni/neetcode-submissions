class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s)-1
        res = 0
        letter = False
        while j >= 0:
            if s[j] == " " and letter == False:
                j -= 1
            elif s[j] == " " and letter == True:
                return res
            else:
                letter = True
                res += 1
                j -= 1
        return res