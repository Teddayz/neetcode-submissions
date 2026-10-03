class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = -math.inf
        minimum = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            # Case 1: Start a new subarray
            curr = nums[i]
            # Case 2: Multiplying with the previous min product
            currMin = minimum * nums[i]
            # Case 3: Multiplying with the previous max product
            currMax = maximum * nums[i]

            tempMax = max(currMax, currMin)
            maximum = max(tempMax, curr)
            tempMin = min(currMin, currMax)
            minimum = min(tempMin, curr)
            globalMax = max(globalMax, maximum)
        return globalMax if globalMax != -math.inf else nums[0]