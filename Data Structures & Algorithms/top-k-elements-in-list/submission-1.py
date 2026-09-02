class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        result = []
        for i in range(k):
            most = max(dic,key = dic.get)
            result.append(most)
            dic.pop(most)
        return result