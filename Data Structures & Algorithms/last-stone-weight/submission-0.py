class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-1] -= stones[-2]
                stones.pop(-2)
                
            stones = sorted(stones)

        if stones:
            return stones[0]
        return 0
        