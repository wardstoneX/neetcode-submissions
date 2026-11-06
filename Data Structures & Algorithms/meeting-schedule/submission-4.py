"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        print(intervals)

        intervals.sort(key=lambda x: x.start)

        meetingEnd = 0

        for interval in intervals:
            if meetingEnd > interval.start: 
                return False
            meetingEnd = interval.end
        
        return True
            

