class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        if not nums:
            return result
        def backtrack(curr: List[int], i: int) -> None:
            if i == len(nums):
                result.append(curr.copy())
                return
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()
            backtrack(curr, i + 1)

        backtrack(curr, 0)
        return result
