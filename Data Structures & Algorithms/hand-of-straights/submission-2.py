class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hmap = defaultdict(int)
        for i in range(len(hand)):
            hmap[hand[i]] = hmap.get(hand[i], 0) + 1
        
        cards = list(hmap.keys())
        heapq.heapify(cards)

        while hmap:

            minHeapElement = cards[0]
            for i in range(groupSize):
                
                element = minHeapElement + i
                if hmap[element] == 0:
                    return False

                
                hmap[element] -= 1 

                if hmap[element] == 0:
                    hmap.pop(element)

                    heapq.heappop(cards)

        return True
                 

