class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalprofit = 0
        for r in range(1,len(prices)):
            if prices[r] > prices[r - 1]:
                totalprofit += prices[r] - prices[r - 1]
        return totalprofit