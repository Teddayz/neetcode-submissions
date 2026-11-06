class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        hashMap = {}
        res = 0
        # if len(s) == 1:
        #     return 1

        while right < len(s):
            # If the new character is in the window, bring left pointer to the most right of this char
            if s[right] in hashMap and hashMap[s[right]] >= left:
                left = max(left, hashMap[s[right]]) + 1
            
            hashMap[s[right]] = right
            res = max(res, right - left + 1)
            right += 1

        return res
