class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i,arr):
            if i < 0:
                return arr
            
            result = []
            for p in arr:
                for j in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(j, nums[i])
                
                    result.append(p_copy)

            return backtrack(i-1, result)
        
        return backtrack(len(nums)-1, [[]])


        