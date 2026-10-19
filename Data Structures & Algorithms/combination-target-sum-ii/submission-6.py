class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(index: int, curr: List[int]) -> None:
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if index == n or sum(curr) > target:
                return

            curr.append(candidates[index])
            backtrack(index + 1, curr)
            curr_num = curr.pop()
            while index < n and candidates[index] == curr_num:
                index += 1
            backtrack(index, curr)
        backtrack(0, [])
        return res
                
