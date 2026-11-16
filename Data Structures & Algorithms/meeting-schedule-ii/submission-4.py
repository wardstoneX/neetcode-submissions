"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key= lambda interval: interval.start)
        meeting_rooms = []
        
        

        for interval in intervals:

            

            if meeting_rooms and interval.start < meeting_rooms[0]:
                heapq.heappush(meeting_rooms, interval.end)

            elif not meeting_rooms:
                heapq.heappush(meeting_rooms, interval.end)
            else:
                heapq.heappop(meeting_rooms)
                heapq.heappush(meeting_rooms, interval.end)

            
        return len(meeting_rooms)


