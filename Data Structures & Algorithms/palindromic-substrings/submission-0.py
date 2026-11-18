class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            r,l = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]: 
                result +=1
                r += 1
                l -= 1
            
            l,r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                result +=1
                r += 1
                l -= 1
        return result