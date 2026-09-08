class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        for i in range(n):
            profit = max(prices[i:n]) - prices[i]
            if profit > res:
                res = profit    
        return res