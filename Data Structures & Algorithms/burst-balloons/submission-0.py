from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        @cache
        def solve(i, j):
            if j - i < 2:
                return 0
            maxi = 0
            for ind in range(i + 1, j):                      
                coins = nums[i] * nums[ind] * nums[j] \
                      + solve(i, ind) + solve(ind, j)
                maxi = max(maxi, coins)
            return maxi

        return solve(0, n - 1)