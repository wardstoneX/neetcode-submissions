class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numbers = []
        self.k = k
        heapq.heapify(self.numbers)
        for num in nums:
            heapq.heappush(self.numbers, num)
        
        print(self.numbers)
        
        

    def add(self, val: int) -> int:
        print(self.numbers)

        heapq.heappush(self.numbers, val)

        while len(self.numbers) > self.k:
            heapq.heappop(self.numbers)
        
        return self.numbers[0]
        
