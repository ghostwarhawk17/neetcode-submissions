class Solution:
    def count(self, s):
        ones = zeros = 0
        for c in s:
            if c == '0':
                zeros += 1
            else:
                ones += 1
        return ones, zeros

    def solve(self, ind, curr_one, curr_zero, m, n, strs, dp):
        if ind >= len(strs):
            return 0
        if dp[ind][curr_one][curr_zero] != -1:
            return dp[ind][curr_one][curr_zero]

        nottake = self.solve(ind + 1, curr_one, curr_zero, m, n, strs, dp)
        take = 0

        new_ones, new_zeros = self.count(strs[ind])
        if curr_one + new_ones <= n and curr_zero + new_zeros <= m:
            take = 1 + self.solve(ind + 1,
                                  curr_one + new_ones,
                                  curr_zero + new_zeros,
                                  m, n, strs, dp)

        dp[ind][curr_one][curr_zero] = max(take, nottake)
        return dp[ind][curr_one][curr_zero]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[-1] * (m + 1) for _ in range(n + 1)] for _ in range(len(strs))]
        return self.solve(0, 0, 0, m, n, strs, dp)