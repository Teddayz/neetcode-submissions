class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        min_heap = list(freq.keys())
        heapq.heapify(min_heap)

        while min_heap:
            curr = min_heap[0]
            
            if freq[curr] == 0:
                heapq.heappop(min_heap)
                continue
            
            for i in range(groupSize):
                if curr in freq and freq[curr] > 0:
                    freq[curr] -= 1
                    curr += 1
                else:
                    return False
            
        return True


        