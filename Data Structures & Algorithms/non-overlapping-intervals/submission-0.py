class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = [intervals[0]]
        result = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < res[-1][1]:
                result += 1
                continue
            res.append(intervals[i])
        return result