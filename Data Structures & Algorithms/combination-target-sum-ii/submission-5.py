class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        n = len(candidates)
        candidates.sort()
        if not candidates:
            return []

        def backtrack(current: List[int], index: int, total: int) -> None:
            if total == target:
                result.append(current.copy())
                return
            if index >= n or total > target:
                return
            # At each node, I add the next element, and recurse
            current.append(candidates[index])
            backtrack(current, index + 1, total + candidates[index])
            curr_num = current.pop()
            while index < n and candidates[index] == curr_num:
                index += 1
            backtrack(current, index, total)

            
        backtrack(current, 0, 0)
        return result
