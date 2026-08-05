class Solution:
    def solve(self,i,j,k,s1,s2,s3,dp):
        if k == len(s3) and i == len(s1) and j == len(s2):
            return True
        if (i,j) in dp:
            return dp[(i,j)]
        res = False
        if i < len(s1) and s3[k] == s1[i]:
            res =  self.solve(i + 1,j,k + 1,s1,s2,s3,dp)
                
        if not res and j < len(s2) and s3[k] == s2[j]:
            res = self.solve(i,j + 1,k + 1,s1,s2,s3,dp)


        dp[(i,j)] = res
        return dp[(i,j)]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == "" and s2 == "" and s3 == "":
            return True
        dp = {}
        return self.solve(0,0,0,s1,s2,s3,dp)

        