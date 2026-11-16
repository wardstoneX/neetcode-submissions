class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        last = intervals[0]

        for interval in intervals[1:]:

            if interval[0] < last[1]:
                last[1] = min(last[1], interval[1])
                count +=1
            else:
                last = interval
        
        return count