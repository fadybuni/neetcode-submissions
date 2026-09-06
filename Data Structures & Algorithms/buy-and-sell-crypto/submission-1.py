class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprof = 0
        minprice = prices[0]
        for i in range(n):
            minprice = min(minprice,prices[i])
            maxprof = max(maxprof, prices[i] - minprice)
        return maxprof


