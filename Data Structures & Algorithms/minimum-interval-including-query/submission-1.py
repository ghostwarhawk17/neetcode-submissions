class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])
        sorted_q = sorted(enumerate(queries), key = lambda x:x[1])
        minheap = [] # [res,end]
        res = [-1] * len(queries) 
        i = 0

        for orig_ind,q in sorted_q:
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minheap,(r - l + 1,r))
                i += 1
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            if minheap :
                res[orig_ind] = minheap[0][0]
        return res
            
        