class Solution:
    def rob(self, nums: List[int]) -> int:
        
        value1 = 0
        value2 = 0

        for i in range(len(nums)-1,-1,-1):
            current_house = nums[i]
            print(current_house, value1, value2)
            tmp = value2
            value2 = max(current_house + value1, value2)
            value1 = tmp


        return value2
