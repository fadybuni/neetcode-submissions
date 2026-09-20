class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        n = len(prices)
        for i in range(1, n):
            profit = prices[i] - buy
            if profit > res:
                res = profit
            buy = min(buy,prices[i])
        return res