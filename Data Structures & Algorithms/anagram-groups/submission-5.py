class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        res = []

        for i in range(len(strs)):
            sorted_s = tuple(sorted(strs[i]))
            hashMap[sorted_s].append(strs[i])
            
        for _, v in hashMap.items():
            res.append(v)
            
        return res