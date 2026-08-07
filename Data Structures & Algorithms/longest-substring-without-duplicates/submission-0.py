class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        maxLength = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] in hash_set:
                while left < right and s[right] in hash_set:
                    hash_set.remove(s[left])
                    left += 1
            hash_set.add(s[right])
            maxLength = max(maxLength, right - left + 1)
            right += 1
        return maxLength