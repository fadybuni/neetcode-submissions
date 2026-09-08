class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        s = s.lower()
        j = len(s)-1
        while j > i:
            while not s[j].isalnum() and j>i:
                j -= 1
            while not s[i].isalnum() and j>i:
                i += 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            