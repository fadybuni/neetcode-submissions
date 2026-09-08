class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        res = []
        while k > 0:
            freq = max(seen, key=seen.get)
            res.append(freq)
            seen.pop(freq)
            k -= 1
        return res