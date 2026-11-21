class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrace(i, e, arr):
            if i >= len(nums):
                result.append(arr.copy())
                return
            elif nums[i] == e:
                backtrace(i+1, e, arr)
                return

            arr.append(nums[i])
            backtrace(i+1, e, arr)

            arr.pop()
            backtrace(i+1, nums[i], arr)
        
        backtrace(0, 21, [])
        return result

