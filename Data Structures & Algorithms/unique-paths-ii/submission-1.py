class Solution:
    def solve(self,i,j,obstacleGrid,dp):
        if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
            return 1
        if obstacleGrid[i][j] == 1:
            return 0
        if i < 0 or i >= len(obstacleGrid) or j < 0 or j >= len(obstacleGrid[0]):
            return 0
        if dp[i][j] !=-1:
            return dp[i][j]
        left = self.solve(i,j-1,obstacleGrid,dp)
        up = self.solve(i - 1,j,obstacleGrid,dp)
        dp[i][j] = up + left
        return dp[i][j]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        return self.solve(len(obstacleGrid) - 1,len(obstacleGrid[0])-1,obstacleGrid,dp)