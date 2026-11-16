class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        last = intervals[0]
        result = [] 
        current = None
        for interval in intervals[1:]:
            current= interval

            if current[0] > last[1]:
                result.append(last)
                last = current
            else:
                last[1] = max(last[1], current[1])
        

        result.append(last)
        return result
        