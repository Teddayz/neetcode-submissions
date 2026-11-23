from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if s1 == s2:
            return True
        left, right = 0, len(s1)
        hash_map_s1 = defaultdict(int)
        hash_map_s2 = defaultdict(int)

        for i in range(len(s1)):
            hash_map_s1[s1[i]] += 1
            hash_map_s2[s2[i]] += 1

        if hash_map_s1 == hash_map_s2:
            return True
        while right < len(s2):
            hash_map_s2[s2[right]] += 1
            hash_map_s2[s2[left]] -= 1
            if hash_map_s2[s2[left]] == 0:
                hash_map_s2.pop(s2[left])
            if hash_map_s1 == hash_map_s2:
                return True
            left += 1
            right += 1
        return False