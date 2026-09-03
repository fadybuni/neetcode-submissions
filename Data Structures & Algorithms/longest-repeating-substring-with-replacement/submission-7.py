class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s is None:
            return 0
        greatest = 0
        n = len(s)
        for ch in set(s):
            i = 0
            spent = 0
            for j in range(n):
                if s[j] != ch:
                    spent += 1
                while spent > k:
                    if s[i] != ch:
                        spent -= 1
                    i += 1
                greatest = max(greatest, j-i + 1)
        return greatest

