class Solution:
    def solve(self,ind,target,nums,dp):
        if target == 0:
            return True
        if ind == 0:
            if nums[ind] == target:
                return True
            return False
        if ind < 0 or ind > len(nums) - 1 :
            return False
        if dp[ind][target] != -1:
            return dp[ind][target]
        nottake = self.solve(ind - 1,target,nums,dp)
        take = False
        if nums[ind] <= target:
            take = self.solve(ind - 1,target - nums[ind],nums,dp)
        dp[ind][target] = nottake or take
        return dp[ind][target]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        totalsum = sum(nums)
        target = 0
        if totalsum % 2:
            return False
        else:
            target = totalsum // 2
        dp = [[-1 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        return bool(self.solve(len(nums) - 1,target,nums,dp))