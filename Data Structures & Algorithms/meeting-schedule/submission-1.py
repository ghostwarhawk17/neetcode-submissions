class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals == []:
            return True
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start_inter, end_inter = intervals[i].start, intervals[i].end
            if start_inter >= res[-1].end:
                res.append(intervals[i])
            else:
                return False
        return True