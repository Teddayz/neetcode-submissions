class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        n = len(nums)
        visited = set()
        def backtrack(current: List[int], index: int) -> None:
            if len(current) == n:
                result.append(current.copy())
                return
            if index >= n:
                return
            for num in nums:
                if num not in visited:  
                    current.append(num)
                    visited.add(num)
                    backtrack(current, index + 1)
                    current.pop()
                    visited.remove(num)
                    backtrack(current, index + 1)
                
        backtrack(current, 0)
        return result
            