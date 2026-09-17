class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest = 0
        n = len(s)
        if n == 1:
            return s
        for ch in range(n):
            i,j = ch,ch
            while i >= 0 and j < n and s[i] == s[j]:
                if j-i+1 > longest:
                    longest = j-i+1
                    res = s[i:j+1]
                j += 1
                i -= 1
            i,j = ch,ch+1
            while i >= 0 and j < n and s[i] == s[j]:
                if j-i+1 > longest:
                    longest = j-i+1
                    res = s[i:j+1]
                j += 1
                i -= 1
        return res
        