class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap = {}
        for i,c in enumerate(hand):
            if c not in hashmap:
                hashmap[c]= 1
            else:
                hashmap[c]+=1
        minheap = []
        for key in hashmap:
            heapq.heappush(minheap,key)
        if len(hand) % groupSize:
            return False
        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]
            for i in range(first , first + groupSize):
                if i not in hashmap:
                    return False
                else:
                    hashmap[i] -= 1
                    if hashmap[i] == 0:
                        if i != minheap[0]:
                            return False
                        heapq.heappop(minheap)
        return True
            
            