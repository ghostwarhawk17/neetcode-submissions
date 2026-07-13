from collections import defaultdict
from itertools import combinations
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        g = defaultdict(list)
        for time_stamp, user, web in sorted(zip(timestamp, username, website)):
            g[user].append(web)
        
        score = defaultdict(int)

        for user, websites in g.items():
            for pattern in set(combinations(websites, 3)):
                score[pattern] += 1

        max_pattern, max_count = (), 0

        for pattern, count in score.items():
            if count > max_count:
                max_count = count
                max_pattern = pattern
            elif count == max_count and pattern < max_pattern:
                max_pattern = pattern

        return list(max_pattern)
