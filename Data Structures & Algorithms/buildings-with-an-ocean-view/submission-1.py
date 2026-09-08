class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        n = len(heights)
        ans.append(n - 1)
        curr_highest = heights[-1]
        for i in range(len(heights) - 2,-1,-1):
            curr = heights[i]
            if curr > curr_highest:
                curr_highest = max(curr,curr_highest)
                ans.append(i)

        ans.sort()
        return ans
        