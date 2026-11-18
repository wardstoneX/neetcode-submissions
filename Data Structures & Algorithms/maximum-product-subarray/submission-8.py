class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        maxProduct, minProduct = 1,1

        for n in nums:

            if n == 0:
                maxProduct, minProduct = 1,1 
                result = max(result, 0) 
                continue
            
            tmp = n*maxProduct

            maxProduct = max(n*maxProduct, n*minProduct, n)
            minProduct = min(tmp, n, n*minProduct)
            result = max(result, maxProduct)
        return result