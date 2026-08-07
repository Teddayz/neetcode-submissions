import heapq
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxLength = 0
        hash_map = {}
        max_freq = 0
        while right < len(s):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1
            max_freq = max(max_freq, hash_map.get(s[right]))
            window_length = right - left + 1
            if window_length - max_freq > k:
                hash_map[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
            right += 1
            
        return maxLength
                
        