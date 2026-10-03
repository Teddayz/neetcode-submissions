class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        currSum = nums[0]
        globalMax = nums[0]
        for i in range(1, n):
            if currSum < 0:
                # Start from here
                currSum = nums[i]
                globalMax = max(currSum, globalMax)
                continue
            # Case 2: I include the number
            currSum += nums[i]
            globalMax = max(currSum, globalMax)
            
        return globalMax if globalMax != -math.inf else max(nums)

        