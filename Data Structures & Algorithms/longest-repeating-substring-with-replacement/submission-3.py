from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        # The window length - maxFreq msut be <= k
        maxFreq = 0
        freq_map = defaultdict(int)
        res = 0
        while right < len(s):
            freq_map[s[right]] += 1
            if freq_map[s[right]] > maxFreq:
                maxFreq = freq_map[s[right]]
            if right - left + 1 - maxFreq > k:
                freq_map[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
            
