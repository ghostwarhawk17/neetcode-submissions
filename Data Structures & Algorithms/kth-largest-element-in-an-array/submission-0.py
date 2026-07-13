class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        n = len(nums)
        for i in range(len(nums)):
            heapq.heappush(q,nums[i])

        while len(q) > k:
            heapq.heappop(q)
        return heapq.heappop(q)