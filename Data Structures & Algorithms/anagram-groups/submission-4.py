class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        result = []

        index = 0
        for s in strs:
            sorted_s = sorted(s)
            sorted_s = tuple(sorted_s)
            if sorted_s not in check:
                check[sorted_s] = index
                result.append([])
                result[index].append(s)
                index += 1
                continue
            result[check[sorted_s]].append(s)

        return result
        
            