class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(n):
            if i % 2 == 1 and nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            if i % 2 == 0 and nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums