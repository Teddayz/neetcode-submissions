class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in check:
                check[key] = []
            check[key].append(s)
        return list(check.values())
        
            