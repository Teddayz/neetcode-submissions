class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array to all -1 to denote that it is impossible to make up that amount
        if amount == 0:
            return 0

        frontier = deque()
        frontier.append((amount, 0)) # Pass in the remaining + number of coins
        visited = set()

        while frontier:
            node = frontier.popleft()
            remaining = node[0]
            if remaining in visited:
                continue
            visited.add(remaining)
            numOfCoins = node[1]
            for coin in coins:
                temp = remaining - coin
                if temp == 0:
                    return numOfCoins + 1
                elif temp > 0:
                    frontier.append((temp, numOfCoins + 1))
        
        return -1