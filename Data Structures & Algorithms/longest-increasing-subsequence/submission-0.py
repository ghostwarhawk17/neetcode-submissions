from _bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = []
        temp.append(nums[0])

        for i in range(len(nums)):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                ind = bisect_left(temp,nums[i])
                temp[ind]= nums[i]
        return len(temp)