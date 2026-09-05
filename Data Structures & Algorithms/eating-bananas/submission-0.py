class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        n = len(piles)
        res = high
        while high >= low:
            temp = 0
            mid = (high+low) //2
            for k in range(n):
                temp += (piles[k] + mid -1) // mid
            if temp > h:
                low = mid + 1
            else:
                high = mid - 1
                res = min(mid,res)
        return res
        
                
                    