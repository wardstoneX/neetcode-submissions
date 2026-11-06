class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 0
        i = n

        while i >= 0:
            s = first + second
            first = second
            second = s
            i -=1
        return second
        