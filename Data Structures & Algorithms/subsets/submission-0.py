class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr_subset = []  
        def backtrack(start, current):
            result.append(curr_subset[:])
            for i in range(start, len(nums)):
                curr_subset.append(nums[i])
                backtrack(i + 1, curr_subset)
                curr_subset.pop()
        backtrack(0, curr_subset)
        return result