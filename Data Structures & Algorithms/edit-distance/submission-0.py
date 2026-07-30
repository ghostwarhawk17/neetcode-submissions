class Solution:
    def solve(self,i,j,word1,word2,dp):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if dp[i][j] != -1:
            return dp[i][j]

        if word1[i] == word2[j]:
            dp[i][j] = 0 + self.solve(i - 1,j -1,word1,word2,dp)
        else:
            dp[i][j] = min((1 + self.solve(i - 1,j,word1,word2,dp)),
                           (1 + self.solve(i,j - 1,word1,word2,dp)),
                           (1 + self.solve(i - 1, j -1,word1,word2,dp)))
        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) +1)]
        return self.solve(len(word1) - 1,len(word2) - 1,word1,word2,dp)
        