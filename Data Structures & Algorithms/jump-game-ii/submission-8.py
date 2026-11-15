class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0,0
        jumps = 0
        while r < len(nums) - 1:
            if r >= len(nums):
                return jumps
            jumps += 1

            i = l
            farthest = 0
            while i <= r:
                farthest = max(farthest,  i + nums[i])
                i +=1
            
            l = r+1 
            r = farthest
        return jumps