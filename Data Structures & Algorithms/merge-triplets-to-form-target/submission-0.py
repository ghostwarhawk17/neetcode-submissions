
from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue

            if a == target[0]:
                good.add(0)
            if b == target[1]:
                good.add(1)
            if c == target[2]:
                good.add(2)

        return len(good) == 3
