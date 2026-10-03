class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        min_heap = list(freq.keys())
        heapq.heapify(min_heap)

        while min_heap:
            smallest = min_heap[0]
            if freq[smallest] == 0:
                heapq.heappop(min_heap)
                continue

            count = freq[smallest]

            for i in range(groupSize):
                card = smallest + i
                if card in freq and freq[card] > 0:
                    freq[card] -= 1
                else:
                    return False
        return True


        