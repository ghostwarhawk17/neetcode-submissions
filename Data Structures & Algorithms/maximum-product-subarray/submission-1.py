class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 0
        currmax=currmin =1
        if len(nums) == 1:
            return nums[0]

        for num in nums:
            current = currmax * num
            currmax = max(current,currmin * num,num)
            currmin = min(current,currmin * num,num)
            res = max(res,currmax)
        return res