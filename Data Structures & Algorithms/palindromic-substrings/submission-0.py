class Solution:
    def countSubstrings(self, s: str) -> int:
        totalCount = 0
        for i in range(len(s)):
            count1 = self.expandFromCenter(s, i, i)
            count2 = self.expandFromCenter(s, i, i + 1)
            totalCount += count1 + count2

        return totalCount
        
    def expandFromCenter(self, s: str, start_index: int, end_index: int) -> int:
        count = 0
        while start_index >= 0 and end_index < len(s):
            if s[start_index] == s[end_index]:
                count += 1
                start_index -= 1
                end_index += 1
            else:
                break
        return count