class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        val1 = 1
        val2 = 1

        for i in range(n-2, -1, -1):

            tmp = val1 + val2

            val1 = val2
            val2 = tmp
        return val2        