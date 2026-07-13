class Solution:
    def solve(self,ind,target,nums,ans,current):
        if target < 0 or ind == len(nums):
            return 
        if target == 0:
            ans.append(list(current))
            return
        if nums[ind] <= target:
            current.append(nums[ind])
            self.solve(ind,target - nums[ind],nums,ans,current)
            current.pop()
        self.solve(ind + 1,target,nums,ans,current)
        

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        current =[]
        self.solve(0,target,nums,ans,current)
        return ans