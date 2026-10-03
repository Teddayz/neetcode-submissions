class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)
        
        def backtrack(start: int, partitions: List[str]) -> None:           
            if start == n:
                result.append(partitions.copy())
                return
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if self.isPalindrome(substring):
                    partitions.append(substring)
                    backtrack(end, partitions)
                    partitions.pop()
                
        backtrack(0, [])
        return result
    
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


            