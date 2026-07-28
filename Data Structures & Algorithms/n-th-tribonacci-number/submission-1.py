class Solution:
    def solve(self,n,dp):
        if n <= 2:
            return 1 if n != 0 else 0
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.solve(n - 1,dp) + self.solve(n - 2,dp) + self.solve(n - 3,dp)
        return dp[n]
    def tribonacci(self, n: int) -> int:
        dp = [-1 for _ in range(n + 1)]
        return self.solve(n,dp)