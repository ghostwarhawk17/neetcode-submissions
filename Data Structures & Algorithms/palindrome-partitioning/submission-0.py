class Solution:
    def ispalin(self,s):
        rev_s = s[::-1]
        return s == rev_s

    def solve(self,i,j,s,path,ans):
        if i == j:
            ans.append(path[:])
            return 0
        
        temp_str = ""
        for ind in range(i,j):
            temp_str += s[ind]
            if self.ispalin(temp_str):
                path.append(temp_str)
                self.solve(ind + 1,j,s,path,ans)
                path.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        self.solve(0,len(s),s,path,ans)
        return ans

        