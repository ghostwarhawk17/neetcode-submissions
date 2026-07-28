class Solution:
    def solve(self,ind,nums,dp):
        if ind == len(nums):
            return 1
        if ind > len(nums) or ind < 0:
            return 0
        if dp[ind] != -1:
            return dp[ind]
        notpick = self.solve(ind - 1,nums,dp)
        pick = nums[ind] + self.solve(ind -2 ,nums,dp)
        dp[ind] = max(pick,notpick)
        return dp[ind]
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        return self.solve(len(nums) - 1,nums,dp)
        