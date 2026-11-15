class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        s = set()

        for i in range(len(triplets)):
            print(s)
            valid = True
            for j in range(3):
                if triplets[i][j] > target[j]:
                    valid = False
                    break
            if not valid:
                continue
            
            for j in range(3):
                if triplets[i][j] == target[j]:
                    s.add(j)
            
            
        return len(s) == 3