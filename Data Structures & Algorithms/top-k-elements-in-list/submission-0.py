class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numf = {}
        for i in nums:
            if i in numf:
                numf[i] += 1
            else:
                numf[i] = 1
        res = []
        while k > 0:
            freq = max(numf, key=numf.get)
            res.append(freq)
            numf.pop(freq)
            k -=1
        return res
        