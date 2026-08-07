class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        left = 0
        right = 0
        start = 0
        end = len(s)
        hash_map_base = {}
        hash_map = {}
        valid = False
        for char in t:
            hash_map_base[char] = hash_map_base.get(char, 0) + 1
        while right < len(s):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1
            if self.isValidWindow(hash_map_base, hash_map):
                valid = True
                # Shrink until the window is valid
                while left <= right and self.isValidWindow(hash_map_base, hash_map):
                    hash_map[s[left]] = hash_map.get(s[left]) - 1
                    if hash_map[s[left]] == 0:
                        hash_map.pop(s[left])
                    left += 1
                # Add back the previous element that made is a valid window
                left = left - 1
                hash_map[s[left]] = hash_map.get(s[left], 0) + 1
                # Get smallest length of substring
                if (right - left + 1) < (end - start + 1):
                    start = left
                    end = right
                hash_map[s[left]] = hash_map.get(s[left], 0) - 1
                if hash_map[s[left]] == 0:
                    hash_map.pop(s[left])
                left += 1               
            right += 1
        if not valid:
            return ""
        return s[start:end + 1]
    
    def isValidWindow(self, hash_map_base: dict, hash_map: dict) -> bool:
        for (key, val) in hash_map_base.items():
            if hash_map.get(key, 0) < val:
                return False  
        return True
