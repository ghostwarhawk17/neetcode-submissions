class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        org_row,org_col = 0,0
        ans = []
        for i in range(len(points)):
            row,col = points[i]
            dist = (math.sqrt((row - org_row)**2 + (col - org_col)**2))
            heapq.heappush(q,(dist,i))

        while q and k > 0:
            distance , cord = heapq.heappop(q)
            ans.append(points[cord])
            k-= 1
        return ans