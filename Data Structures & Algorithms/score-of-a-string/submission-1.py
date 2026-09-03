class Solution:
    def scoreOfString(self, s: str) -> int:
        
        n = len(s)
        if n < 1:
            return ord(s)
        res = 0
        prev = ord(s[0])
        for i in range(1,n):
            curr = ord(s[i])
            res += abs(curr - prev)
            prev = curr
            
        return res