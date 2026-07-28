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
        if len(nums) == 1:
            return nums[0]
        dp1 = [-1 for _ in range(len(nums))]
        dp2 = [-1 for _ in range(len(nums))]
        return max(self.solve(len(nums) - 2,nums[1:],dp1),
        self.solve(len(nums) - 2,nums[:-1],dp2 ))
        