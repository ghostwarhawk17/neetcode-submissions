from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        @cache
        def solve(i, j):
            if i >= j:                       # empty interval
                return 0
            maxi = 0
            for ind in range(i, j):          # ind = balloon burst LAST
                coins = nums[i - 1] * nums[ind] * nums[j] \
                      + solve(i, ind) + solve(ind + 1, j)
                maxi = max(maxi, coins)
            return maxi

        return solve(1, n - 1)