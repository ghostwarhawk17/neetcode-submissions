class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_point = -1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_point = i
                break
        if break_point == -1:
            nums.reverse()
            return


        smaller = float("inf")
        ans = -1

        for j in range(break_point + 1, len(nums)):
            if nums[j] > nums[break_point] and nums[j] < smaller:
                smaller = nums[j]
                ans = j

    
        nums[break_point], nums[ans] = nums[ans], nums[break_point]
        nums[break_point + 1:] = reversed(nums[break_point + 1:])