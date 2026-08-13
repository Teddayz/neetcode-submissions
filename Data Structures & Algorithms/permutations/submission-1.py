class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        curr = []

        def backtrack(i):
            if (len(curr) == n):
                result.append(curr.copy())
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(i + 1)
                    curr.pop()
        backtrack(0)
        return result
