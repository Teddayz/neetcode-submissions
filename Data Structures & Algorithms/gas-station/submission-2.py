class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        totalTank = 0
        start_index = 0
        for i in range(len(gas)):
            totalTank += gas[i] - cost[i]
            if totalTank < 0:
                totalTank = 0
                start_index = i + 1
                continue
        return start_index