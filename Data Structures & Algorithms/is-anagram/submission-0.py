class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hash_map_s[s[i]] = hash_map_s.get(s[i], 0) + 1
            hash_map_t[t[i]] = hash_map_t.get(t[i], 0) + 1
        return hash_map_s == hash_map_t