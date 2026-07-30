class Solution:
    def solve(self,ind,buy,prices,dp):
        if ind >= len(prices):
            return 0
        if dp[ind][buy] != -1:
            return dp[ind][buy]
        if buy == 1:
            dp[ind][buy] = max(-prices[ind] + self.solve(ind + 1,0,prices,dp), 0 + self.solve(ind + 1,1,prices,dp))
        else:
            dp[ind][buy] = max((prices[ind] + self.solve(ind + 2,1,prices,dp),(0 + self.solve(ind + 1,0,prices,dp))))
        return dp[ind][buy]
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[-1 for _ in range(2)] for _ in range(len(prices) + 1)]
        return self.solve(0,1,prices,dp)
        