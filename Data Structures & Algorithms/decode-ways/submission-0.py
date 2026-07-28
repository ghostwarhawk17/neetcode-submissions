class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * (len(s) + 1)

        def dfs(ind):
            if ind == len(s):
                return 1
            if s[ind] == '0':
                return 0
            if dp[ind] != -1:
                return dp[ind]

            res = dfs(ind + 1)
            if ind + 1 < len(s) and (s[ind] == '1' or (s[ind] == '2' and s[ind + 1] in "0123456")):
                res += dfs(ind + 2)

            dp[ind] = res
            return res

        return dfs(0)