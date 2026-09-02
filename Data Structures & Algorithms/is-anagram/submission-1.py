class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sh = {}
        th = {}
        for i in range(len(s)):
            if s[i] not in sh:
                sh[s[i]] = 1
            else:
                sh[s[i]] += 1
            if t[i] not in th:
                th[t[i]] = 1
            else:
                th[t[i]] += 1
        return  th == sh

        