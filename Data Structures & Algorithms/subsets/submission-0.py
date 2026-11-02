class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(ind,curr):
            if ind == len(nums):
                res.append(curr.copy())
                return
            # take the current elemrnt
            curr.append(nums[ind])
            dfs(ind + 1,curr)

            curr.pop()
            dfs(ind + 1,curr)

        dfs(0,curr)
        return res


