class Solution:
    def solve(self,i,j,m,n,dp):
        if i == 0 and j == 0:
            return 1
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        # left :
        left = self.solve(i,j-1,m,n,dp)
        up = self.solve(i - 1,j,m,n,dp)

        dp[i][j] = left + up
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.solve(m-1,n-1,m,n,dp)
        