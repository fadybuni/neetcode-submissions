class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res = 1
        curr = 1
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i]-1 == nums[i-1]:
                curr += 1
                res = max(res,curr)
            else:
                curr = 1
        return res