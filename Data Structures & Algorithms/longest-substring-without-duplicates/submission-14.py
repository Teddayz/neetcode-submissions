class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        left, right = 0, 0
        res = 0

        while right < len(s):
            if s[right] in hash_map and hash_map[s[right]] >= left:
                left = max(hash_map[s[right]], left) + 1
            hash_map[s[right]] = right
            res = max(res, right - left + 1)
            right += 1
        return res