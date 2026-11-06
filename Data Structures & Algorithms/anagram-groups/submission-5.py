class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}
        for i, s in enumerate(strs):
            arr = [0] * 26
            for c in s:
                index = ord(c) - ord('a') 
                arr[index] = 1 + arr[index]
            if tuple(arr) in hmap:
                hmap[tuple(arr)].append(s)
            else:
                hmap[tuple(arr)] = [s] 
        return list(hmap.values())


