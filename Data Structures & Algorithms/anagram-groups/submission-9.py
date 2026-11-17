class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_map = {}
        res = []
        index = 0
        for s in strs:
            # Sort the string first and check whether it is present in the hash_map
            sorted_s = sorted(s)
            if tuple(sorted_s) not in hash_map:
                hash_map[tuple(sorted_s)] = index
                index += 1
            i = hash_map[tuple(sorted_s)]
            if len(res) == i:
                res.append([])
            res[i].append(s)

        return res
            
            
            