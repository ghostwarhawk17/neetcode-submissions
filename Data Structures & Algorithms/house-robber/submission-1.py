class Solution:
    def solve(self,ind,nums,dp):
        if ind >= len(nums):
            return 0
       
        if dp[ind]!= - 1:
            return dp[ind]
        pick = 0
     
        pick = nums[ind] + self.solve(ind + 2,nums,dp)
        notpick = self.solve(ind + 1,nums,dp)

        dp[ind] = max(pick,notpick)
        return dp[ind]

    def rob(self, nums: List[int]) -> int:
        dp =[-1 for _ in range(len(nums) + 1)]
        return self.solve(0,nums,dp)
        