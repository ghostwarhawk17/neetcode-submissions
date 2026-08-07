from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        q = deque()
        visited = [[0] * n for _ in range(n)]
        directions = [
            (1,0), (0,1), (-1,0), (0,-1),(1,1), (-1,-1), (1,-1),(-1,1)
        ]

        q.append((0, 0, 1))      # row, col, distance
        visited[0][0] = 1

        while q:

            row, col, dist = q.popleft()
            if row == n - 1 and col == n - 1:
                return dist

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (0 <= new_row < n and
                    0 <= new_col < n and
                    not visited[new_row][new_col] and
                    grid[new_row][new_col] == 0):
                    visited[new_row][new_col] = 1
                    q.append((new_row, new_col, dist + 1))

        return -1