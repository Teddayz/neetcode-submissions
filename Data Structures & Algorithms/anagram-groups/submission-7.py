class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = defaultdict(list)
        res = []

        for word in strs:
            sorted_word = tuple(sorted(word))
            hashMap[sorted_word].append(word)
        
        for _, word in hashMap.items():
            res.append(word)
        
        return res