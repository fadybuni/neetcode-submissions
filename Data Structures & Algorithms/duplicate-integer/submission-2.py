class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len1 = nums
        nums = set(nums)
        if len(len1) != len(nums):
            return True
        else:
            return False