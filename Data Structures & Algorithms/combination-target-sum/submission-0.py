class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(curr: List[int], i: int, curr_sum: int) -> None:
            if curr_sum == target:
                result.append(curr.copy())
                return
            if curr_sum > target:
                return
            else:
                while i < len(nums):
                    curr.append(nums[i])
                    backtrack(curr, i, curr_sum + nums[i])
                    curr.pop()
                    i += 1

        backtrack(curr, 0, 0)
        return result