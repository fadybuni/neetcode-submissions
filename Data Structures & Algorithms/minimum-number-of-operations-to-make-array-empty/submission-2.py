class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic = {}
        curr = 0
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for keys in dic:
            count = dic[keys]
            while count >= 5:
                count -= 3
                curr += 1
            if count == 1:
                return -1
            elif count <= 3:
                curr += 1
            elif count == 4:
                curr += 2
        return curr

                