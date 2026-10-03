class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        current = []
        n = len(nums)

        def backtrack(current: List[int], index: int) -> None:
            if index >= n:
                result.append(current.copy())
                return
            current.append(nums[index])
            backtrack(current, index + 1)
            curr_num = current.pop()
            while index < n and nums[index] == curr_num:
                index += 1
            backtrack(current, index)
        backtrack(current, 0)
        return result