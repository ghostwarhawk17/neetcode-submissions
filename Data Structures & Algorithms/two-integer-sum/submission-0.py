class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in mapp:
                return [mapp[k], i]
            mapp[nums[i]] = i
