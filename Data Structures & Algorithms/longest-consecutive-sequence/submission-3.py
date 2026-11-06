class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            s = set(nums)
            r = set()
            h = {}
            length = 0
            for  n in nums: 
                if n in r:
                    continue
                if n -1 not in s:
                    h[n] = [n]
                    r.add(n)
                    length = max(length, 1)
                    continue
                j=0
                m = []
                while n-j in s:
                    #print(n,m, h)
                    if n-j in h:
                        tmp = h[n-j]
                        m.extend(tmp)
                        h.pop(n-j)
                        h[n] = tmp
                        break
                    m.append(n-j)
                    r.add(n-j)
                    j+=1
                h[m[0]] = m
                length = max(length, len(m))
            #print(h)
            return length

                        

                    