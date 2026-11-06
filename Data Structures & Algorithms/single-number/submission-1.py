class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]

        i = 1

        while i < len(nums):
            result = result ^ nums[i]
            i +=1
        return result

        