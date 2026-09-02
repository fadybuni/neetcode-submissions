class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for spot, value in enumerate(nums):
            compliment = target - value

            if compliment in dic:
                return [dic[compliment],spot]
            dic[value] = spot