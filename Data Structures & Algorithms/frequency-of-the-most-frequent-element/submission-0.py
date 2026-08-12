class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        nums.sort()

        max_freq  = totalsum = 0

        for r in range(len(nums)):
            totalsum += nums[r]
            while l < r and nums[r] * (r - l + 1) > totalsum + k:
                totalsum -= nums[l]
                l +=1
            max_freq = max(max_freq,r - l + 1)

        return max_freq
        
