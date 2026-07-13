import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []   # smaller half (as negative values)
        self.minheap = []   # larger half

    def addNum(self, num: int) -> None:

        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)

        if len(self.minheap) > len(self.maxheap) + 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)

        if len(self.maxheap) > len(self.minheap) + 1:
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)

    def findMedian(self) -> float:

        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]

        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]

        return (-self.maxheap[0] + self.minheap[0]) / 2.0