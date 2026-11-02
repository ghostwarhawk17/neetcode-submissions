
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []

        def dfs(ind):
            res.append(curr.copy())

            for i in range(ind, len(nums)):

                if i > ind and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                dfs(i + 1)
                curr.pop()

        dfs(0)
        return res
