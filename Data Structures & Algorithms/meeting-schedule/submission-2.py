"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prevend = 0
        intervals = sorted(intervals, key=lambda i: i.start)
        for i in intervals:
            if i.start >= prevend:
                prevend = i.end
            else:
                return False
        return True
