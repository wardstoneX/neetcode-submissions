class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
  
    def decode(self, s: str) -> List[str]:
        results = []

        read = ""
        number = 0
        i = 0
        # 2#ab3#cde
        while i < len(s):
            if s[i].isdigit():
                read += s[i]
                i +=1
            elif s[i] == "#":
                number = int(read)
                results.append(s[i+1:i+number +1])
                read = ""
                i += number + 1

        return results

