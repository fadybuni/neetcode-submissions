class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = nums
        for n in range(n):
            res.append(nums[n])
        return res