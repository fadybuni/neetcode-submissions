class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            needed = target - num
            if needed in dic:
                res = dic[needed]
                return [res,index]
            dic[num] = index
        