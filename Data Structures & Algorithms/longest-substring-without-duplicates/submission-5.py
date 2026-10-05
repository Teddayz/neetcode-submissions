class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, res = 0, 0, 0
        hashMap = {}
        while right < len(s):
            if s[right] in hashMap:
                left = max(hashMap[s[right]] + 1, left)
            hashMap[s[right]] = right
            res = max(res, right - left + 1)
            # print(res)
            right += 1
        return res