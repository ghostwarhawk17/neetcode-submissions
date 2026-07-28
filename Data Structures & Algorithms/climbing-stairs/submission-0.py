class Solution:
    def solve(self,ind,n,dp):
        if ind == n:
            return 1
        if ind > n:
            return 0
        if dp[ind] != -1:
            return dp[ind]
        ways = self.solve(ind + 1,n,dp) + self.solve(ind + 2,n,dp)
        dp[ind] = ways
        return dp[ind]
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n + 1)]
        return self.solve(0,n,dp)