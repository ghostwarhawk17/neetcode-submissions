class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac,alt = set(),set()
        def dfs(row,col,visited,prevheight,heights):
            if row < 0 or row == len(heights) or col < 0 or col >= len(heights[0]) or (row,col) in visited or heights[row][col] < prevheight:
                return
            visited.add((row,col))
            dfs(row + 1,col,visited,heights[row][col],heights)
            dfs(row - 1,col,visited,heights[row][col],heights)
            dfs(row ,col + 1,visited,heights[row][col],heights)
            dfs(row,col - 1,visited,heights[row][col],heights)

        for c in range(len(heights[0])):
            dfs(0,c,pac,heights[0][c],heights)
            dfs(len(heights) - 1,c,alt,heights[len(heights) - 1][c],heights)

        for r in range(len(heights)):
            dfs(r,0,pac,heights[r][0],heights)
            dfs(r, len(heights[0]) - 1, alt, heights[r][len(heights[0]) - 1], heights)
        ans = []
    
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):

                if (i,j) in pac and (i,j) in alt:
                    ans.append([i,j])

        return ans