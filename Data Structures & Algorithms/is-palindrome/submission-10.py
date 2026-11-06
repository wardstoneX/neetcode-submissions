class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1

        while l <= r:
            print(l, r, s[l].isalnum(), s[r].isalnum(), s[l].lower() == s[r].lower() )
            if s[l].isalnum() and s[r].isalnum() and s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            elif s[l].isalnum() and s[r].isalnum() and s[l].lower() != s[r].lower():
                return False
            else:
                while l < len(s) and not s[l].isalnum() :
                    print("inc l")
                    l += 1
                while r >= 0 and not s[r].isalnum():
                    print("dec r")
                    r -= 1
    
        return True