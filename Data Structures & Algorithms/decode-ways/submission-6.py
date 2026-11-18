class Solution:
    def numDecodings(self, ss: str) -> int:
        cache ={} 
        def dfs(s):
            if s in cache:
                return cache[s]

            if not s:
                return 1

            if s[0] == '0':
                return 0

            result = dfs(s[1:])

            if len(s) >= 2 and (
                (s[0] == '2' and s[1] in "0123456") or
                (s[0] == '1' and s[1] in "0123456789")
            ):
                result += dfs(s[2:])
            cache[s] = result
            return result

        return dfs(ss)
        