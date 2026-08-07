class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = "".join(char for char in s if char.isalnum()).lower()
        left = 0
        right = len(cleaned_str) - 1
        while left < right:
            if cleaned_str[left] == cleaned_str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True