class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #abba,  ab ba len(abba) = 4
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for c in range(len(s)-1, -1, -1):

            for w in wordDict:
                #print(c, w, s[c : c + len(w)],s[c : c + len(w)] == w )
                if c + len(w) <= len(s) and s[c : c + len(w)] == w:
                    dp[c] = dp[c+len(w)]
                
                if dp[c]:
                    break
        #print(dp[0])
        return dp[0]
        