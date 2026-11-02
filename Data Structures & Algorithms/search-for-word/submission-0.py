
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = set()

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(i, j, k):
            if k == len(word):
                return True

            if i < 0 or i >= n or j < 0 or j >= m:
                return False

            if (i,j) in visited or board[i][j] != word[k]:
                return False

            visited.add((i,j))

            for dr, dc in directions:
                if dfs(i + dr, j + dc, k + 1):
                    return True

            visited.remove((i,j))
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False
