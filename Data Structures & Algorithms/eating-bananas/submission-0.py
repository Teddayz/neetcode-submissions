import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        fastest_rate = len(piles)
        for pile in piles:
            fastest_rate = max(fastest_rate, pile)
        slowest_rate = 1
        # Minimum banana per hour = k
        # Fastest time = len(piles) -> This means that my k = maximum of array
        # Slowest time -> k == 1 where i eat 1 banana per hour
        while slowest_rate <= fastest_rate:
            middle_rate = (slowest_rate + fastest_rate) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / middle_rate)
            if hours > h:
                slowest_rate = middle_rate + 1
            else:
                fastest_rate = middle_rate - 1
            # print(fastest_rate)
        return slowest_rate