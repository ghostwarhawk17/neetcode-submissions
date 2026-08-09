"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)

        start.sort()
        end.sort()

        i = j = 0
        count  = 0
        maxi = 0

        while i < len(start) :
            if start[i] < end[j]:
                count += 1
                i += 1
                maxi = max(maxi,count)

            else:
                count -=1
                j +=1
            

        return maxi
