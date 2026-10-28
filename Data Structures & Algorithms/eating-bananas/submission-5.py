class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slowest = 1
        fastest = max(piles)
        res = math.inf

        while slowest <= fastest:
            time_taken = 0
            curr = (slowest + fastest) // 2
            for pile in piles:
                time_taken += math.ceil(pile / curr)
            if time_taken <= h:
                res = curr
                fastest = curr - 1
            else:
                slowest = curr + 1
        return res if res != math.inf else 0