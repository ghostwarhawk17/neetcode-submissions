class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_cnt = [0] * len(grid)
        col_cnt = [0] * len(grid[0])
        res=0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    row_cnt[r] +=1
                    col_cnt[c] +=1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] ==1 and max(row_cnt[r],col_cnt[c]) > 1:
                    res+=1
        return res