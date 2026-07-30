class Solution:
    def dfs(self,i,j,grid,dp):
        directions =[(-1,0),(0,-1)]
        if i ==0 and j ==0:
            return grid[0][0]
        if i < 0 or i >= len(grid) or j<0 or j >= len(grid[0]):
            return float("inf")
        if dp[i][j] != -1:
            return dp[i][j]
        best = float("inf")
        for dr,dc in directions:
            new_row = i + dr
            new_col = j + dc

            best = min(best,grid[i][j] + self.dfs(new_row,new_col,grid,dp))
            dp[i][j]= best
        return dp[i][j]
        

    def minPathSum(self, grid: List[List[int]]) -> int:
        dp =[[-1 for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
        return self.dfs(len(grid) -1,len(grid[0]) - 1,grid,dp)
        