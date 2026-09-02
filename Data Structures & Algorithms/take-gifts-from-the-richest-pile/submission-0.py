
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap = []
        for gift in gifts:
            heapq.heappush(maxheap,(-1 * gift))
        heapq.heapify(maxheap)

        ans = 0
        time = 0

        while maxheap and time < k:
            time +=1 
            ele = -1 * heapq.heappop(maxheap)
            remainder = math.floor(math.sqrt(ele))

            if remainder:
                heapq.heappush(maxheap,(-1 * remainder))

        while maxheap:
            ans += -heapq.heappop(maxheap)

        return ans

        