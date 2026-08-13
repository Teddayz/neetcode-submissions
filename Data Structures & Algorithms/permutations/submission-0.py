class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        curr = []
        visited = {}
        for i in range(n):
            visited[nums[i]] = False

        def backtrack(i):
            if (len(curr) == n):
                result.append(curr.copy())
                return
            for num in nums:
                if visited[num] == False:
                    curr.append(num)
                    visited[num] = True
                    backtrack(i + 1)
                    curr.pop()
                    visited[num] = False
        backtrack(0)
        return result
