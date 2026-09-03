class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in nums:
            res *= i

        def signFunc(x):
            if x == 0:
                return 0
            if x > 0:
                return 1
            if x < 0:
                return -1
        
        return signFunc(res)