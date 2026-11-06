class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <=2:
            return 1
        f = 0
        s = 1
        t = 1

        i =3

        while i <= n:
            tmp = f+s+t

            f = s
            s = t
            t = tmp

            i+=1
        return t
        