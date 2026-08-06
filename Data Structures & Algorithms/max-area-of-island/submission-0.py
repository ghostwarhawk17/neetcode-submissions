class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        q = deque() # multi source bfs
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        maxi = float("-inf")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i,j))
                cnt = 0
                while q:
                    row,col = q.popleft()
                    cnt +=1
                    if (row,col) not in visited:
                        visited.add((row,col))

                    for dr,dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if (new_row,new_col) not in visited and 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                            q.append((new_row,new_col))
                            
                            visited.add((new_row,new_col))
                maxi = max(maxi,cnt)

        return maxi

