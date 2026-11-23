class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for point in points:
            val = point[0] * point[0] + point[1] *point[1]
            heapq.heappush(heap, (-val, [point[0], point[1]]))
        
        while heap and len(heap) > k:
            heapq.heappop(heap)
        
        result = []

        while heap:

            result.append(heapq.heappop(heap)[1])

        return result