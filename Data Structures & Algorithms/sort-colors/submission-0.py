class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = j = l = 0

        while l < len(nums):
            if nums[l] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                if i < j:
                    nums[j], nums[l] = nums[l], nums[j]
                i += 1
                j += 1
                l += 1
            elif nums[l] == 1:
                nums[j], nums[l] = nums[l], nums[j]
                j += 1
                l += 1
            else:
                l += 1
