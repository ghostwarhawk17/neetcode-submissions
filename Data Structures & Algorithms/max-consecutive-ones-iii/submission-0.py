class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zero_count=one_count = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                one_count +=1
            else:
                zero_count +=1
            
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -=1
                else:
                    one_count -=1
                l+=1
            res = max(res,one_count + zero_count)
        return res
