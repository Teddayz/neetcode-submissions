class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        curr = []
        visited = set()
        def backtrack():
            if (len(curr) == n):
                result.append(curr.copy())
                return
            for num in nums:
                if num not in visited:
                    curr.append(num)
                    visited.add(num)
                    backtrack()
                    curr.pop()
                    visited.remove(num)
        backtrack()
        return result
