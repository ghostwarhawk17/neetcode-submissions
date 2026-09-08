class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        pairs = [[gass,costs] for gass,costs in zip(gas,cost)]
        for i in range(len(pairs)):
            g,c = pairs[i]
            total += g - c
            if total < 0:
                total = 0
                res = i + 1
        return res