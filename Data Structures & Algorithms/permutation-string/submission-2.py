class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        hash_map_s1 = {}
        hash_map_s2 = {}

        for i in range(len(s1)):
            hash_map_s1[s1[i]] = hash_map_s1.get(s1[i], 0) + 1
            hash_map_s2[s2[i]] = hash_map_s2.get(s2[i], 0) + 1
        
        start = 0
        end = len(s1)
        if hash_map_s1 == hash_map_s2:
            return True

        while end < len(s2):
            hash_map_s2[s2[end]] = hash_map_s2.get(s2[end], 0) + 1
            hash_map_s2[s2[start]] -= 1
            if hash_map_s2[s2[start]] == 0:
                hash_map_s2.pop(s2[start])
            if hash_map_s2 == hash_map_s1:
                return True
            start += 1
            end += 1
            
        return False