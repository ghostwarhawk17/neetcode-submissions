class Solution:
    def dfs(self, row, col, grid, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == 0:
            return
        visited.add((row, col))
        self.dfs(row + 1, col, grid, visited)
        self.dfs(row, col + 1, grid, visited)
        self.dfs(row - 1, col, grid, visited)
        self.dfs(row, col - 1, grid, visited)

    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        visited = set()
        found = False
        for i in range(len(grid)):
            if found: break
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(i, j, grid, visited)
                    found = True
                    break

        for row, col in visited:
            q.append((row, col, 0))

        while q:
            row, col, dist = q.popleft()

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited:
                    if grid[new_row][new_col] == 1:         
                        return dist                           
                    visited.add((new_row, new_col))
                    q.append((new_row, new_col, dist + 1))

        return -1