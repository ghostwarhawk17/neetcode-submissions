class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxheap = []
        mincapital = [(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(mincapital)

        for i in range(k):
            while mincapital and mincapital[0][0] <= w:
                cap,prof = heapq.heappop(mincapital)
                heapq.heappush(maxheap,-1 * prof)

            if not maxheap:
                break
            w += -1 * heapq.heappop(maxheap) 
        return w
        