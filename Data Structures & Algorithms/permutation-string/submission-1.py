class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash_map_one = {}
        hash_map_two = {}
        for i in range(len(s1)):
            hash_map_one[s1[i]] = hash_map_one.get(s1[i], 0) + 1
            hash_map_two[s2[i]] = hash_map_two.get(s2[i], 0) + 1
        left = 0
        right = len(s1)
        while right < len(s2):
            if hash_map_one == hash_map_two:
                return True
            else:
                hash_map_two[s2[right]] = hash_map_two.get(s2[right], 0) + 1
                hash_map_two[s2[left]] = hash_map_two.get(s2[left]) - 1
                if hash_map_two.get(s2[left]) == 0:
                    hash_map_two.pop(s2[left])
                left += 1
                right += 1
        return hash_map_one == hash_map_two
