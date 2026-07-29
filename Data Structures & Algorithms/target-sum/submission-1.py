class Solution:
    def solve(self, ind, target, nums, dp):
        if ind == 0:
            if target == 0 and nums[0] == 0:
                return 2
            if target == 0 or target == nums[0]:
                return 1
            return 0
        if dp[ind][target] != -1:
            return dp[ind][target]
        nottake = self.solve(ind - 1, target, nums, dp)
        take = 0
        if nums[ind] <= target:
            take = self.solve(ind - 1, target - nums[ind], nums, dp)
        dp[ind][target] = take + nottake
        return dp[ind][target]

    def findTargetSumWays(self, nums: List[int], target: int):
        totalsum = sum(nums)

        if totalsum - target < 0:
            return 0
        if (totalsum - target) % 2:
            return 0
        tar = (totalsum - target) // 2
        dp = [[-1 for _ in range(tar + 1)] for _ in range(len(nums))]
        return self.solve(len(nums) - 1, tar, nums, dp)