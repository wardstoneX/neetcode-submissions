class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0
        for i in range(len(s)):
            r,l = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l +1
                if length > resLen:
                    result = s[l:r+1]
                    resLen = max(resLen, length)
                r += 1
                l -= 1
            
            l,r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l +1
                if length > resLen:
                    result = s[l:r+1]
                    resLen = max(resLen, length)
                r += 1
                l -= 1
        return result


        