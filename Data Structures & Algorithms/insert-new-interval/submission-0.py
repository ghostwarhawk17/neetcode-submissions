class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # non overlapping
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                if newInterval[0] < intervals[i][1] or newInterval[1] > intervals[i][0]:
                    newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res
