class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # At each step, check if its a palindrome, if it is, I add it to current list
        # Go to that index
        res = []
        n = len(s)
        def backtrack(i: int, curr: List[str]) -> None:
            if i >= n:
                res.append(curr.copy())
                return
            for index in range(i + 1, n + 1):
                substring = s[i:index]
                if self.isPalindrome(substring):
                    curr.append(substring)
                    backtrack(index, curr)
                    curr.pop()
            

        backtrack(0, [])
        return res

    
    def isPalindrome(self, word: str) -> bool:
        start = 0
        end = len(word) - 1
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True