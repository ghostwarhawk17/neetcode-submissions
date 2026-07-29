class Solution:
    def solve(self, target, nums, dp):
        if target == 0:
            return 1

        if dp[target] != -1:
            return dp[target]

        ways = 0

        for num in nums:
            if num <= target:
                ways += self.solve(target - num, nums, dp)

        dp[target] = ways
        return ways

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)
        return self.solve(target, nums, dp)