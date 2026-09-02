class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmaxprofit = 0
        b = 0
        s = 1
        while s < len(prices):
            currmaxprofit = max(currmaxprofit,prices[s] - prices[b])
            if prices[s] < prices[b]:
                b = s
            s += 1

        return currmaxprofit
