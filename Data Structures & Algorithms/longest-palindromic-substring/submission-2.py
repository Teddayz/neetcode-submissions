class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        maxLength = 0

        for i in range(len(s)):
            # If odd only 1 letter
            res1 = self.expandAroundCenter(s, i, i)
            print(res1)
            l1 = res1[1] - res1[0]
            # if its two letters
            res2 = self.expandAroundCenter(s, i, i + 1)
            l2 = res2[1] - res2[0]
            if l2 > l1 and l2 > maxLength:
                start = res2[0]
                end = res2[1]
                maxLength = l2
           
            if l1 > maxLength:
                start = res1[0]
                end = res1[1]
                maxLength = l1

        return s[start:end + 1]
        
    def expandAroundCenter(self, s: str, start_index: int, end_index: int) -> List[int]:
        
        while start_index >= 0 and end_index < len(s):
            if s[start_index] == s[end_index]:
                start_index -= 1
                end_index += 1
            else:
                break

        return [start_index + 1, end_index - 1]