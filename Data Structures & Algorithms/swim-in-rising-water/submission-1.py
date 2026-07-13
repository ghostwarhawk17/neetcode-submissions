import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        q = []
        heapq.heappush(q, (grid[0][0], (0, 0)))
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        while q:
            time, coord = heapq.heappop(q)
            row, col = coord
            if visited[row][col]:
                continue
            visited[row][col] = 1
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return time

            for dr, dc in directions:

                new_row = row + dr
                new_col = col + dc
                if (0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[0])
                    and not visited[new_row][new_col]):
                    new_time = max(time, grid[new_row][new_col])
                    heapq.heappush(q, (new_time, (new_row, new_col)))
        return 0