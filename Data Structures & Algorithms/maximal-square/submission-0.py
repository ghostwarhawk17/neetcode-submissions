class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix[0])):
            dp[0][i] = int(matrix[0][i])

        for j in range(len(matrix)):
            dp[j][0] = int(matrix[j][0])

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],dp[i][j - 1],dp[i - 1][j])
        maxi = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxi = max(maxi,dp[i][j])

        return maxi * maxi