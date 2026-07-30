class Solution:
    def solve(self, i, j, word1, word2, dp):
        if j < 0:
            return i < 0                                           
        if i < 0:                                                  
            if word2[j] == "*":
                return self.solve(i, j - 2, word1, word2, dp)      
            return False
        

        if dp[i][j] != -1:                                         
            return dp[i][j]

        if word2[j] == "*":                                        
            dp[i][j] = self.solve(i, j - 2, word1, word2, dp)      
            if not dp[i][j] and (word2[j - 1] == "." or word1[i] == word2[j - 1]):
                dp[i][j] = self.solve(i - 1, j, word1, word2, dp)  
        elif word2[j] == "." or word1[i] == word2[j]:              
            dp[i][j] = self.solve(i - 1, j - 1, word1, word2, dp)
        else:
            dp[i][j] = False
        return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1 for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        return self.solve(len(s) - 1, len(p) - 1, s, p, dp)