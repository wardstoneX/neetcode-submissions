class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = set()
        while True:
            if n == 1:
                return True
            elif n in s:
                return False
            s.add(n)
            sum = 0
            for digit in str(n):
                d = int(digit)
                d = d*d
                sum += d
            n = sum
            print(sum)