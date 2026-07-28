class Solution:
    def solve(self,ind,target,coins,dp):
        if ind ==0:
            if target % coins[ind] == 0:
                return target//coins[ind]
            return float("inf")
        if ind < 0:
            return 0
        if ind == 0:
            if coins[ind] == target:
                return 1
            if coins[ind] == target and target == 0:
                return 2
            
        if dp[ind][target] != -1:
            return dp[ind][target]

        nottake = self.solve(ind - 1,target,coins,dp)
        take = float("inf")
        if coins[ind] <= target:
            take = 1 + self.solve(ind,target - coins[ind],coins,dp)

        dp[ind][target] = min(nottake,take)

        return dp[ind][target]

    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) )]
        ans = self.solve(len(coins) - 1,amount,coins,dp)
        return -1 if ans == float("inf") else ans
        