class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {} # maps number to index

        for i, n in enumerate(nums):
            x = target - n
            if x in hmap:
                return [hmap[x], i]
            else:
                hmap[n] = i
        return [] 
        