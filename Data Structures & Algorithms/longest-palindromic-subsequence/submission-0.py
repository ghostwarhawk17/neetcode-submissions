class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        st = s[::-1]
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(st) + 1 )]
 
        for i in range(len(st)- 1,-1,-1):
            for j in range(len(s)-1,-1,-1):
                if st[i] == s[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j]=max(dp[i][j + 1],dp[i + 1][j])
        return dp[0][0]