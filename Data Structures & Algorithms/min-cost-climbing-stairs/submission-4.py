class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        elif len(cost) == 1:
            return cost[0]

        f = 0
        s = 0

        i = 0

        while i < len(cost)-1:
            tmp = min(f + cost[i], s + cost[i+1])
            f = s
            s = tmp

            i+=1
        return s




        