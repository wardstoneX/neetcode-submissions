class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        result = []
        end = 0
        start = 0
        hmap = {}
        for i, c in enumerate(s):
            hmap[c] = i
        
        for i, c in enumerate(s):
            print(i,c, start,end)
            endOfChar = hmap[c]

            if end < endOfChar:
                end = endOfChar
            elif i == end:
                result.append(end-start + 1)
                start = end+1
                end = start
        
        return result