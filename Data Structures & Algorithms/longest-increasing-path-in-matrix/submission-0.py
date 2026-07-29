class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            best = 1
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1 + dfs(ni, nj))
            dp[i][j] = best
            return best

        return max(dfs(i, j) for i in range(rows) for j in range(cols))