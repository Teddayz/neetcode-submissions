class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        left, right = 0, 0
        res = 0
        while right < len(s):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        return res