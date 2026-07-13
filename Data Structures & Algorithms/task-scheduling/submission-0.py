class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        time = 0
        count = {}
        for task in tasks:
            if task not in count:
                count[task] = 1
            else:
                count[task] +=1
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        

        while q or maxheap:
            time += 1
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt,time + n])
                
            if q and time == q[0][1]:
                 heapq.heappush(maxheap,q.popleft()[0])
        return time
        