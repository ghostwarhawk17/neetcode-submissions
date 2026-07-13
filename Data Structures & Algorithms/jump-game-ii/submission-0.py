class Solution:
    def dfs(self,ind,nums,n,dp):
        if dp[ind]!= -1:
            return dp[ind]
        if ind == n - 1:
            return 0
        if ind >= n:
            return float("inf")
        ans = float("inf")
        for jump in range(1,nums[ind] + 1):
            if ind + jump < n:
                ans =  min(ans, 1 + self.dfs(ind + jump , nums,n,dp))
        dp[ind] = ans
                    
        return dp[ind]
    def jump(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        n = len(nums)
        return self.dfs(0,nums,n,dp)

        