class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr: List[int], index: int) -> None:
            if index >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[index])
            backtrack(curr, index + 1)
            curr.pop()
            backtrack(curr, index + 1)
        backtrack([], 0)
        return res