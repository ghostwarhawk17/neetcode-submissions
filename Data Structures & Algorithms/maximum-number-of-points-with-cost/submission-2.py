class Solution:
    def solve(self,row,prev_col,points,dp):
        if row == len(points):
            return 0
        if dp[row][prev_col] != -1:
            return dp[row][prev_col]
        best = 0

        for c in range(len(points[0])):
            gain = points[row][c] - abs(c - prev_col)
            best = max(best,gain + self.solve(row + 1,c,points,dp))

        dp[row][prev_col] = best
        return dp[row][prev_col]

    def maxPoints(self, points: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(points[0]))] for _ in range(len(points))]
        return max(points[0][c] + self.solve(1,c,points,dp) for c in range(len(points[0])))