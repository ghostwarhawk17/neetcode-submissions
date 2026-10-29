class Solution:
    def dfs(self,r,col,negdiag,postdiag,res,grid):
        if r == len(grid[0]):
            ans = ["".join(row) for row in grid]
            res.append(ans)
            return

      
        for c in range(len(grid)):
            if (r - c) in negdiag or (r + c) in postdiag or c in col:
                continue
            grid[r][c] ='Q'
            col.add(c)
          
            postdiag.add(r + c)
        
            negdiag.add(r - c)

            self.dfs(r + 1,col,negdiag,postdiag,res,grid)
            col.remove(c)
            postdiag.remove(r + c) 
            negdiag.remove(r - c) 
            grid[r][c] = '.'
    
         

    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.' for _ in range(n)] for _ in range(n)]
        col = set()
        negdiag =  set()
        postdiag = set()
        res =[]

        self.dfs(0,col,negdiag,postdiag,res,grid)
        return res


                
                    
                 