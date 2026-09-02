class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        suffix = 1
        n = len(nums)
        for i in range(n):
            res.append(prefix)
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res