class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for stone in stones:
                heapq.heappush(heap, -stone)
        
        while heap and len(heap)>1:
            val1 = - heapq.heappop(heap)
            val2 = - heapq.heappop(heap)
            
            if val1 != val2:
                heapq.heappush(heap, -abs(val1-val2))
        
        if not heap:
            return 0
        return -heap[0]