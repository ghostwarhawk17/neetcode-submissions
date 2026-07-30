class Solution:
    def solve(self, ind, coins, target, dp):
        if ind == 0:
            return 1 if target % coins[0] == 0 else 0  

        if dp[ind][target] != -1:
            return dp[ind][target]

        res = self.solve(ind - 1, coins, target, dp)     
        if coins[ind] <= target:
            res += self.solve(ind, coins, target - coins[ind], dp)  
        dp[ind][target] = res
        return dp[ind][target]

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        return self.solve(len(coins) - 1, coins, amount, dp)