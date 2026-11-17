class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        value1 = 0
        value2 = 0

        for i in range(len(cost)):

            tmp = cost[i] + min(value1, value2)
            value2 = value1    
            value1 = tmp
        return min(value1,value2)
                