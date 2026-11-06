class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for _ in range(len(nums) + 1)]
        
        freq = {} # 
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for num, count in freq.items():
            arr[count].append(num)

        result = []
        for n in reversed(arr):
            
            while len(n) != 0:
                result.append(n.pop())
                if len(result) == k:
                    return result

         