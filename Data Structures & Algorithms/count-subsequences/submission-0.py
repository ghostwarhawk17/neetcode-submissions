class Solution:
    def solve(self,i,j,str1,str2,dp):
        if j < 0:
            return 1
        if i < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if str1[i] == str2[j]:
            dp[i][j] = (self.solve(i - 1, j - 1,str1,str2,dp) + self.solve(i - 1, j,str1,str2,dp))
        else:
            dp[i][j] = self.solve(i - 1, j, str1,str2 ,dp)
        return dp[i][j]
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        return self.solve(len(s) - 1, len(t) - 1,s,t,dp)
        