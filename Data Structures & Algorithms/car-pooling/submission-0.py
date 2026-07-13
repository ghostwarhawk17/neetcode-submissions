class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        curr_capacity = 0
        minheap = [] #pairs of end,numpass

        for i in range(len(trips)):
            num,start,to = trips[i]
            while minheap and minheap[0][0] <= start:
                end,numpass = heapq.heappop(minheap)
                curr_capacity -= numpass
            heapq.heappush(minheap,(to,num))

            curr_capacity += num
            if curr_capacity > capacity:
                return False
        return True