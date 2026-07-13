class Solution:
    def dfs(self,ind,nums,n,memo):
        if ind in memo:
            return memo[ind]
        if ind == n - 1:
            return True
        if nums[ind] == 0:
            return False
    
        for jump in range(nums[ind], 0, -1):
            if ind + jump < n:
                if self.dfs(ind + jump,nums,n,memo):
                    memo[ind] = True
                    return True
        memo[ind] = False
        return False
    def canJump(self, nums: List[int]) -> bool:
        return self.dfs(0,nums,len(nums),{})