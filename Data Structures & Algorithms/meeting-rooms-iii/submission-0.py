class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = []
        used = []
        count = [0] * n
        meetings.sort(key = lambda x : x[0])

        for i in range(n):
            heapq.heappush(available,(i))
        heapq.heapify(available)

        for i in range(len(meetings)):
            start,end = meetings[i]
            while used and used[0][0] <= start:
                _,room = heapq.heappop(used)
                heapq.heappush(available,room)
            if len(available) > 0:
                room = heapq.heappop(available)
                heapq.heappush(used,(end,room))
                heapq.heapify(used)

            else:
                early_end,room = heapq.heappop(used)
                heapq.heappush(used,(early_end + (end - start),room))
            count[room] += 1
        return count.index(max(count))
            
                

                
